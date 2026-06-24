# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The HTML slide deck for the **CUNY AI Lab panel at ACH 2026** (Fri June 26, 2026):
"Building Community-Oriented Infrastructures for AI Experimentation." 41 slides for
five presenters. It is **based on the `cuny-ai-lab/cali-narst` theme**
(https://cuny-ai-lab.github.io/cali-narst/) — a custom dark deck, not reveal.js.
This folder is its own git repo (branch `main`).

`SLIDES.md` is the manifest and **source of truth for slide content** (per-presenter
sections, the Zach figure→slide map, Azucena/Steve sources, and Zach's spoken
talk track). Edit `SLIDES.md` and `index.html` together.

## Files

- `index.html` — the deck. Each slide is one `<section class="slide" data-slide="…">`.
- `src/styles.css`, `src/slides.js` — **the cali-narst theme, verbatim. Do not edit.**
  Put all panel-specific CSS in `src/ach-accents.css` instead.
- `src/ach-accents.css` — our additions: presenter accents, the `figure-hero`
  layout, the `walk-step` image walkthrough, the emblem (`.brand-mark`), and the
  `step-grid` rules imported verbatim from cali-brooklyn (for Luke's Intervention
  slide; not part of the vendored cali-narst theme).
- `images/` — figures (copied from `../figures/`), Sandbox screenshots, the
  `zm-step*` walkthrough shots, the `ach26.svg` emblem, and logos.

## How the deck works (theme behavior)

- `slides.js` auto-paginates every `section.slide` and drives nav (arrow keys /
  space / footer scrubber / `btn-prev`·`btn-next`), the lightbox, and fragments.
  The footer **counter** ("18 / 44") is set from `slides.length` — don't
  hand-edit it. The scrubber's **`max` attribute is NOT** — it's hardcoded on
  `<input id="slide-scrubber" … max="44">` in `index.html`; bump it whenever you
  add/remove a slide or the scrubber stops short.
- **Fragments:** any element with class `frag` is hidden until revealed; each
  click/Right-arrow reveals the next `.frag`, then advances to the next slide.
- **Accents are CSS, keyed by `data-slide` prefix** (`matt-`, `luke-`, `zach-`,
  `azu-`, `steve-`) — see `ach-accents.css`. Keep the prefixes or colors/overview
  break.

## Slide layouts (class on the `<section>`)

- `slide-title` — title slide (animated WebGL background + title card).
- `placeholder-slide even-layout` / `odd-layout` — text column + figure stage.
- `placeholder-slide crowded` — text-only (stage hidden); used by Azucena/Steve.
- `placeholder-slide figure-hero` — **minimal title line on top, the image
  foregrounded across nearly the whole slide.** Bottom padding is reclaimed and
  the stage is transparent/borderless so wide images read large, not boxed. Used
  for Zach's **chart** slides (wide aspect ratios need full width). In
  `ach-accents.css`.
- `placeholder-slide figure-side` — **horizontal variant: narrow title rail
  (~29%) on the left, screenshot fills the right at full slide height.** Used for
  Zach's **screenshot** slides (`zach-2`, `zach-4`, `zach-5`) — ~16:9 shots run
  taller this way than stacked under a title. In `ach-accents.css`.
- Zach's model-comparison (zach-4) uses the `walk-stage` reveal — each of the
  two comparison shots is shown full-stage in turn, not side by side (a 2-up
  made them unreadable, since each shot is itself a 2-model split). The
  `.gallery-2` CSS remains in `ach-accents.css` for any genuine 2-up need.

**Stepped image walkthrough** (e.g. Zach slide 2, sign-in → chat → models): put
`<img class="walk-step">` images in a `<figure class="stage walk-stage">`; the
first is the base, each later one gets `class="walk-step frag"` so clicks step
through them. Files: `images/zm-step1/2/3-*.png`.

## Preview / QA

No build step. Serve and open a slide by number:
```bash
python3 -m http.server 8765    # from this folder
# open http://localhost:8765/index.html#11   (#N = slide N)
```
For a headless screenshot of slide N (how QA is done — there are no tests):
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --window-size=1440,900 --virtual-time-budget=2500 --screenshot=out.png \
  "http://localhost:8765/index.html#N"`

## Deploy

Public deck lives at **https://cuny-ai-lab.github.io/ach-2026/** (repo
`CUNY-AI-Lab/ach-2026`, GitHub Pages off `main`). **Push to `main` → Pages
rebuilds (~1 min).** No build/CI step; the repo root is served as-is.

## Gotchas

- **CSS cache-buster (bites hard).** The stylesheet links carry a version query
  — `src/styles.css?v=…` and `src/ach-accents.css?v=…`. **Bump that `?v=` string
  every time you change a CSS file**, or browsers (and the Pages CDN) serve the
  *old* CSS and your layout change appears to do nothing. Use a date-ish token
  (e.g. `?v=20260624b`).
- iCloud-synced tree: PNGs can go `compressed,dataless`; `brctl download images`
  before heavy reads/renders if a screenshot stalls.

## House rules

- **Banned words in deck prose:** `bot`, `chatbot`, `assistant` (use
  "configuration" / "model card" / "conversation partner"). Exception:
  Azucena's student quotes are verbatim evidence — leave them as-is.
- **Privacy:** no student names, emails, or personal data; aggregate / anonymized
  sections only.
- **Fonts** load from Google Fonts (`Newsreader`, `IBM Plex Sans`/`Mono`); system
  serif/sans fall back offline.
- **Commits:** lowercase, detailed, ≤100 chars; never co-author as Claude Code.
