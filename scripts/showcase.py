#!/usr/bin/env python3
"""Render showcase scaffolding and track stage fingerprints without external dependencies."""
import argparse
from contextlib import contextmanager
from html import escape
import json
import os
from pathlib import Path
import re
from string import Template
import sys
import tempfile

from validate import PUBLIC_MANIFEST, SITEMAP_NS, check_site, https_url, public_name, safe_path, sha

PACKAGE = Path(__file__).resolve().parents[1]
TEMPLATES = PACKAGE / "templates"
FACTS = ".agents/product-facts.json"
STATE = ".agents/showcase/state.json"
STATE_DIR = ".agents/showcase"
RENDERER = ".agents/showcase/validate.py"
WORKFLOW = ".github/workflows/oss-showcase-pages.yml"
FORMATS = {
    "logo": {".svg", ".png", ".webp"},
    "favicon": {".svg", ".png", ".ico"},
    "social": {".png", ".jpg", ".jpeg"},
    "demo": {".gif", ".mp4", ".webm"},
    "poster": {".png", ".jpg", ".jpeg", ".webp"},
}
PROFILES = {"cli", "mcp", "skill", "plugin", "library", "web"}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def template(name, root=None):
    if root is not None:
        override = safe_path(root, f"{STATE_DIR}/templates/{name}")
        if override.exists():
            return override.read_text(encoding="utf-8")
    return (TEMPLATES / name).read_text(encoding="utf-8")


def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temp = Path(handle.name)
        try:
            handle.write(data)
            handle.close()
            os.replace(temp, path)
        finally:
            temp.unlink(missing_ok=True)


@contextmanager
def writing(root):
    lock = safe_path(root, f"{STATE_DIR}/write-lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.mkdir()
    try:
        yield
    finally:
        lock.rmdir()


def plain_md(text):
    return re.sub(r"([\\`*_{}\[\]()<>#!|&])", r"\\\1", text)


def evidence(value, root):
    if not isinstance(value, dict) or not all(value.get(key) for key in ("summary", "setup", "example")):
        raise ValueError("Provide verified evidence for the summary, setup and example.")
    for refs in value.values():
        if not isinstance(refs, list) or not refs:
            raise ValueError("Each evidence field needs a nonempty list of repository paths.")
        for ref in refs:
            if not safe_path(root, ref).is_file():
                raise ValueError(f"Evidence file is missing: {ref}")


def render(root):
    facts = read_json(safe_path(root, FACTS))
    profile = facts["profile"]
    if profile not in PROFILES:
        raise ValueError("Choose a supported profile.")
    defaults = json.loads(template(f"profiles/{profile}.json"))
    for key in ("name", "summary", "setup", "example"):
        if not isinstance(facts.get(key), str) or not facts[key].strip():
            raise ValueError(f"A verified {key} is required.")
    evidence(facts["evidence"], root)
    canonical = facts["site_url"].rstrip("/") + "/"
    site = https_url(canonical)
    repo = facts["repo_url"]
    https_url(repo)
    labels = facts.get("labels", {})
    quickstart = labels.get("quickstart", defaults["quickstart"])
    lang = facts.get("lang", "en")
    if not re.fullmatch(r"[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*", lang):
        raise ValueError("Invalid document language.")
    code_language = facts.get("code_language", "")
    if not re.fullmatch(r"[A-Za-z0-9_+-]*", code_language):
        raise ValueError("Invalid code language.")

    assets = facts.get("assets", {})
    public = {"assets/showcase.css": template("showcase.css", root).encode()}
    for role, entry in assets.items():
        name = entry["path"]
        if role not in FORMATS or not public_name(name) or Path(name).suffix not in FORMATS[role]:
            raise ValueError(f"Invalid public asset for role: {role}")
        if role in {"social", "demo"} and not entry.get("alt", "").strip():
            raise ValueError(f"Provide a public description for {role}.")
        if role == "demo" and not entry.get("caption", "").strip():
            raise ValueError("Provide a demo caption describing the observable result.")
        public[name] = safe_path(root, f"docs/{name}").read_bytes()

    title = facts["name"]
    summary = facts["summary"]
    result = facts.get("result", "")
    sections = facts.get("sections", [])
    for section in sections:
        key = section["title"]
        if not facts["evidence"].get(key):
            raise ValueError("Each public section needs source evidence keyed by its title.")
    if result and not facts["evidence"].get("result"):
        raise ValueError("The example result needs evidence.")
    schema_type = facts.get("schema_type", "")
    if schema_type not in {"", "SoftwareApplication", "WebApplication", "SoftwareSourceCode"}:
        raise ValueError("Choose an applicable factual schema type or leave it blank.")
    schema = ""
    if schema_type:
        payload = json.dumps({
            "@context": "https://schema.org", "@type": schema_type, "url": canonical,
            "name": title, "description": summary,
        }, ensure_ascii=False).replace("<", "\\u003c")
        schema = f'<script type="application/ld+json">{payload}</script>'

    logo_html = logo_md = demo_html = demo_md = favicon = social = ""
    if logo := assets.get("logo"):
        logo_html = f'<img class="logo" src="{logo["path"]}" alt="">'
        logo_md = f'![{plain_md(title)} logo](docs/{logo["path"]})\n'
    if icon := assets.get("favicon"):
        favicon = f'<link rel="icon" href="{icon["path"]}">'
    if image := assets.get("social"):
        url = escape(canonical + image["path"])
        alt = escape(image["alt"])
        social = "\n  ".join(
            f'<meta {kind}="{key}" content="{value}">' for kind, key, value in (
                ("property", "og:image", url), ("property", "og:image:alt", alt),
                ("name", "twitter:image", url), ("name", "twitter:image:alt", alt),
            )
        )
    if demo := assets.get("demo"):
        path = demo["path"]
        alt = escape(demo["alt"])
        caption = escape(demo["caption"])
        if path.endswith(".gif"):
            player = f'<a href="{path}">{escape(labels.get("demo", "Open animated demo"))}</a>'
            demo_md = f'![{plain_md(demo["alt"])}](docs/{path})\n'
        else:
            poster = f' poster="{assets["poster"]["path"]}"' if "poster" in assets else ""
            player = f'<video controls muted playsinline preload="none" aria-label="{alt}"{poster} src="{path}"></video>'
            demo_md = f'[{plain_md(demo["alt"])}](docs/{path})\n'
        demo_html = f"<figure>{player}<figcaption>{caption}</figcaption></figure>"
        demo_md += f'{plain_md(demo["caption"])}\n\n'

    page = Template(template("index.html", root)).substitute(
        title=escape(title), summary=escape(summary), canonical=escape(canonical), repo=escape(repo),
        lang=escape(lang), card="summary_large_image" if social else "summary", social=social,
        favicon=favicon, schema=schema, demo=demo_html, logo=logo_html,
        quickstart=escape(quickstart), repository=escape(labels.get("repository", "Repository")),
        setup=escape(facts["setup"]), example=escape(facts["example"]),
        result=f"<p>{escape(result)}</p>" if result else "",
        sections="\n    ".join(
            f"<section><h2>{escape(s['title'])}</h2><p>{escape(s['body'])}</p></section>" for s in sections
        ),
    )
    runs = re.findall(r"`+", facts["example"])
    fence = "`" * max(3, max(map(len, runs), default=0) + 1)
    readme = Template(template("README.md.in", root)).substitute(
        title=plain_md(title), summary=plain_md(summary), canonical=canonical, logo=logo_md, demo=demo_md,
        quickstart=plain_md(quickstart), setup=plain_md(facts["setup"]), example=facts["example"],
        fence=fence, code_language=code_language, result=plain_md(result),
        sections="".join(f"\n## {plain_md(s['title'])}\n\n{plain_md(s['body'])}\n" for s in sections),
    )
    public["index.html"] = page.encode()
    public["sitemap.xml"] = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="{SITEMAP_NS}"><url><loc>{escape(canonical)}</loc></url></urlset>\n'.encode()
    if site.path == "/":
        public["robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {canonical}sitemap.xml\n".encode()
    if facts.get("llms_txt") is True:
        public["llms.txt"] = f"# {plain_md(title)}\n\n> {plain_md(summary)}\n\n## Documentation\n\n- [Project homepage]({canonical})\n- [Source repository]({repo})\n".encode()
    check_site(canonical, public)
    generated = {f"docs/{name}": data for name, data in public.items()
                 if name not in {entry["path"] for entry in assets.values()}}
    generated.update({
        "README.md": readme.encode(),
        RENDERER: (PACKAGE / "scripts/validate.py").read_bytes(),
        WORKFLOW: template("pages.yml").replace("$site_url", json.dumps(canonical)).encode(),
        PUBLIC_MANIFEST: json_bytes({"url": canonical, "files": {name: sha(data) for name, data in public.items()}}),
    })
    return generated


def read_state(root):
    path = safe_path(root, STATE)
    return read_json(path) if path.exists() else {"generated": {}, "stages": {}}


def file_digest(root, name):
    path = safe_path(root, name)
    if not path.exists():
        return None
    return sha(path.read_bytes())


def snapshot(root, spec):
    return {
        key: {name: file_digest(root, name) for name in sorted(set(spec[key]))}
        for key in ("inputs", "outputs")
    }


def stages(root, args):
    spec = read_json(args.spec)
    stored = read_state(root)
    current = {name: snapshot(root, paths) for name, paths in sorted(spec.items())}
    if args.command == "record":
        value = current[args.stage]
        if not value["inputs"] or not value["outputs"] or None in value["outputs"].values():
            raise ValueError("Record only a completed stage with reviewed inputs and existing outputs.")
        stored["stages"][args.stage] = value
        write_state(root, stored)
        print(f"Recorded {args.stage}.")
        return
    for name, value in current.items():
        saved = stored["stages"].get(name)
        if saved is None:
            reason = "unrecorded"
        elif saved["inputs"] != value["inputs"]:
            reason = "inputs changed"
        elif saved["outputs"] != value["outputs"] or None in value["outputs"].values():
            reason = "outputs changed or missing"
        else:
            reason = "current"
        print(f"{name}: {reason}")


def write_state(root, value):
    path = safe_path(root, STATE)
    data = json_bytes(value)
    if not path.exists() or path.read_bytes() != data:
        atomic(path, data)


def generate(root, args):
    outputs = render(root)
    if args.command == "preview":
        args.destination.mkdir()
        for name, data in outputs.items():
            key = safe_path(args.destination, name)
            atomic(key, data)
        print(f"Rendered draft files in {args.destination}. Existing project files are unchanged.")
        return
    ignored = set()
    if args.keep_readme:
        ignored.add("README.md")
    if args.keep_workflow or safe_path(root, WORKFLOW).exists():
        ignored.add(WORKFLOW)
    state = read_state(root)
    previously = state["generated"]
    next_state = dict(previously)
    changes = {}
    conflicts = []
    for name, data in outputs.items():
        if name in ignored:
            print(f"keep {name}")
            continue
        old = file_digest(root, name)
        new = sha(data)
        if old == new:
            status = "current"
        elif old is None:
            status = "create"
            changes[name] = data
        elif previously.get(name) == old:
            status = "update"
            changes[name] = data
        else:
            status = "conflict"
            conflicts.append(name)
        print(f"{status} {name}")
        next_state[name] = new
    for name in sorted(previously.keys() - outputs.keys()):
        print(f"retained outside generated output: {name}")
    if conflicts:
        raise ValueError("Reconcile differing existing files before applying. No generated files changed.")
    if args.command == "apply":
        for name, data in changes.items():
            atomic(safe_path(root, name), data)
            # Preserve the baseline after each completed write for safe retries.
            previously[name] = sha(data)
            write_state(root, state)
        state["generated"] = next_state
        write_state(root, state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("plan", "apply"):
        command = sub.add_parser(name)
        command.add_argument("--keep-readme", action="store_true")
        command.add_argument("--keep-workflow", action="store_true")
    preview = sub.add_parser("preview")
    preview.add_argument("destination", type=Path)
    for name in ("status", "record"):
        command = sub.add_parser(name)
        command.add_argument("spec", type=Path)
        if name == "record":
            command.add_argument("stage")
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    action = stages if args.command in {"status", "record"} else generate
    if args.command in {"apply", "record"}:
        with writing(root):
            action(root, args)
    else:
        action(root, args)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        sys.exit(f"Showcase failed: {error}")
