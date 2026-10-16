# GC UI — Official Product Identity v1.0

GC UI is GoreeCloud's independent, cross-platform user-interface design language. These are its **own** canonical product identity assets; they do not replace or adapt the official GoreeCloud platform symbol or Glaze UI's separate Design Center identity.

## Official vector masters
- `app-icon.svg` — canonical squared app icon (midnight navy field; blue/cyan symbol); source of all app launcher, browser, social and repository raster icons.
- `gc-ui-symbol.svg` — canonical transparent letterform monogram for surfaces that do not need an icon tile.
- `gc-ui-logo.svg` — horizontal full-color symbol + outlined GC UI wordmark for light fields.
- `gc-ui-logo-dark.svg` — same outlined wordmark geometry with reversed lettering for dark fields.
- `app-icon-monochrome.svg` — approved one-ink icon derivative.
- `gc-ui-symbol-monochrome.svg` — approved one-ink symbol derivative; `currentColor` can supply its foreground.

**Canonical priority:** Vector sources above are authoritative. PNG exports must be generated from these masters, never hand-redrawn independently. The outlined wordmark has no font dependency at display time; its letterform paths were constructed from Inter Display SemiBold (font bytes are not stored or distributed). Don't substitute the parent GoreeCloud emblem.

## Visual construction
**Meaning:** The G and C are two rounded, adjacent open ribbons. Their aligned baseline describes consistency; their separate openings describe freedom and flexible cross-platform adaptation. They deliberately avoid Glaze UI's angular overlapping facet symbol.

- **Iris-blue ribbon:** #5C8BFF → #6564FF → #8369F5.
- **Cyan ribbon:** #42E0D1 → #44C9F5 → #8F85FF.
- **Icon field:** midnight navy from #101C3B through #0D1730 to #090F24.
- **Light wordmark:** GC #15213A; UI #6456EE.
- **Reversed wordmark:** GC #F8FAFF; UI #AFA4FF.
- **Geometry:** 512-square nominal icon/symbol; two 46-unit round-capped and round-joined ribbons. Rounded-square icon field has 116-unit corner radius and an 8-unit outer offset.

The mark is intentionally geometric at small sizes; do not add glass gloss, glow, bevels, shadows, a rainbow texture, or platform branding into the official vectors. Interfaces may surround it with GC UI materials, but the identity paths themselves remain stable.

## Usage
- **App launcher/social avatar/favicon:** app-icon, not the full horizontal logo.
- **Wide headers, splash screens, document cover:** full horizontal logo, correct light/dark version.
- **Compact nav/system badges:** transparent symbol when a platform does not require the colored icon tile.
- **One-ink/forced-colors contexts:** monochrome symbol or monochrome app icon; do not recolor the blue/cyan masters arbitrarily.
- Preserve aspect ratio and leave at least half a stroke-width of visual clearance around the mark; use a larger margin for lockups.
- Small size check: icon should remain legible at 16/32/48 px; never substitute the full wordmark at favicon size.
- Text alternatives: `GC UI` (symbol/icon) and `GC UI logo` (full lockup) when identity is informational. Decorative uses should be hidden from assistive technology when adjacent text already names it.

## Approval and traceability
This v1.0 identity was created at the explicit request of the GC UI owner, using one-time authorization to write to this repository. `catalog.json` pins the canonical product icon, the monochrome variant and additional identity sources by Git blob SHA. New derivatives should be synchronized here before changes reach consumers.

Raster build, size review and acceptance evidence must not be confused with application accessibility certification. If the owner selects a future revision, replace the current canonical master and regenerate derivatives rather than keeping competing current marks in the authoritative tree.
