#!/usr/bin/env python3
"""Validate and optionally assemble a reviewed, explicitly listed Pages artifact."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import urljoin, urlsplit
from xml.etree import ElementTree

PUBLIC_MANIFEST = ".agents/showcase/public.json"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
PUBLIC_FILES = {"index.html", "sitemap.xml", "robots.txt", "llms.txt"}
ASSET_SUFFIXES = {".css", ".gif", ".ico", ".jpeg", ".jpg", ".mp4", ".png", ".svg", ".webm", ".webp"}
SECRET_PATTERN = re.compile(
    rb"-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:gh[pousr]_|github_pat_|sk-proj-)[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}"
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(root, name):
    if not isinstance(name, str) or not name or "\\" in name:
        raise ValueError("Expected a repository-relative path.")
    parts = name.split("/")
    if any(part in {"", ".", "..", ".git"} for part in parts):
        raise ValueError(f"Unsafe path: {name}")
    path = root
    for part in parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink is outside the managed file contract: {name}")
    return path


def public_name(name):
    path = PurePosixPath(name)
    return name in PUBLIC_FILES or (
        len(path.parts) >= 2 and path.parts[0] == "assets"
        and path.suffix in ASSET_SUFFIXES
        and all(re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*", part) for part in path.parts)
    )


def https_url(url):
    value = urlsplit(url)
    if (value.scheme != "https" or not value.hostname or value.username or value.password
            or value.query or value.fragment or any(c.isspace() for c in url)
            or not re.fullmatch(r"[A-Za-z0-9.:-]+", value.netloc)
            or any(not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.~-]*", p)
                   for p in value.path.strip("/").split("/") if p)
            or "//" in value.path):
        raise ValueError("Expected a clean HTTPS URL without credentials, query or fragment.")
    return value


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.meta = {}
        self.canonical = []
        self.h1 = 0
        self.title = False
        self.lang = ""
        self.json_ld = []
        self.schema_buffer = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if any(k.startswith("on") for k in a):
            raise ValueError("Inline event handlers are outside the static starter contract.")
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self.title = True
        if tag == "h1":
            self.h1 += 1
        if "id" in a:
            if a["id"] in self.ids:
                raise ValueError("Duplicate HTML id.")
            self.ids.add(a["id"])
        if tag == "img" and "alt" not in a:
            raise ValueError("Image missing alt attribute.")
        if tag in {"base", "embed", "object", "iframe"}:
            raise ValueError(f"Unsupported tag in the static starter: {tag}")
        if tag == "script":
            if a.get("type") == "application/ld+json" and "src" not in a:
                self.schema_buffer = ""
            elif a.get("src", "").startswith("assets/"):
                raise ValueError("Register and review custom JavaScript in the repository-specific validator.")
            else:
                raise ValueError("Unexpected script in the static starter.")
        if tag == "meta" and ("name" in a or "property" in a):
            self.meta[a.get("name") or a.get("property")] = a.get("content")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href"))
        for key in ("href", "src", "poster"):
            if a.get(key):
                self.links.append((tag, key, a[key]))

    def handle_data(self, data):
        if self.schema_buffer is not None:
            self.schema_buffer += data

    def handle_endtag(self, tag):
        if tag == "script" and self.schema_buffer is not None:
            self.json_ld.append(json.loads(self.schema_buffer))
            self.schema_buffer = None


def check_site(url, files):
    base = https_url(url)
    if not url.endswith("/"):
        raise ValueError("The canonical site URL must end with a slash.")
    required = {"index.html", "sitemap.xml", "assets/showcase.css"}
    if required - files.keys():
        raise ValueError("Required public outputs are missing.")
    for name, data in files.items():
        if not public_name(name) or not data:
            raise ValueError(f"Invalid public file: {name}")
        if name.endswith((".html", ".css", ".xml", ".txt", ".svg")) and SECRET_PATTERN.search(data):
            raise ValueError(f"Potential secret in {name}; review locally.")
    page = Page()
    page.feed(files["index.html"].decode("utf-8"))
    page.close()
    if page.canonical != [url] or page.h1 != 1 or not page.title or not page.lang:
        raise ValueError("Homepage canonical, title, language or heading is invalid.")
    for key in ("description", "og:title", "og:description"):
        if not page.meta.get(key):
            raise ValueError(f"Missing metadata: {key}")
    if page.meta.get("og:url") != url:
        raise ValueError("Open Graph URL and canonical disagree.")
    if "noindex" in (page.meta.get("robots") or "").lower():
        raise ValueError("An indexable site cannot have a noindex directive.")
    for tag, attr, link in page.links + [
        ("meta", "src", page.meta[key]) for key in ("og:image", "twitter:image") if page.meta.get(key)
    ]:
        if link.startswith("//"):
            raise ValueError("Protocol-relative links are outside the static starter contract.")
        resolved = urlsplit(urljoin(url, link))
        if resolved.scheme not in {"https", "mailto"} or resolved.username or resolved.password:
            raise ValueError("Invalid public link scheme or credentials.")
        if resolved.netloc != base.netloc:
            if attr != "href" or tag != "a":
                raise ValueError("Public assets must be local to the showcase.")
            continue
        if not resolved.path.startswith(base.path):
            raise ValueError("A same-origin link escapes the site base path.")
        relative = resolved.path[len(base.path):] or "index.html"
        if relative not in files:
            raise ValueError(f"Missing local reference: {relative}")
        if relative == "index.html" and resolved.fragment and resolved.fragment not in page.ids:
            raise ValueError(f"Missing fragment: {resolved.fragment}")
    for schema in page.json_ld:
        if (not isinstance(schema, dict) or schema.get("@context") != "https://schema.org"
                or schema.get("url") != url or not schema.get("name") or not schema.get("@type")):
            raise ValueError("JSON-LD does not match the canonical homepage.")
    sitemap = ElementTree.fromstring(files["sitemap.xml"])
    if sitemap.tag != f"{{{SITEMAP_NS}}}urlset" or [
        entry.text for entry in sitemap.findall(f"{{{SITEMAP_NS}}}url/{{{SITEMAP_NS}}}loc")
    ] != [url]:
        raise ValueError("Sitemap canonical mismatch.")
    if "robots.txt" in files and (
        base.path != "/" or f"Sitemap: {url}sitemap.xml" not in files["robots.txt"].decode()
    ):
        raise ValueError("robots.txt must be at the origin root and reference the sitemap.")
    if "llms.txt" in files and f"]({url})" not in files["llms.txt"].decode():
        raise ValueError("llms.txt must link to the canonical homepage.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--stage", type=Path, help="Create a fresh artifact directory after validation.")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads(safe_path(root, PUBLIC_MANIFEST).read_text(encoding="utf-8"))
    files = {}
    for name, expected in manifest["files"].items():
        if not public_name(name):
            raise ValueError(f"Unapproved public path: {name}")
        data = safe_path(root, f"docs/{name}").read_bytes()
        if sha(data) != expected:
            raise ValueError(f"Public content differs from reviewed manifest: {name}")
        files[name] = data
    check_site(manifest["url"], files)
    if args.stage:
        args.stage.mkdir()
        for name, data in sorted(files.items()):
            target = safe_path(args.stage, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    print(f"Validated {len(files)} public files.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError, ElementTree.ParseError) as error:
        sys.exit(f"Validation failed: {error}")
