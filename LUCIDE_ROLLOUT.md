# Lucide documentation migration

Official Mintlify CLI converted mint.json to docs.json; navigation pages, logos, CTA, colors and social links are preserved. Select the supported Lucide provider library and map five legacy Font Awesome names to Lucide equivalents. All 15 authored Card icon uses have valid Lucide names. Alpha custom CSS sets 1.75 stroke where the provider emits inline Lucide SVG.

Mintlify controls its internal shell and icon runtime version. This provider adapter cannot claim the exact React pin used in platform applications. Social logos remain provider-owned brand marks. No content, evidence, authority or access scope changes. Deploy branch is wolfepereira/docs main; verify actual rendered card icons and navigation after normal CI/merge.

Authored card icons use local SVG assets generated from the shared registry at Lucide 1.50.0,24px and1.75 stroke, with upstream license and per-file hashes. This removes the provider CDN version dependency for owned cards; the Lucide provider setting still governs its shell. Regenerate through `packages/design-system/scripts/project-docs.mjs` in alpha-platform.
