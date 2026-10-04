# Alpha documentation Geist rollout

This site is the Mintlify-hosted `docs.alpha.ac`, owned by `wolfepereira/docs`. Keep its existing navigation and approved MDX content. `alpha-tokens.css` and the licensed Geist Sans/Mono assets are SHA-256-pinned projections of platform `@alpha/design-system` 1.0.0. Mintlify owns the search, navigation and interactive API components; `custom.css` adapts their type, code, controls and focus without introducing a second framework. Pixel and Tiempos are deliberately absent from reference documentation.

Mintlify's root CSS integration is documented at https://www.mintlify.com/docs/customize/custom-scripts. Brand bases remain exact in the shared tokens. Configuration uses the darker semantic blue for readable links; light appearance accents use its dark contrast-tested counterpart. Provider-generated widgets still need rendered preview verification.

Run `python3 scripts/check_docs.py`. Promote through the repository's normal Mintlify integration, inspect the resulting preview and production deployment, and retain the prior provider version for rollback. A passing JSON/navigation check is not production or visual proof. Never use this redesign to silently revise methodology or rating definitions.

The previously missing `/images` logo/favicon references now resolve to canonical Alpha brand assets from the public website registry. These are the existing approved logo files, not new artwork.

Local Mintlify 4.2.984 preview verified the glossary with loaded logos, Geist UI and no horizontal overflow at 390px. The CLI generates a local docs.json compatibility projection; mint.json remains the repository configuration. Production deployment is not yet verified.
