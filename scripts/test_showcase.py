"""Offline smoke tests for generated artifacts and refresh state."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from showcase import FACTS, PACKAGE, PROFILES, STATE, WORKFLOW
from validate import PUBLIC_MANIFEST


class CommitHeaderTest(unittest.TestCase):
    def test_conventional_headers(self):
        script = PACKAGE / "scripts/check_commit_header.py"
        cases = {
            "fix: check public files": True,
            "feat(generator)!: add a required field": True,
            "fix: document migration\n\nBREAKING CHANGE: rename the field": True,
            "feat: ": False,
            "feat(scope) : bad separator": False,
            "Update the generator": False,
        }
        for message, valid in cases.items():
            with self.subTest(message=message):
                result = subprocess.run(
                    [sys.executable, str(script)], input=message,
                    text=True, capture_output=True,
                )
                self.assertEqual(result.returncode, 0 if valid else 1, result.stderr)


class InstallerTest(unittest.TestCase):
    def test_installs_only_skill_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            home = root / "home"
            source.mkdir()
            home.mkdir()
            brand_files = (
                "agents/openai.yaml",
                "docs/assets/oss-showcase-lockup.svg",
                "docs/assets/otto-s.svg",
                "docs/assets/otto-s-favicon.svg",
            )
            for name in ("README.md", "SKILL.md", *brand_files):
                destination = source / name
                destination.parent.mkdir(exist_ok=True, parents=True)
                shutil.copyfile(PACKAGE / name, destination)
            for name in ("references", "scripts", "templates"):
                shutil.copytree(PACKAGE / name, source / name)
            (source / ".git").mkdir()
            (source / ".git/config").write_text("fixture")
            (source / ".env").write_text("fixture")
            (source / "templates/.env.local").write_text("fixture")
            command = ["sh", str(source / "scripts/install.sh")]
            env = {**os.environ, "HOME": str(home)}
            installed = home / ".agents/skills/oss-showcase"

            linked = source / "references/linked.md"
            linked.symlink_to(source / ".env")
            rejected = subprocess.run(command, env=env, capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("Expected a regular skill file", rejected.stderr)
            self.assertFalse(installed.exists())
            linked.unlink()

            subprocess.run(command, env=env, check=True, capture_output=True)
            subprocess.run(command, env=env, check=True, capture_output=True)
            self.assertEqual((home / ".claude/skills/oss-showcase").resolve(), installed.resolve())
            for name in brand_files:
                self.assertEqual((installed / name).read_bytes(), (PACKAGE / name).read_bytes())
            self.assertTrue((installed / "references/publishing.md").is_file())
            self.assertTrue((installed / "templates/profiles/skill.json").is_file())
            for name in (".git", ".env", "templates/.env.local"):
                self.assertFalse((installed / name).exists())
            subprocess.run(
                [sys.executable, str(installed / "scripts/showcase.py"), "--help"],
                check=True, capture_output=True,
            )


class ShowcaseTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write("example.txt", "fixture")
        self.facts = {
            "profile": "cli",
            "name": "Sample",
            "summary": "Print a fixture value.",
            "repo_url": "https://github.com/sample/tool",
            "site_url": "https://sample.github.io/tool/",
            "setup": "Use the bundled fixture.",
            "example": "cat example.txt",
            "result": "Prints fixture.",
            "evidence": {key: ["example.txt"] for key in ("summary", "setup", "example", "result")},
        }

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def command(self, *args, ok=True, script=None):
        path = script or PACKAGE / "scripts/showcase.py"
        result = subprocess.run(
            [sys.executable, str(path), "--root", str(self.root), *args],
            text=True, capture_output=True, cwd=self.root,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def store_facts(self):
        self.write(FACTS, json.dumps(self.facts))

    def validate(self, *args, ok=True):
        return self.command(*args, ok=ok, script=self.root / ".agents/showcase/validate.py")

    def test_profiles_and_idempotence(self):
        for profile in sorted(PROFILES):
            with self.subTest(profile=profile):
                self.facts["profile"] = profile
                self.store_facts()
                self.command("apply")
                self.validate()
                index = self.root / "docs/index.html"
                stamp = index.stat().st_mtime_ns
                self.assertIn("current docs/index.html", self.command("apply"))
                self.assertEqual(index.stat().st_mtime_ns, stamp)

    def test_project_path_root_domain_and_artifact_scope(self):
        self.write("docs/assets/demo.gif", "fixture media bytes")
        self.write("docs/assets/social.png", "fixture card bytes")
        self.write("docs/assets/logo.svg", "<svg/>")
        self.write("docs/assets/favicon.svg", "<svg/>")
        self.write("docs/internal-notes.txt", "internal test fixture")
        self.facts.update({
            "assets": {
                "logo": {"path": "assets/logo.svg"},
                "favicon": {"path": "assets/favicon.svg"},
                "demo": {"path": "assets/demo.gif", "alt": "Fixture", "caption": "The sample prints."},
                "social": {"path": "assets/social.png", "alt": "Sample project"},
            },
            "llms_txt": True,
            "schema_type": "SoftwareApplication",
        })
        self.store_facts()
        self.command("apply")
        page = (self.root / "docs/index.html").read_text()
        self.assertIn('href="assets/demo.gif"', page)
        self.assertIn('<img class="logo" src="assets/logo.svg" alt="">', page)
        self.assertIn('<link rel="icon" href="assets/favicon.svg">', page)
        self.assertIn('https://sample.github.io/tool/assets/social.png', page)
        self.assertIn('docs/assets/demo.gif', (self.root / "README.md").read_text())
        self.assertFalse((self.root / "docs/robots.txt").exists())
        self.validate("--stage", "preview")
        self.assertFalse((self.root / "preview/internal-notes.txt").exists())
        self.assertTrue((self.root / "preview/assets/logo.svg").is_file())
        self.assertTrue((self.root / "preview/assets/favicon.svg").is_file())
        workflow = self.root / WORKFLOW
        existing_workflow = workflow.read_bytes()
        self.facts.update(site_url="https://tool.example.org/", llms_txt=False)
        self.store_facts()
        self.command("apply")
        self.validate("--stage", "custom")
        self.assertTrue((self.root / "custom/robots.txt").exists())
        self.assertFalse((self.root / "custom/llms.txt").exists())
        self.assertEqual(workflow.read_bytes(), existing_workflow)
        self.command("preview", "candidate")
        self.assertIn("https://tool.example.org/", (self.root / "candidate" / WORKFLOW).read_text())
        self.write("docs/assets/demo.gif", "changed after review")
        self.assertIn("differs from reviewed manifest", self.validate(ok=False))

    def test_existing_content_and_read_only_plan(self):
        self.store_facts()
        self.write("README.md", "Manual documentation")
        self.assertIn("conflict README.md", self.command("apply", ok=False))
        self.assertFalse((self.root / PUBLIC_MANIFEST).exists())
        self.command("plan", "--keep-readme")
        self.assertFalse((self.root / STATE).exists())
        self.command("preview", "draft")
        self.assertTrue((self.root / "draft/README.md").exists())
        self.write(WORKFLOW, "Manual deployment workflow")
        self.assertIn(f"keep {WORKFLOW}", self.command("apply", "--keep-readme"))
        self.assertEqual((self.root / WORKFLOW).read_text(), "Manual deployment workflow")
        self.assertEqual((self.root / "README.md").read_text(), "Manual documentation")
        self.write("docs/index.html", "manual page changes")
        self.assertIn("conflict docs/index.html", self.command("apply", "--keep-readme", ok=False))

    def test_matching_content_does_not_grant_ownership(self):
        self.store_facts()
        self.command("preview", "draft")
        readme = self.root / "README.md"
        existing = (self.root / "draft/README.md").read_bytes()
        readme.write_bytes(existing)
        self.assertIn("current README.md", self.command("apply"))
        state_path = self.root / STATE
        state = json.loads(state_path.read_text())
        self.assertNotIn("README.md", state["generated"])

        self.facts["summary"] = "A new summary."
        self.store_facts()
        self.assertIn("conflict README.md", self.command("apply", ok=False))
        self.assertEqual(readme.read_bytes(), existing)

        self.command("apply", "--keep-readme")
        self.assertIn("A new summary.", (self.root / "docs/index.html").read_text())

        state = json.loads(state_path.read_text())
        del state["ownership_version"]
        self.write(STATE, json.dumps(state))
        page = (self.root / "docs/index.html").read_bytes()
        self.facts["summary"] = "Another summary."
        self.store_facts()
        self.assertIn("conflict docs/index.html", self.command("apply", "--keep-readme", ok=False))
        self.assertEqual((self.root / "docs/index.html").read_bytes(), page)

    def test_stage_fingerprints(self):
        self.write("docs/assets/demo.gif", "first recording")
        self.write("stages.json", json.dumps({
            "demo": {"inputs": ["example.txt"], "outputs": ["docs/assets/demo.gif"]},
        }))
        self.assertIn("unrecorded", self.command("status", "stages.json"))
        self.command("record", "stages.json", "demo")
        self.assertIn("current", self.command("status", "stages.json"))
        self.write("example.txt", "new fixture")
        self.assertIn("inputs changed", self.command("status", "stages.json"))
        self.write("example.txt", "fixture")
        (self.root / "docs/assets/demo.gif").unlink()
        self.assertIn("outputs changed", self.command("status", "stages.json"))
        self.command("record", "stages.json", "demo", ok=False)

    def test_symlink_asset_is_rejected(self):
        self.write("fixture.svg", "<svg/>")
        asset = self.root / "docs/assets/logo.svg"
        asset.parent.mkdir(parents=True)
        asset.symlink_to(self.root / "fixture.svg")
        self.facts["assets"] = {"logo": {"path": "assets/logo.svg"}}
        self.store_facts()
        self.assertIn("Symlink", self.command("apply", ok=False))
        self.assertFalse((self.root / PUBLIC_MANIFEST).exists())


if __name__ == "__main__":
    unittest.main()
