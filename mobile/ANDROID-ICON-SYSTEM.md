# GoreeCloud Android Icon System

Status: Required redesign
Target: GoreeCloud first-party Android applications
Design system: Glaze UI

## Problem statement

Physical-device acceptance on the current GoreeCloud Android builds showed that first-party app icons do not read as one coherent platform. Current icons vary too much in background treatment, visual weight, detail, geometry, and palette.

## Direction

The replacement icon family must be unmistakably GoreeCloud while remaining legible at Android launcher sizes.

### Shared construction

- Adaptive icons are required.
- Use one common safe-area and optical-size system across all first-party apps.
- Prefer simple, bold product glyphs over miniature illustrations.
- Avoid excessive internal detail that disappears below 48dp.
- Use neutral Glaze material backgrounds with restrained GoreeCloud accent color.
- Maintain consistent corner/silhouette behavior through Android adaptive-icon masks rather than drawing arbitrary circles into every foreground.
- Monochrome/themed-icon resources are required for supported Android versions.
- Product identity must remain distinguishable without using text inside icons.

### Family behavior

The icon family should feel related through:

- common stroke and corner language;
- consistent optical weight;
- shared neutral-material backgrounds;
- a restrained accent palette;
- consistent light-source/depth treatment;
- unified foreground safe-area sizing.

Products must still have distinct glyphs. Do not make every application the same GoreeCloud logo with a different color.

## Initial Android set

Priority redesign targets:

- GoreeCloud App Store
- GoreeCloud Launcher
- GoreeCloud Browser
- GoreeCloud Gallery
- GoreeCloud Keyboard
- GoreeCloud Messenger when the Android client exists
- GoreeCloud Memos

## Product glyph guidance

- **App Store:** storefront/package/download motif; avoid generic Android mascot imagery.
- **Launcher:** home/workspace/constellation motif; must not look like the Android robot.
- **Browser:** clearly communicates browser/web/navigation at a glance; a browser-window, compass/navigation, or globe-derived glyph may be used if it remains original and GoreeCloud-specific.
- **Gallery:** photo/media motif with simplified landscape/frame geometry.
- **Keyboard:** keyboard/input motif with clear key geometry.
- **Messenger:** conversation/message motif when the Android app exists.
- **Memos:** note/document motif.

## Asset authority

Approved master SVG/vector assets and Android-ready adaptive-icon foreground/background derivatives belong in `GoreeCloud/branding-assets`. Product repositories consume or synchronize approved assets and must not become independent branding authorities.

## Acceptance

A new icon is not accepted based on source-vector appearance alone. Validate on a physical Android device in:

- home screen;
- app drawer;
- light wallpaper;
- dark wallpaper;
- themed/monochrome icon mode where supported;
- small icon contexts such as Settings/app info where applicable.

The family must be reviewed side-by-side, because cross-product consistency is part of the acceptance criteria.
