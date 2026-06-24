# ACH 2026 panel deck — slide manifest

**Deck:** `cail-ach-2026/deck/index.html` (open in a browser, or serve with
`python3 -m http.server` from `deck/`).
**Theme:** the CALI-NARST deck (`cuny-ai-lab.github.io/cali-narst`) — dark
`#0f1319`, `Newsreader` serif display + `IBM Plex Sans`/`Mono`, per-presenter
accent colors. Assets in `deck/src/` (`styles.css`, `slides.js`) are the theme
verbatim; `deck/src/ach-accents.css` adds this panel's presenters.
**Navigation:** arrow keys / space / footer scrubber.
**Zach's layout:** his eight slides use the `figure-hero` layout — a slim title
bar (label + title) on top, the image foregrounded across the whole body below.
The stage is transparent/borderless so wide screenshots read large rather than
floating in a black box. The bullets are no longer on-slide; they live as the
spoken talk track at the bottom of this file. Zach slide 2 carries a stepped
image walkthrough (sign-in → chat → model picker) via the theme's `.frag`
reveal (`zm-step1/2/3-*.png`); his model-comparison slide (zach-4) is a
click-reveal of the two comparison screenshots, each shown full-stage (a
side-by-side made them unreadable, since each shot is already a 2-model split).
**Emblem:** `images/ach26.svg` (gold hands + lightbulb) is the panel mark — it
sits in the header top-left and as the favicon (shown once; the duplicate on
the title card was removed). It keeps its gold (the `.brand-mark` class cancels
the theme's logo-invert filter). The header top-right carries the white CUNY AI
Lab wordmark (`images/cail-logo-white.png`, `.header-cail-logo`).

**Panel:** Building Community-Oriented Infrastructures for AI Experimentation
**Event:** Association for Computers and the Humanities (ACH) 2026
**When:** Friday, June 26, 2026 · 12:00–13:15 CDT
**Presenting order:** Matthew Gold → Luke Waltzer → Zach Muhlbauer →
Azucena García Gutiérrez → Stephen Zweibel

41 slides total: 1 title · 8 Matt · 5 Luke · 1 Zach opener + 8 Zach ·
11 Azucena · 7 Steve.

## Status (QA pass)
All 41 slides were rendered and reviewed — every slide is visible and
well-formatted: no broken images, no text overflow, no empty/error slides.
- Title (1): single emblem, calmer title size, no subtitle, presenters in
  presenting order, CAIL wordmark top-right. ✓
- Matt (2–9): intentionally blank placeholders — label + "Slide N of 8 ·
  content to be drafted", vertically centered. No content. ✓
- Luke (10–14): recreated from source decks (cali-narst / cali-brooklyn) +
  the CALI 1/2 text supplied by the presenter. No content authored here. ✓
- Zach opener (15) + Zach (16–23): `figure-hero` — minimal title line, the
  image foregrounded across nearly the whole slide. Screenshots/charts read
  large. ✓
- Slide 17: 3-step sign-in → chat → model-picker reveal, real screenshots. ✓
- Slide 19: model-comparison click-reveal — each shot full-stage, readable. ✓
- Azucena (24–34) & Steve (35–41): text/quote slides, centered; all three
  quotes fit per slide without overflow. Section openers lead with affiliation
  (topical subtitles removed). ✓

| accent | presenter | data-slide |
|--------|-----------|-----------|
| pale blue `#c9d5e8` | Matthew Gold | `matt-1…8` |
| sage `#a8c4b5` | Luke Waltzer | `luke-1…5` |
| gold `#e8c89f` | Zach Muhlbauer | `zach-intro`, `zach-1…8` |
| lavender `#c9a6cf` | Azucena García Gutiérrez | `azu-1…11` |
| mint `#8fd5c3` | Stephen Zweibel | `steve-1…7` |

---

## 1 · Title
Panel title, presenters (in presenting order), event, date/time. No subtitle.
Animated WebGL background carried from the theme.

## Matt — slides 2–9 (BLANK placeholders)
Eight blank placeholder slides (`matt-1…8`): presenter label + "Slide N of 8 ·
content to be drafted". No content — Matt drafts these himself.

## Luke — slides 10–14 (CALI origin story)
Recreated faithfully from the presenter's source decks — content not authored
here. Note: connect the Lab's critical ethos and ethical commitments to the
CALI origin story and fellows' need for model-agnostic, accountable AI
infrastructure; how CALI grew into a broader infrastructure serving faculty,
students, and other publics across CUNY.

| # | title | source |
|---|-------|--------|
| luke-1 | The Critical AI Literacy Institute: Origins | cali-narst #4 (`cali-website-home.png`; Origins/Elements as `.frag`) |
| luke-2 | CALI: Grounding Scholarship | cali-narst #5 (`cali-books.gif`) |
| luke-3 | CALI as an Intervention | cali-brooklyn #3 (`step-grid`, 4 numbered areas) |
| luke-4 | CALI 1 | presenter text + `cali-cohort1-slide13.jpg` (cali-brooklyn `images/slide13.jpg`) |
| luke-5 | CALI 2 | presenter text (text-only) |

The `step-grid`/`step-row`/`step-num`/`step-text` CSS was imported verbatim from
cali-brooklyn into `ach-accents.css` (it is not part of the cali-narst theme).

## Zach — opener (15) + slides 16–23
Opener `zach-intro` (slide 15): name + section title + affiliation, like the
Azucena/Steve openers. Then the eight figure-hero slides:

Titles from `ach26.docx`; bullets distilled from `scripts/slides_data.py`
talk tracks; figures from `figures/` (banned words `bot`/`chatbot`/`assistant`
avoided per house style).

| # | title | figure |
|---|-------|--------|
| zach-1 | From CALI to the CUNY AI Lab | `13_cali_to_cail.png` |
| zach-2 | What is the CUNY AI Lab Sandbox? | 3-step reveal: `zm-step1-signin` → `zm-step2-chat` → `zm-step3-models` |
| zach-3 | Transparency and Privacy by Design | `14_zero_retention_flow.png` |
| zach-4 | Evaluating and Comparing Open-Weight Models | gallery: `owui_comparison_a.png` + `owui_comparison_b.png` |
| zach-5 | Supporting Purpose-Built, Custom Models | `owui_model_cards.png` |
| zach-6 | Communities of Practice within the Sandbox | `17_communities_hub.png` |
| zach-7 | T(h)inkering with Faculty Fellows | `18_thinkering_fellows.png` |
| zach-8 | Workshopping Project Pilots: AmigAI | `19_amigai_build.png` |

Hands off to Azucena after slide 8 (AmigAI, 36.6% of all messages).

## Azucena — slides 24–34
Reformatted from `Blue Modern Academic Analysis Presentation.pdf` (11 pages)
into the panel theme. Student quotes kept verbatim as evidence.

1. AmigAI in Spanish 204 (title)
2. Classroom Context — SPAN 204, Queens College; mixed HL/L2; CLA
3. Learning Outcomes
4. The Configuration's Prompt (system prompt, verbatim)
5. Interactions — three textbook texts; example exchange (Student A03)
6. Classroom Application — onboarding → reading → interaction → debrief
7. First Impressions — Positive (student quotes)
8. First Impressions — Critical (student quotes)
9. Conclusions
10. Examples of Interactions (live walkthrough)
11. Thank you / contact

Source also references a Canva deck: https://canva.link/09y0vdxtlx2dzla

## Steve — slides 35–41
From https://zweibel.net/ach-2026-steve/ (7 slides), reformatted into the theme.

1. Tools, Agentic AI, and Scholarly Communication (intro)
2. What the Lab Builds and Runs
3. Tools Portal (tools.ailab.gc.cuny.edu)
4. Working with Agentic AI (Agent Studio, Site Studio)
5. Kale Workbench
6. Kale Deploy
7. From Sandbox to a Live Web App (Sandbox → Workbench → Kale Deploy)

---

## Editing notes
- Add/reorder slides by editing `<section class="slide" data-slide="…">`
  blocks in `index.html`; `slides.js` re-paginates and the footer counter
  updates automatically (no need to hand-edit the `1 / 35`).
- Accents follow the `data-slide` prefix — keep the `matt-`/`zach-`/`azu-`/
  `steve-` prefixes so colors and the overview view stay correct.
- Fonts load from Google Fonts; system serif/sans fall back offline.
- Azucena and Steve slides are text-only (`.crowded`); drop in images by
  replacing the empty `figure.stage` with a `figure.stage.figure-stage` + `img`
  and switching the section to `even-layout`, as Zach's slides do.

---

## Zach — talk track (bullets, now spoken not on-slide)
Distilled from `scripts/slides_data.py`. Moved off the slides when they switched
to the `figure-hero` layout; deliver these over each figure.

### From CALI to the CUNY AI Lab
- Grew out of the Google.org-sponsored Critical AI Literacy Institute (CALI)
- Faculty wanted a stable place to work, with tools that persisted between sessions
- Launched spring 2026 with Academic Affairs, GCDI, the Mina Rees Library, and ASHP

### What is the CUNY AI Lab Sandbox?
- The Lab's chat and classroom AI environment, built on Open WebUI
- Curated open-weight models and configurable tools, behind CUNY sign-in
- Models on the left, chat in the center, system prompt and parameters on the right

### Transparency and Privacy by Design
- Model-agnostic routing to zero-retention endpoints: OpenRouter, Bedrock, Cloudflare, Google
- Provider-side: prompts and responses are not stored or used for training
- Sandbox-side: chat history still persists and is admin-readable — both are true

### Evaluating and Comparing Open-Weight Models
- Send one prompt to two curated models and read the responses side by side
- Token counts and response times surfaced for direct comparison
- A public Model Registry explains capabilities, licensing, and recommended use

### Supporting Purpose-Built, Custom Models
- Course-specific configurations: a base model, system prompt, documents, and tools
- Reusable project templates adapted across sections and semesters
- A configuration becomes a designed object students can interrogate

### Communities of Practice within the Sandbox
- One shared environment, one privacy posture, many communities
- CALI faculty development, fellows, course-tool builders, workshops, AmigAI sections
- Access maps to CUNY roles — it appears on enrollment and is revoked on drop

### T(h)inkering with Faculty Fellows
- Hands-on experimentation paired with critical thinking about what AI does
- Fellows design assignments that expose where the tools break
- An interdisciplinary cohort: sociology, mathematics, physics, policy, and music

### Workshopping Project Pilots: AmigAI
- One configuration template, adapted across three Spanish sections
- SPAN 101 conversation · SPA 204 discourse analysis · SPAN 207 heritage critique
- The AmigAI sections are the busiest workload — 36.6% of all messages

