# ACH 2026 panel deck — slide manifest

**Deck:** `cail-ach-2026/deck/index.html` (open in a browser, or serve with
`python3 -m http.server` from `deck/`).
**Theme:** the CALI-NARST deck (`cuny-ai-lab.github.io/cali-narst`) — dark
`#0f1319`, `Newsreader` serif display + `IBM Plex Sans`/`Mono`, per-presenter
accent colors. Assets in `deck/src/` (`styles.css`, `slides.js`) are the theme
verbatim; `deck/src/ach-accents.css` adds this panel's presenters.
**Navigation:** arrow keys / space / footer scrubber.
**Zach's layout:** his eight slides use the `figure-hero` layout — only the
presenter label + title sit at the top; the figure fills the slide body below.
The bullets are no longer on-slide; they live as the spoken talk track at the
bottom of this file. Zach slide 2 carries a stepped image walkthrough (sign-in →
chat → model picker) via the theme's `.frag` reveal (`zm-step1/2/3-*.png`).
**Emblem:** `images/ach26.svg` (gold hands + lightbulb) is the panel mark — it
sits in the header, on the title card, and as the favicon. It keeps its gold
(the `.brand-mark` class cancels the theme's logo-invert filter).

**Panel:** Building Community-Oriented Infrastructures for AI Experimentation
**Event:** Association for Computers and the Humanities (ACH) 2026
**When:** Friday, June 26, 2026 · 12:00–13:15 CDT
**Presenting order:** Matthew Gold → Luke Waltzer → Zach Muhlbauer →
Azucena Garcia Gutierrez → Stephen Zweibel

35 slides total: 1 title · 8 Matt/Luke (blank) · 8 Zach · 11 Azucena · 7 Steve.

## Status (QA pass)
All 35 slides were rendered and reviewed — every slide is visible and
well-formatted: no broken images, no text overflow, no empty/error slides.
- Title: emblem + animated background, presenters in presenting order. ✓
- Zach (10–17): `figure-hero` — figures fill the body under the title. ✓
- Slide 11: 3-step sign-in → chat → model-picker reveal, real screenshots. ✓
- Azucena (18–28) & Steve (29–35): text/quote slides, all legible.
- Matt/Luke (2–9): intentionally blank (title + "content to be drafted").
Known-by-design: blank slides read sparse until drafted; text slides are
left-aligned (theme default), leaving open space on wide displays.

| accent | presenter(s) | data-slide |
|--------|--------------|-----------|
| pale blue `#c9d5e8` | Matt Gold & Luke Waltzer | `matt-1…8` |
| gold `#e8c89f` | Zach Muhlbauer | `zach-1…8` |
| lavender `#c9a6cf` | Azucena Garcia Gutierrez | `azu-1…11` |
| mint `#8fd5c3` | Stephen Zweibel | `steve-1…7` |

---

## 1 · Title
Panel title, subtitle, presenters (in presenting order), event, date/time.
Animated WebGL background carried from the theme.

## Matt & Luke — slides 2–9 (BLANK placeholders)
Eight blank slides to be drafted. Working titles are placeholders only.
Planning notes from `ach26.docx` to seed them:
- **Matt:** set the stakes; CUNY's public-serving mission; the proven track
  record of open-source innovation and community-led infrastructure (Manifold,
  CAC); teaching critical AI studies alongside advocacy/service (Empire AI,
  GC's forthcoming AI guidelines, GC digital initiatives, scholarly comms).
- **Luke:** connect the Lab's critical ethos to the CALI origin story and
  fellows' need for model-agnostic, accountable AI infrastructure; how CALI
  grew into a broader infrastructure serving faculty, students, and publics.
- Closing (Matt or Luke): return to the shared question — how can CAIL support
  hands-on AI experimentation that builds institutional capacity toward AI
  infrastructure that is accountable, interpretable, and owned by its users.

## Zach — slides 10–17
Titles from `ach26.docx`; bullets distilled from `scripts/slides_data.py`
talk tracks; figures from `figures/` (banned words `bot`/`chatbot`/`assistant`
avoided per house style).

| # | title | figure |
|---|-------|--------|
| zach-1 | From CALI to the CUNY AI Lab | `13_cali_to_cail.png` |
| zach-2 | What is the CUNY AI Lab Sandbox? | 3-step reveal: `zm-step1-signin` → `zm-step2-chat` → `zm-step3-models` |
| zach-3 | Transparency and Privacy by Design | `14_zero_retention_flow.png` |
| zach-4 | Evaluating and Comparing Open-Weight Models | `owui_comparison_a.png` |
| zach-5 | Supporting Purpose-Built, Custom Models | `owui_model_cards.png` |
| zach-6 | Communities of Practice within the Sandbox | `17_communities_hub.png` |
| zach-7 | T(h)inkering with Faculty Fellows | `18_thinkering_fellows.png` |
| zach-8 | Workshopping Project Pilots: AmigAI | `19_amigai_build.png` |

Hands off to Azucena after slide 8 (AmigAI, 36.6% of all messages).
Note: slide 4 shows one comparison screenshot (`owui_comparison_a`); the source
has a second (`owui_comparison_b`) if a side-by-side is wanted later.

## Azucena — slides 18–28
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

## Steve — slides 29–35
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

