# Agent Instructions

## Alpha Operating System (cross-project guidance)

For Alpha-related work, use the repository-local skill at `.agents/skills/alpha-operating-system/SKILL.md` (invoke `$alpha-operating-system` when skill discovery is available). Apply its outcome-first, narrow-scope, AI-native execution, evidence, measured network-effects and sustainable-speed principles. For simple bug fixes, keep the response and implementation concise; for substantial strategy or architecture work, identify customer/owner, metrics, safe experiment, explicit non-goals and tradeoffs.

**Precedence:** This is supplemental operating guidance. Existing repository-specific product, design, security, data, testing, approval and release contracts take precedence, especially for governance evidence, tenant privacy, independent ratings and production actions. Do not override the repository's established tools, workflows or human-approval gates. The CFO/IR commercial wedge is a testable company hypothesis, not a mandate for this repository.

## Repository-specific contribution guide

This repository is the Mintlify documentation site: MDX pages, `docs.json`, and
static images. It does not own the platform backend or its deployment configuration.
Keep API examples and methodology claims grounded in the owning implementation;
do not imply that a documented endpoint, rating or integration is deployed.

- Edit navigation in `docs.json` alongside the referenced `.mdx` pages.
- Preserve `LUCIDE_PROVENANCE.json`, `NAVIGATION_PROVENANCE.json`, and their
  pinned assets; `scripts/check_docs.py` checks hashes as well as page existence.
- Run `python3 scripts/check_docs.py` (Python 3.12 in CI) and `git diff --check`.
  There is no repository npm install or application test script to invent.
- `.github/workflows/ci.yml` validates documentation; `security.yml` scans source
  and secrets. A passing source check is not proof of hosted Mintlify rendering.
- Preview affected pages and check links, code samples, keyboard access and mobile
  layout when changing presentation. Publishing the hosted site needs approval.
- Never include credentials, customer records, privileged material or private
  Council/Eval evidence in public examples. Use explicitly synthetic examples.
