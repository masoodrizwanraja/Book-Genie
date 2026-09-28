# Book Genie

Book Genie is an early foundation for a reusable, author-directed book creation workflow. It organizes a book brief, outline, chapter drafts, source notes, and review decisions so that a long manuscript can be developed one chapter at a time. It does **not** generate prose yet. The first working slice creates and checks a local project; generation, research, editing, and export are planned extensions.

The design supports substantial nonfiction and narrative projects with coherent chapters, supporting sources, and author review. No private manuscript content is embedded in the product or public examples.

## What works today

- `init` creates a project with a brief, ordered outline, chapter draft files, source notes, and a review log.
- `check` validates the project schema, chapter ordering, file presence, and unique chapter identifiers.
- All book material remains in readable Markdown and JSON files that an author can edit and version.

## Repository map

| Path | Purpose |
| --- | --- |
| `src/book_genie/` | Small dependency-free CLI and project schema validation |
| `docs/architecture.md` | Workflow, boundaries, future components and design decisions |
| `docs/assumptions.md` | Current assumptions and open decisions |
| `docs/mvp-backlog.md` | Prioritized, testable MVP work |
| `examples/` | Safe example brief for local exploration |
| `tests/` | Tests for the working project lifecycle |

## Development setup

Requires Python 3.11+; no API key, external service, or database is needed for the current slice.

```bash
git clone https://github.com/masoodrizwanraja/Book-Genie.git
cd Book-Genie
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
python -m unittest discover -s tests -v
book-genie init ./my-book --title "My Book" --author "My Name"
book-genie check ./my-book
```

An installed package is optional: `PYTHONPATH=src python -m book_genie init ./my-book --title "My Book"` works too. `init` refuses to overwrite an existing directory. Keep private manuscripts and source documents outside the repository. Review the example at `examples/brief.example.md` for questions to answer before drafting.

## Project files

`book.json` records schema version, title, author, and an ordered list of chapters. `brief.md` defines audience, promise, voice, scope, and constraints. `chapters/NN-slug.md` holds author-editable drafts. `sources.md` tracks claims and source details; `reviews.md` logs author decisions and approvals. Project creation includes one placeholder chapter, which should be renamed and expanded in the outline before writing.

**Status:** foundation only. There is no AI integration, source verification, collaboration, PDF/EPUB output, or publishing workflow. Never treat generated text or citations as verified without human review. See [architecture](docs/architecture.md), [assumptions](docs/assumptions.md), and [MVP backlog](docs/mvp-backlog.md).
