# Prioritized MVP backlog

The current scaffold completes **P0.1**. Items below are proposed, with dependencies and acceptance criteria to keep implementation reviewable.

| Priority | Item | Acceptance criteria |
| --- | --- | --- |
| P0.1 done | Local project creation and structural validation | `init` creates a readable project; `check` rejects missing files, duplicate IDs, or invalid ordering; tests pass |
| P0.2 | Author intake and outline editing | Capture audience, promise, voice, scope, length target, exclusions; add/reorder chapters without losing drafts; validate revisions |
| P0.3 | Chapter plan and manual drafting | Each chapter has a goal, section plan, status, and editable draft; progress is visible |
| P0.4 | Source and claim register | Record source identity, location, claim, verification state, and chapter link; unresolved claims are visible |
| P0.5 | Human review and revision loop | Comments and requested edits map to chapters; only the author marks content approved; edits retain history |
| P1.1 | Bounded AI drafting pilot | A replaceable provider adapter drafts one section from explicit context; log inputs, outputs, model, and costs; author accepts or rejects |
| P1.2 | Manuscript consistency checks | Flag missing sections, repeated material, name/term discrepancies, and unsupported claims for review |
| P1.3 | First export | Compile approved chapters in order into the chosen format; verify headings, tables, and source notes |
| P2 | Templates and collaboration | Genre templates and shared review once a pilot demonstrates the need |

## Suggested first pilot

Use a non-sensitive sample project to exercise intake → outline → one chapter → evidence → review → export. Test a real manuscript only after privacy, source permissions, and author approval rules are defined. Avoid making page count or chapter count a universal product constraint.
