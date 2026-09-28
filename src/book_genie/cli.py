"""Minimal local project creation and structural validation."""

import argparse
import json
from pathlib import Path

SCHEMA_VERSION = 1


def init_project(path: Path, title: str, author: str = "") -> None:
    if path.exists():
        raise ValueError(f"Refusing to overwrite existing path: {path}")
    path.mkdir(parents=True)
    (path / "chapters").mkdir()
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "title": title.strip(),
        "author": author.strip(),
        "chapters": [{"id": "chapter-01", "number": 1, "title": "Untitled chapter", "file": "chapters/01-untitled.md"}],
    }
    (path / "book.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (path / "brief.md").write_text(f"# {title.strip()} — book brief\n\n- Audience:\n- Reader promise:\n- Voice:\n- Scope and exclusions:\n- Length target:\n- Approval owner:\n", encoding="utf-8")
    (path / "chapters" / "01-untitled.md").write_text("# Untitled chapter\n\n## Goal\n\n## Draft\n\n", encoding="utf-8")
    (path / "sources.md").write_text("# Sources and claims\n\nRecord sources, locations, claims, and verification status here.\n", encoding="utf-8")
    (path / "reviews.md").write_text("# Review decisions\n\nRecord chapter, reviewer, date, requested change, and approval here.\n", encoding="utf-8")


def check_project(path: Path) -> list[str]:
    errors = []
    manifest_path = path / "book.json"
    if not manifest_path.is_file():
        return ["Missing book.json"]
    try:
        book = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"Cannot read book.json: {exc}"]
    if not isinstance(book, dict):
        return ["book.json must contain an object"]
    if book.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"Expected schema_version {SCHEMA_VERSION}")
    if not isinstance(book.get("title"), str) or not book["title"].strip():
        errors.append("Book title is required")
    for filename in ("brief.md", "sources.md", "reviews.md"):
        if not (path / filename).is_file():
            errors.append(f"Missing {filename}")
    chapters = book.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        return errors + ["chapters must be a nonempty list"]
    seen_ids = set()
    seen_files = set()
    for index, chapter in enumerate(chapters, start=1):
        if not isinstance(chapter, dict):
            errors.append(f"Chapter {index} must be an object")
            continue
        ident = chapter.get("id")
        if not isinstance(ident, str) or not ident.strip() or ident in seen_ids:
            errors.append(f"Chapter {index} has missing or duplicate id")
        else:
            seen_ids.add(ident)
        if type(chapter.get("number")) is not int or chapter["number"] != index:
            errors.append(f"Chapter {index} number must be {index}")
        if not isinstance(chapter.get("title"), str) or not chapter["title"].strip():
            errors.append(f"Chapter {index} title is required")
        filename = chapter.get("file")
        if not isinstance(filename, str) or not filename:
            errors.append(f"Chapter {index} file is required")
            continue
        relative = Path(filename)
        if relative.is_absolute() or ".." in relative.parts or len(relative.parts) != 2 or relative.parts[0] != "chapters" or relative.suffix != ".md":
            errors.append(f"Chapter {index} file must be a Markdown path under chapters/")
        elif filename in seen_files:
            errors.append(f"Chapter {index} file is duplicated")
        elif not (path / relative).is_file():
            errors.append(f"Missing chapter file: {filename}")
        seen_files.add(filename)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="book-genie", description="Local book project tools")
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("init", help="Create a new local book project")
    create.add_argument("path", type=Path)
    create.add_argument("--title", required=True)
    create.add_argument("--author", default="")
    check = commands.add_parser("check", help="Check project file structure")
    check.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    if args.command == "init":
        if not args.title.strip():
            parser.error("--title cannot be blank")
        try:
            init_project(args.path, args.title, args.author)
        except (OSError, ValueError) as exc:
            parser.exit(1, f"Error: {exc}\n")
        print(f"Created {args.path}")
        return 0
    errors = check_project(args.path)
    if errors:
        for error in errors:
            print(f"Error: {error}")
        return 1
    print(f"Project structure is valid: {args.path}")
    return 0
