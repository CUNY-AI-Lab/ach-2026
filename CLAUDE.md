# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The HTML slide deck for the **CUNY AI Lab panel at ACH 2026** (Fri June 26, 2026):
"Building Community-Oriented Infrastructures for AI Experimentation." 43 slides for
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
  layout, the `walk-step` image walkthrough, and the emblem (`.brand-mark`).
- `images/` — figures (copied from `../figures/`), Sandbox screenshots, the
  `zm-step*` walkthrough shots, the `ach26.svg` emblem, and logos.

## How the deck works (theme behavior)

- `slides.js` auto-paginates every `section.slide` and drives nav (arrow keys /
  space / footer scrubber / `btn-prev`·`btn-next`), the lightbox, and fragments.
  The footer counter and scrubber max are set from `slides.length` — **never
  hand-edit the "1 / 35"**; add or remove a `<section>` and it re-counts.
- **Fragments:** any element with class `frag` is hidden until revealed; each
  click/Right-arrow reveals the next `.frag`, then advances to the next slide.
- **Accents are CSS, keyed by `data-slide` prefix** (`matt-`, `luke-`, `zach-`,
  `azu-`, `steve-`) — see `ach-accents.css`. Keep the prefixes or colors/overview
  break.

## Slide layouts (class on the `<section>`)

- `slide-title` — title slide (animated WebGL background + title card).
- `placeholder-slide even-layout` / `odd-layout` — text column + figure stage.
- `placeholder-slide crowded` — text-only (stage hidden); used by Azucena/Steve.
- `placeholder-slide figure-hero` — **slim title bar on top, the image
  foregrounded across the whole body below.** Stage is transparent/borderless so
  wide screenshots read large, not boxed. Used for all of Zach's slides. Defined
  in `ach-accents.css`.
- `figure.stage figure-stage gallery-2` — two images side by side inside a
  figure-hero (Zach slide 4's model comparison).

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
For a headless screenshot of slide N:
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --window-size=1440,900 --virtual-time-budget=2500 --screenshot=out.png \
  "http://localhost:8765/index.html#N"`

## House rules

- **Banned words in deck prose:** `bot`, `chatbot`, `assistant` (use
  "configuration" / "model card" / "conversation partner"). Exception:
  Azucena's student quotes are verbatim evidence — leave them as-is.
- **Privacy:** no student names, emails, or personal data; aggregate / anonymized
  sections only.
- **Fonts** load from Google Fonts (`Newsreader`, `IBM Plex Sans`/`Mono`); system
  serif/sans fall back offline.
- **Commits:** lowercase, detailed, ≤100 chars; never co-author as Claude Code.
