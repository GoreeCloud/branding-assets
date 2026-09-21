# GoreeCloud Branding Assets

Authoritative source-control repository for current GoreeCloud branding assets, including approved logos, icons, artwork, wallpapers, wordmarks, platform marks, product marks, system identities, service identities, and approved production derivatives.

## Repository policy

- This repository is the canonical source for all current GoreeCloud branding assets.
- GoreeCloud applications, websites, documentation, repositories, and services must identify approved assets from this repository as their branding source of truth.
- Product-, system-, or service-local copies may exist only when required for packaging, deployment, public-site generation, offline use, performance, or platform integration; they are synchronized derivatives rather than independent authorities.
- New logos, icons, artwork, wordmarks, and identity-system assets originate here through controlled review before becoming production authority.
- All GoreeCloud-themed wallpapers belong in this repository. Wallpaper artwork must be high-quality and production-ready, with 4K output preferred whenever practical and approved form-factor variants provided for phones, televisions, desktops, tablets, and other supported displays as needed.
- Rejected, superseded, retired, obsolete, duplicate, or abandoned logo/icon/artwork files must not be retained in the current authoritative repository tree or in consumer repositories as historical asset collections.
- Review candidates may exist only as temporary working revisions or short-lived review branches. Once a decision is complete, unapproved or superseded artwork is removed from the current tree rather than archived as branding assets.
- Historical traceability belongs in Git revision history and chronological change records under GoreeCloud revision-control requirements; history must not be recreated as `concepts/`, `legacy/`, `archive/`, `retired/`, `old/`, or similar artwork collections on the current authoritative branch.
- Branding never creates technical authority or evidence for privacy, security, continuity, design conformance, coordination, or application capability claims.

## Current platform identity

**Official platform symbol:** Unified Clean — Blue  
**Canonical vector source:** `official/goreecloud-logo.svg`  
**Design language:** Glaze UI  
**Platform:** GoreeCloud

The canonical SVG is the source of truth for the GoreeCloud platform mark. Raster icons, favicons, launcher artwork, social avatars, and other production derivatives must be generated from approved vector sources rather than independently redrawn.

## Repository structure

- `official/` — approved GoreeCloud parent-platform identity artwork and derivatives.
- `products/` — canonical GoreeCloud application and product identity artwork.
- `systems/` — canonical platform-system branding for Privacy Shield, Wardveil Security, Everkeep, Glaze UI, and GoreeCloud Mesh.
- `services/` — canonical service-identity namespace and machine-readable service registry. Approved service vectors use `services/<service-id>/service-icon.svg`.
- `wallpapers/` — canonical GoreeCloud-themed wallpaper namespace and form-factor guidance; see `wallpapers/README.md`.
- `catalog.json` — machine-readable registry of the canonical platform, product, and platform-system branding authority.
- `services/catalog.json` — authoritative machine-readable registry for service identities, parent derivation, lifecycle state, and consumer surfaces.
- `BRAND.md` — platform identity meaning, usage, geometry, color, and brand rules.
- `WORDMARK.md` — GoreeCloud wordmark specification and construction guidance.
- `PRODUCTION-ASSETS.md` — production export matrix and regeneration requirements.
- `MIGRATION.md` — completed repository consolidation, audit, and legacy-repository deletion record.
- `tools/` — asset-generation and validation tooling.

Product, system, service, campaign, and experience-specific current assets should be organized inside this repository rather than split into separate branding repositories.

## Platform-system identities

The following are substantive GoreeCloud platform systems, not decorative labels:

- **Privacy Shield → Privacy Center** — platform-wide privacy identity and privacy-control authority.
- **Wardveil Security → Security Center** — platform-wide security and protection identity.
- **Everkeep → Continuity Center** — resilience, backup/recovery, preservation, portability, succession, and digital-legacy identity.
- **Glaze UI → Design Center** — GoreeCloud visual, interaction, adaptation, and interface-design system.
- **GoreeCloud Mesh → Mesh Center** — application/service coordination and governance plane.

Approved system artwork is indexed in `systems/README.md`. GoreeCloud Mesh uses the approved **Interlace** identity at `systems/goreecloud-mesh/goreecloud-mesh-mark.svg`.

## Service identities

Service identities are reduced derivatives of an approved parent product or platform-system identity. They are not independent mini-brands and must remain distinguishable from the full parent application/system artwork.

`services/catalog.json` may register a known service as `artwork-pending` without claiming an asset. Pending records must keep `canonical_asset` and `git_blob` null and must not place a canonical-looking SVG at the reserved production path. Approved services use `services/<service-id>/service-icon.svg` and pin the exact accepted Git blob.

Operational state remains separate from the stable service mark. A service icon must not itself imply healthy, connected, authorized, secure, protected, synchronized, or otherwise accepted runtime state.

See `services/README.md` for the full service identity contract.

## Integration contract

Consumers must reference this repository as `GoreeCloud/branding-assets` for branding provenance. The former `GoreeCloud/goreecloud-logo` repository was deleted after migration and a zero-active-reference audit; it must not be recreated or referenced as a current branding source.

`catalog.json` is the machine-readable discovery entry point for canonical GoreeCloud platform, product, and platform-system branding paths. `services/catalog.json` is the corresponding authoritative discovery entry point for service identities. Consumer-specific documentation may retain additional local build paths, but it must not redefine canonical branding authority.

When an asset is vendored into another repository, its documentation or machine-readable identity contract should record the canonical path here. Vendored bytes must stay synchronized with the approved source. When canonical artwork is replaced, the superseded consumer copy must be replaced or removed rather than retained beside the current derivative.

## Governance

Approved production assets must be source-traceable and evidence-backed. Public artwork and language must not imply capabilities that are not implemented or accepted for the represented scope.

Branding CI validates both the root catalog and the service registry. Service validation also checks parent identity existence and pinning, lifecycle truth, canonical path discipline, parent-icon non-reuse, consumer mappings, and orphan service SVGs.

See `catalog.json`, `services/catalog.json`, `BRAND.md`, `WORDMARK.md`, `PRODUCTION-ASSETS.md`, `wallpapers/README.md`, `products/README.md`, `systems/README.md`, and `services/README.md` before integrating, modifying, or exporting GoreeCloud identity artwork.
