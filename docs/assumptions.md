# Assumptions and decisions to keep flexible

| Topic | Working assumption | Why it can change |
| --- | --- | --- |
| Product purpose | Reusable, author-directed long-form book workflow | Exact positioning and target customers have not been specified |
| Initial workflow | One author and one book in a local project directory | A team workflow may require shared storage and roles |
| Example genres | Structured nonfiction and narrative memoir | Actual launch genre and templates require validation |
| Technology | Python 3.11+ standard library for the first CLI slice | Frontend, model, storage, and deployment are undecided |
| Source handling | Sources and sensitive claims require human verification | Citation format and licensed content policy need decisions |
| Generated content | Future AI output is a draft requiring author review | Provider and editorial process are undecided |
| Export | Manuscript exports are expected later | Which of DOCX, PDF, EPUB or other formats comes first is open |
| Existing manuscripts | Private works may inform workflow needs | Their content and chapter structures require explicit permission before use as repository examples |

## Decisions before a hosted or AI-enabled MVP

- Who is the first author persona, and which genre is the initial launch focus?
- What book data may be sent to an AI provider, and what retention/deletion rules apply?
- What is the review threshold for sources, copyrighted quotations, sensitive personal stories, and health or religious claims?
- Which output format and handoff process should the first launch support?

These are product decisions, not blockers to the local scaffold. No one has approved a particular provider, pricing model, or publishing commitment.
