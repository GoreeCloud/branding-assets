# GoreeCloud Production Branding Assets

## Purpose

I use approved canonical GoreeCloud vector artwork as the sole source for production branding derivatives. For the parent GoreeCloud platform identity, the canonical source remains `official/goreecloud-logo.svg`; raster and platform packages are generated artifacts rather than independent masters.

Product, platform-system, and service derivatives follow the same canonical-first rule. A consumer repository may package a native copy only after the corresponding canonical source is approved and provenance is recorded.

## Production export matrix

### General PNG

I maintain square PNG exports at 16, 32, 48, 64, 128, 256, 512, 1024, and 2048 pixels as needed for interfaces, documentation, integrations, and distribution.

### Web

I maintain favicon-compatible 16, 32, and 48 pixel artwork, plus 180, 192, and 512 pixel web/application icons. A multi-size `favicon.ico` may contain the 16, 32, and 48 pixel renderings.

### Social and repository identity

I use a 1024 × 1024 canonical raster rendering for GitHub and social-avatar source artwork. Individual platforms may downsample this source. I do not redesign an approved mark for a specific social network unless an explicitly approved platform derivative requires it.

### Android

Launcher-source raster sizes are maintained for mdpi (48), hdpi (72), xhdpi (96), xxhdpi (144), and xxxhdpi (192). Application projects may derive adaptive-icon packaging from approved application artwork, but may not alter the canonical identity geometry without an approved derivative specification.

Service artwork used inside Android applications is generated from the approved canonical service SVG. It must not fall back to the full parent application/system icon or a generic placeholder after the service identity has been approved.

### Apple platforms

I maintain source raster sizes including 120, 152, 167, 180, and 1024 pixels for appropriate application-icon workflows. Platform-specific packaging must follow current platform requirements while preserving the approved GoreeCloud artwork.

### Wallpapers

All GoreeCloud-themed wallpapers must be stored in `GoreeCloud/branding-assets`, with canonical wallpaper files organized under `wallpapers/`.

Wallpaper exports must be high-quality and production-ready. 4K resolution is preferred whenever practical. Lower-resolution or device-specific derivatives may be supplied where compatibility, performance, packaging, or presentation requirements justify them.

Wallpaper coverage must support relevant display classes, including phones, televisions, desktop computers, tablets, laptops, ultrawide displays, foldable devices, and other current or future GoreeCloud-supported surfaces. When one composition cannot crop safely across form factors, provide approved portrait, landscape, square or near-square, television, desktop, tablet, or other aspect-ratio variants as needed.

All wallpaper derivatives must remain traceable to the approved source and must not be independently redesigned in consumer repositories.

## Service identity production rule

The canonical service identity registry is `services/catalog.json`.

Known services may be registered as `artwork-pending` before artwork exists. That state deliberately has no production source: `canonical_asset` and `git_blob` remain null, and the reserved `services/<service-id>/service-icon.svg` path must not exist.

After visual and semantic approval, a service is promoted to `approved` only when:

- the canonical source exists at `services/<service-id>/service-icon.svg`;
- the exact Git blob is pinned in `services/catalog.json`;
- the mark is a reduced derivative of its registered parent Identity DNA rather than a direct copy of the full parent icon;
- small-size, grayscale, supported appearance, contrast, and accessibility review is complete for its intended surfaces;
- consumer derivatives remain traceable to the canonical source;
- operational state is conveyed separately from the stable identity;
- the applicable project/change records document the migration and evidence.

Service artwork never implies successful authentication, authorization, privacy consent, security, health, connectivity, synchronization, continuity, or other runtime acceptance.

## Generation rule

All raster and platform assets must be regenerated from the approved SVG when the canonical artwork changes. I do not manually edit exported PNG files and then treat those edits as official artwork.

## Validation

Before release, I visually inspect small exports to confirm that defining geometry and negative-space relationships remain distinct. I also verify square dimensions, alpha/background expectations, file integrity, and that no export has been stretched or cropped.

Automated branding CI validates the root canonical catalog and the service identity registry. Automated source validation does not replace human visual acceptance; it proves path, provenance, parent, lifecycle, and registry integrity only.

## Repository policy

`GoreeCloud/branding-assets` is the authoritative Git home for approved branding vector sources and identity documentation. Binary production packages may be distributed as release artifacts or checked in where operationally useful, but they remain derivatives of canonical sources stored here.
