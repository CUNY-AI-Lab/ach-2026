# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The HTML slide deck for the **CUNY AI Lab panel at ACH 2026** (Fri June 26, 2026):
"Building Community-Oriented Infrastructures for AI Experimentation." 41 slides for
five presenters (see `SLIDES.md` for the per-presenter ranges and count). It is **based on the `cuny-ai-lab/cali-narst` theme**
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
  layout, the `walk-step` image walkthrough, the emblem (`.brand-mark`), the
  `step-grid` rules imported verbatim from cali-brooklyn (for Luke's Intervention
  slide; not part of the vendored cali-narst theme), Azucena's restored
  components (`.azu-impressions` quote boards, `.bubble-cloud`, `.json-card`,
  `.illus`), and the `--fit` auto-shrink type scale.
- `src/ach-fit.js` — **our** auto-shrink-to-fit (not theme). Lowers `--fit` on
  the active slide's `.content` until its text stops overflowing the slide box;
  the type tokens in `ach-accents.css` are `calc(token * var(--fit))`. Runs on
  slide activation, fragment reveals, and resize. Loaded after `slides.js` in
  `index.html`. To make a new font-size participate, write it as
  `calc(<size> * var(--fit, 1))`.
- `images/` — figures (copied from `../figures/`), Sandbox screenshots, the
  `zm-step*` walkthrough shots, the `ach26.svg` emblem, and logos.

## How the deck works (theme behavior)

- `slides.js` auto-paginates every `section.slide` and drives nav (arrow keys /
  space / footer scrubber / `btn-prev`·`btn-next`), the lightbox, and fragments.
  The footer **counter** ("18 / 41") is set from `slides.length` — don't
  hand-edit it. The scrubber's **`max` attribute is NOT** — it's hardcoded on
  `<input id="slide-scrubber" … max="41">` in `index.html`; bump it whenever you
  add/remove a slide or the scrubber stops short. (Footer order is currently
  `← [scrubber] → ⛶ counter`, full-width — overridden in `ach-accents.css`.)
- **Fragments:** any element with class `frag` is hidden until revealed; each
  click/Right-arrow reveals the next `.frag`, then advances to the next slide.
- **Accents are CSS, keyed by `data-slide` prefix** (`matt-`, `luke-`, `zach-`,
  `azu-`, `steve-`) — see `ach-accents.css`. Keep the prefixes or colors/overview
  break.

## Slide layouts (class on the `<section>`)

- `slide-title` — title slide (interactive Molnar canvas background + title card).
- `placeholder-slide even-layout` / `odd-layout` — text column + figure stage.
- `placeholder-slide crowded` — text-only (stage hidden); used by Azucena/Steve.
- `placeholder-slide figure-hero` — **minimal title line on top, the image
  foregrounded across nearly the whole slide.** Bottom padding is reclaimed and
  the stage is transparent/borderless so wide images read large, not boxed. Used
  for Zach's **chart** slides (wide aspect ratios need full width). In
  `ach-accents.css`.
- `placeholder-slide figure-side` — **horizontal variant: narrow title rail
  (~29%) on the left, image fills the right at full slide height.** Used for
  Zach's screenshots and **near-square images** (`zach-2`, `zach-4`, `zach-5`,
  `zach-6`) — anything ~16:9 or squarer reads bigger this way than stacked under
  a title. **Wide charts stay `figure-hero`** (they need the full width). Rule of
  thumb: aspect ratio ≲ ~1.8 → `figure-side`; wider → `figure-hero`. In
  `ach-accents.css`.
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
python3 -m http.server 8765 --directory .   # run from this folder; --directory
# open http://localhost:8765/index.html#11   pins it so cwd can't misroute it
```
**Serve the deck folder, not its parent.** Launched from the repo root, `localhost:8765` has no `index.html` and shows nothing — pass `--directory <deck>` to be safe. For a preview that survives, run the server in your own shell (`! python3 …`); servers backgrounded from inside a Claude tool call get reaped between turns.
For a headless screenshot of slide N (how QA is done — there are no tests):
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --window-size=1440,900 --virtual-time-budget=2500 --screenshot=out.png \
  "http://localhost:8765/index.html#N"`

Two headless-QA traps that have wasted real time:
- **Confirm the server is actually up** before reading a screenshot
  (`curl -s -o /dev/null -w '%{http_code}' http://localhost:8765/index.html`).
  A dead server yields a stale/blank shot that looks like "my change did
  nothing." When a fix seems ignored, suspect the server/screenshot before the
  CSS.
- **Headless floors the CSS viewport at ~500px.** `--window-size=390` still
  renders at `innerWidth≈500` but the *screenshot* is 390px wide — so the right
  ~110px is cropped and looks like overflow that isn't real. To test mobile, use
  `--window-size=500,900` (screenshot width == viewport) and treat ~500px as the
  narrowest reliable width.

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
- **Changed an image? Cache-bust the `<img src>` too.** Editing a file in
  `images/` in place keeps its URL, so browsers and the Pages CDN serve the
  *stale* PNG. Append/bump a `?v=…` on that specific `src` in `index.html`
  (the CSS `?v=` won't cover it).
- iCloud-synced tree: PNGs can go `compressed,dataless`; `brctl download images`
  before heavy reads/renders if a screenshot stalls.
- **Mobile (<720px):** the layouts collapse to one column via the theme. A
  `@media (max-width:720px)` block in `ach-accents.css` force-shrinks stage
  images (`min-width:0; max-width:100%`) — without it a wide image keeps its
  intrinsic width (flex `min-width:auto`) and is clipped by the stage's
  `overflow:hidden`. Keep that guard if you touch stage CSS.

## House rules

- **Banned words in deck prose:** `bot`, `chatbot`, `assistant` (use
  "configuration" / "model card" / "conversation partner"). Exception:
  Azucena's student quotes are verbatim evidence — leave them as-is.
- **Privacy:** no student names, emails, or personal data; aggregate / anonymized
  sections only.
- **Fonts** load from Google Fonts (`Newsreader`, `IBM Plex Sans`/`Mono`); system
  serif/sans fall back offline.
- **Commits:** lowercase, detailed, ≤100 chars; never co-author as Claude Code.
