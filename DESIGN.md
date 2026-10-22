# Tareeq design system

Tareeq (طريق, "road" or "way") is a hands-free Arabic learning app. Full visual reference: open `styleguide.html`.

## Files
- `css/tokens.css`: colour, type, spacing, radius, motion tokens (light + dark). Edit here first.
- `css/base.css`: base styles and components (buttons, phrase card, chips, progress, form).
- `assets/brand/`: logo mark and logo lockup (SVG). `favicon.svg` is a copy of the mark.
- `assets/fonts/`: self-hosted Fraunces, Instrument Sans, Cairo (Arabic) woff2 files (all SIL OFL).
- `social/`: HTML sources for `og-image.png` (1200×630) and `twitter-card.png` (1200×600).
- `scripts/render-images.py`: regenerates the PNG images and icons (needs Python Playwright + Chromium).

## Principles
1. Audio first. Visual UI is for when the user is parked: 56px targets, one action per screen.
2. Arabic leads. Arabic is larger than Latin text beside it, always `lang="ar" dir="rtl"`, line-height 1.7.
3. Road metaphor. Olive and asphalt with a dashed saffron centre line (`.roadline`). Rounded shapes.
4. Accessible. All text pairs meet WCAG AA. Saffron is never text on cream.
5. Dark mode is the in-car theme and follows `prefers-color-scheme`.

## SEO
Primary keywords: learn Arabic, study Arabic language, Palestinian Arabic. Metadata is in `index.html` (title, description, canonical, Open Graph, X card, JSON-LD). Contact: contact@tareeqapp.com.
