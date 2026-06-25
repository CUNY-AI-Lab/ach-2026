# ACH 2026 panel deck — slide manifest

**Deck:** `cail-ach-2026/deck/index.html` (open in a browser, or serve with
`python3 -m http.server` from `deck/`).
**Theme:** the CALI-NARST deck (`cuny-ai-lab.github.io/cali-narst`) — dark
`#0f1319`, `Newsreader` serif display + `IBM Plex Sans`/`Mono`, per-presenter
accent colors. `deck/src/styles.css` + `deck/src/slides.js` are the theme
verbatim (do not edit); `deck/src/ach-accents.css` adds this panel's presenters,
layouts, and components; `deck/src/ach-fit.js` is our auto-shrink-to-fit script.
**Navigation:** arrow keys / space / footer scrubber. Footer order is
`← [scrubber] → ⛶ counter`; the scrubber `max` is hardcoded in `index.html`.
**Header:** gold emblem (`ach26.svg`) top-left → links to **ach2026.ach.org/en/**;
white CUNY AI Lab wordmark (`cail-logo-white.png`) top-right → ailab.gc.cuny.edu.
The emblem is also the favicon. (`.brand-mark` cancels the theme's logo-invert.)

**Panel:** Building Community-Oriented Infrastructures for AI Experimentation
**Event:** Association for Computers and the Humanities (ACH) 2026
**When:** Friday, June 26, 2026 · 12:00–13:15 CDT
**Presenting order:** Matthew Gold → Luke Waltzer → Zach Muhlbauer →
Azucena García Gutiérrez → Stephen Zweibel

**41 slides:** 1 title · 5 Matt · 6 Luke · 1 Zach opener + 8 Zach · 11 Azucena ·
9 Steve. (title=1 · matt 2–6 · luke 7–12 · zach-intro=13, zach 14–21 ·
azu 22–32 · steve 33–41.)

| accent | presenter | data-slide |
|--------|-----------|-----------|
| pale blue `#c9d5e8` | Matthew Gold | `matt-1…8` |
| sage `#a8c4b5` | Luke Waltzer | `luke-1…5` |
| gold `#e8c89f` | Zach Muhlbauer | `zach-intro`, `zach-1…8` |
| lavender `#c9a6cf` | Azucena García Gutiérrez | `azu-1…11` |
| mint `#8fd5c3` | Stephen Zweibel | `steve-1…9` |

## Layouts in use (class on the `<section>`)
- `slide-title` — animated WebGL background + title card.
- `crowded` — text-only; the `figure.stage` is `aria-hidden` and hidden.
- `odd-layout` / `even-layout` — text column + figure stage side by side.
- `figure-hero` — minimal title line on top, image fills the body (wide charts).
- `figure-side` — narrow title rail left, image fills the right at full height
  (screenshots / near-square images; aspect ≲ ~1.8).
- `walk-stage` — stacked `.walk-step` images; each later one is a `.frag` so a
  click swaps to it (used as a stepped reveal AND as a two-shot A→B toggle).

---

# Verbatim slide-by-slide

Each entry is the live content of the slide, exactly as in `index.html`:
**header(s)** then **body** then **image / stage**. `—` = no image (blank /
`aria-hidden` stage). Banned words (`bot`/`chatbot`) appear only inside
Azucena's verbatim student quotes, which are evidence and kept as-is.

## 1 · Title  (`title` · slide-title)
- eyebrow: **ACH 2026 · Friday, June 26 · 12:00–13:15 CDT**
- h1: **Building Community-Oriented Infrastructures for AI Experimentation**
- panelists: **Matthew Gold, Luke Waltzer, Zach Muhlbauer, Azucena García Gutiérrez, and Stephen Zweibel**
- institution: **CUNY Graduate Center · Association for Computers and the Humanities (ACH) 2026**
- stage: animated domain-warp canvas (no image file).

## Matt Gold — slides 2–6  (`matt-1…5` · crowded)
Five slides from `ach26.docx` (Matt's outline; Slide 3 uses his 2026-06-24 comment,
which supersedes the doc's older bullets). Text-only for now — the doc references
screenshots (CUNY context, DH platforms, AI-studies image) not yet in `images/`.

### 2 · `matt-1` (crowded) — The CUNY Context
- The largest urban public university
- Mission: to educate "the children of the whole people" of New York City
- The CUNY Graduate Center as a central node
- image: — (screenshot pending)

### 3 · `matt-2` (crowded) — CUNY as an Engine of Social Mobility
- blockquote — David Leonhardt, "America's Great Working-Class Colleges," *New York Times*, Jan 18 2017: "Because the elite colleges aren't fulfilling that responsibility, working-class colleges have become vastly larger engines of social mobility. The new data shows, for example, that the City University of New York system propelled almost six times as many low-income students into the middle class and beyond as all eight Ivy League campuses, plus Duke, M.I.T., Stanford and Chicago, combined."
- image: —

### 4 · `matt-3` (crowded) — DH at CUNY: Building Open Knowledge Infrastructures
- Building open-source platforms
- Building in response to community feedback and needs
- Prioritizing open source and open access
- Providing alternatives to enterprise infrastructure
- image: — (Commons/Manifold/DHDebates/CBOX screenshots pending)

### 5 · `matt-4` (crowded) — The Challenge
- note: **screenshot to be added** (image-only slide in the doc)
- image: — (screenshot pending)

### 6 · `matt-5` (crowded) — AI at CUNY
- Embed reflexive critique and a critical approach to technology
- Focus on classroom use
- Build alternatives to enterprise-level initiatives
- Preserve CUNY values
- image: — (critical-AI-studies image pending)

## Luke Waltzer — slides 7–12  (CALI origin story)
Recreated from the presenter's source decks (cali-narst / cali-brooklyn); content
not authored here. **Spoken note:** connect the Lab's critical ethos and ethical
commitments to the CALI origin story and fellows' need for model-agnostic,
accountable AI infrastructure; how CALI grew into a broader infrastructure
serving faculty, students, and other publics across CUNY.

### 7 · `luke-1` (odd-layout lw2) — The Critical AI Literacy Institute: Origins
- label: **Luke Waltzer** · h1: **The Critical AI Literacy Institute: Origins**
- body (`.parallel-points`): CUNY Context · Funding from Google.org · CALI as a Response
- image: **`cali-website-home.png`** (CALI website home page) · src: cali-narst #4

### 8 · `luke-2` (odd-layout) — CALI: Grounding Scholarship
- label: **Luke Waltzer** · h1: **CALI: Grounding Scholarship**
- body: Critical University Studies · Critical Ed Tech and Infrastructure Studies · DH, Science Education, Educational Development
- image: **`cali-books.gif`** (key texts) · src: cali-narst #5

### 9 · `luke-3` (odd-layout) — CALI as an Intervention
- label: **Luke Waltzer** · h1: **CALI as an Intervention** · h2: **Four interconnected areas**
- stage: `step-grid`, four numbered rows — **1 Faculty Development · 2 Research · 3 Research and Development · 4 Advocacy** · src: cali-brooklyn #3
- image: — (CSS step-grid, no file)

### 10 · `luke-4` (odd-layout) — CALI Goals
- label: **Luke Waltzer** · h1: **CALI Goals** · h2: **Three commitments**
- stage: `step-grid`, three numbered rows — **1 Reasoned Adoption ↔ Informed Refusal · 2 Communities of Practice · 3 Research, Tinker, Advocate** · src: cali-narst #8
- image: — (CSS step-grid, no file)

### 11 · `luke-5` (odd-layout) — CALI 1
- label: **Luke Waltzer** · h1: **CALI 1** · h2: **22 Faculty from 12 Campuses** · list-label: **Outcomes**
- body: Curricula · Survey Responses and Focus Groups · Faculty Reflections · Collaborations
- image: **`cali-cohort1-slide13.jpg`** (first CALI cohort, 2025) · src: cali-brooklyn slide13

### 12 · `luke-6` (odd-layout) — CALI 2
- label: **Luke Waltzer** · h1: **CALI 2** · h2: **23 Faculty from 12 Campuses** · list-label: **Tracks**
- body: Critical Foundations · Ecological Implications · T(h)inkering
- image: **`cali-cohort2-slide16.png`** (faculty presenting an 8-class module at the GC) · src: cali-brooklyn slide16

## Zach Muhlbauer — opener (12) + slides 13–20
Charts use `figure-hero` (title on top, image fills width); screenshots and the
near-square diagram use `figure-side` (title rail left, image fills right). The
on-slide bullets were removed; they now live as the spoken talk track at the
bottom of this file.

### 13 · `zach-intro` (crowded) — section opener
- label: **Zach Muhlbauer** · h1: **Experimentation as Infrastructure: The CUNY AI Lab Sandbox** · institution: **CUNY AI Lab · CUNY Graduate Center**
- image: —

### 14 · `zach-1` (figure-hero) — From CALI to the CUNY AI Lab
- image: **`13_cali_to_cail.png`** (CALI → year-one R&D → tools → proposal → CAIL timeline)

### 15 · `zach-2` (figure-side) — What is the CUNY AI Lab Sandbox?
- stage: `walk-stage`, 3-step reveal — **`zm-step1-signin.png`** → **`zm-step2-chat.png`** → **`zm-step3-models.png`** (sign-in → chat → model picker)

### 16 · `zach-3` (figure-hero) — Transparency and Privacy by Design
- image: **`14_zero_retention_flow.png`** (zero-retention routing flow)

### 17 · `zach-4` (figure-side) — Evaluating and Comparing Open-Weight Models
- stage: `walk-stage` A→B click-reveal — **`owui_comparison_a.png`** then **`owui_comparison_b.png`** (each shown full-stage; not side by side — each shot is itself a 2-model split)

### 18 · `zach-5` (figure-side) — Supporting Purpose-Built, Custom Models
- image: **`owui_model_cards.png`** (course-specific model configurations)

### 19 · `zach-6` (figure-side) — Communities of Practice within the Sandbox
- image: **`17_communities_hub.png`** (the Sandbox as connective tissue — near-square diagram)

### 20 · `zach-7` (figure-hero) — T(h)inkering with Faculty Fellows
- image: **`18_thinkering_fellows.png`** (fellows across five disciplines)

### 21 · `zach-8` (figure-hero) — Workshopping Project Pilots: AmigAI
- image: **`19_amigai_build.png`** (AmigAI adapted across three sections)
- Hands off to Azucena after this slide.

## Azucena García Gutiérrez — slides 21–31
Rebuilt from `Blue Modern Academic Analysis Presentation.pdf`. The dartboard,
interface, and transcript are real images; the original's thinking-person and
clipboard clip-art were **recreated as on-theme components** — a `.bubble-cloud`
(slide 29) and an interactive `.json-card` (slide 32). Student quotes verbatim;
attributions exactly match the source. Source also references a Canva deck:
https://canva.link/09y0vdxtlx2dzla

### 22 · `azu-1` (crowded) — title
- label: **Azucena García Gutiérrez** · h1: **AmigAI · Spanish 204** · institution: **City University of New York (CUNY) · The Graduate Center**
- image: —

### 23 · `azu-2` (crowded) — Classroom Context
- h1: **Classroom Context** · sub: **Intermediate Spanish · SPAN 204 · Queens College, CUNY**
- body (arrow-bullets):
  - A mixed classroom of heritage (HL) and second-language (L2) learners
  - Spanish-language textbooks lean on technologies that ignore diverse Latinx and Afrolatinx realities (Padilla & Vana, 2022; Vana & Padilla, 2024)
  - Equip students to critically analyze pedagogical texts and build a Critical Language Awareness (CLA) (Leeman, 2018)
  - Use AmigAI to help students challenge texts from their own textbook
- image: —

### 24 · `azu-3` (odd-layout) — Learning Outcomes
- h1: **Learning Outcomes** · sub: **AmigAI Intervention**
- body (arrow-bullets):
  - Develop awareness of how to scrutinize texts through guided questions
  - Provide a space to reflect on AI technologies in language education with AmigAI
  - Develop AI critical awareness about these technologies
  - Put students' full Spanish repertoires into practice
- image: **`azu_dartboard.png`** (three arrows in a bullseye) on a blended `.illus` stage

### 25 · `azu-4` (odd-layout) — The Configuration's Prompt
- h1: **The Configuration's Prompt**
- blockquote (the AmigAI system prompt, verbatim):
  > "You are a guide for conducting discourse analysis of educational texts in Spanish for intermediate-level college students (B2 level on the CEFR scale). You challenge the student to analyze the text critically. Your students include both Spanish L2 and heritage language learners. You speak Spanish at an intermediate level (B2 level on the CEFR scale). You never use praise, compliments, or validation in your responses. You guide the student only through questions."
- image: **`azu_amigai_interface.png`** (the AmigAI 204 configuration in the Sandbox)

### 26 · `azu-5` (crowded) — Interactions
- h1: **Interactions** · sub: **Texts and guided questions**
- body (arrow-bullets):
  - Three texts from the Spanish textbook: immigration, El Caribe, and Guatemalan Indigenous populations
  - AmigAI surfaces biases, stereotypes, omissions, and different realities within the text through guided questions
- blockquote (example exchange):
  > "Te pido que mires de nuevo el primer párrafo. En las líneas 3 a 6 dice que 'con mayor frecuencia el latino llega a los Estados Unidos con un nivel de estudios más alto y mejor preparado para ejercer trabajos bien remunerados' [1]. ¿Esta afirmación del texto, de que los trabajos son 'bien remunerados', coincide con la realidad de muchos inmigrantes latinos que conoces o de la que has oído hablar?" — *AmigAI, first interaction, Student A03*
- image: —

### 27 · `azu-6` (odd-layout) — Classroom Application
- h1: **Classroom Application** · sub: **Fundamental Components**
- body (check-bullets ✓):
  - Reading comprehension of the reading materials
  - Explanation of the task with AmigAI; onboarding instructions
  - Individual interaction with AmigAI
  - Debriefing discussion as a class
- image: **`azu_thinking.png`** (wordless illustration — a student in thought with abstract, text-free speech bubbles) on a blended `.illus` stage. (Replaced an earlier `.bubble-cloud` of Spanish guiding-question text, removed because the word-tokens flattened the tool's discourse.)

### 28 · `azu-7` (crowded · azu-impressions) — First Impressions / Positive Components
Three thematic columns (`.quote-cols.cols-3`) on a wide viewport; stacks to one
column at ≤1024px (medium/small). Top-aligned, compact. Grouped:
- **More intentional**
  - "…overall, this was a very positive interaction. It asked very specific questions, and it asked more about, like, in conversation." — Student 1
  - "I didn't expect it to be so detailed with these questions. And I thought it was very cool — quotes directly from the text." — Student 2
  - "When you have someone, or something else, to ask questions to think deeper, it kind of gives you a deeper understanding of what you're reading." — Student 4
- **"A before" and "an after" the readings**
  - "It feels informative, but it doesn't portray the negative side." — Student 1
  - "The chatbot actually helped me see the real side of immigration that the text might not have wanted to cover." — Student 2
  - "The text never talks about the push back on immigration or negative attention…" — Student 2
- **AI Critical Awareness**
  - "It makes me think of how ChatGPT is being trained — what are their perspectives, what kind of information are we actually reading?" — Student 3
  - "Los libros de texto cuentan con formas de enseñar relacionadas a una agenda." — Student 3
- image: —

### 29 · `azu-8` (crowded · azu-impressions) — First Impressions / Negative Components
Two thematic columns (`.quote-cols.cols-2`) on a wide viewport; stacks to one
column at ≤1024px. Grouped:
- **Awareness of their learning process through AI**
  - "Analyzing text… it's hard to do that on an AI-chat basis model." — Student 2
  - "There's a lot more opportunity for the student to voice their input in a natural way when it's in a real-life setting, like a classroom." — Student 2
  - "I feel like with AI, you lose that personal touch." — Student 2
  - "And doing it with the chatbot, you lose that humanity." — Student 2
  - "The false positivity feels like you are talking with a robot, a screen." — Student 1
- **Monolingual Approach**
  - "It would not translate for me. It just repeats the question." — Student 1
  - "If it's not gonna help me understand the text, what's the point?" — Student 1
- image: —

### 30 · `azu-9` (odd-layout) — Conclusions
- h1: **Conclusions**
- body (check-bullets ✓):
  - A pedagogical tool for AI critical-literacy discussions
  - Challenging to use under translingual approaches and at lower levels
  - Conversations that develop critical awareness
  - Technical issues and invisible labor remain real costs
- stage: **`.json-card`** — the **actual AmigAI 204 configuration**: `{ "id": "amigai--204", "base_model_id": "deepseek.v3.2", "name": "AmigAI 204", "params": { "system": "Eres un guía para hacer un análisis del discurso… (B2)… [… 11 pasos …]", "max_tokens": 168, "top_k": 40, "top_p": 0.9, "temperature": 0.3 } }`. The system prompt is truncated; the `<pre>` wraps (inline `white-space:pre-wrap`).
- image: — (CSS component, no file)

### 31 · `azu-10` (figure-hero) — Examples of Interactions
- h1: **Examples of Interactions**
- image: **`azu_examples_transcript.png`** (`.framed`) — AmigAI transcript analyzing "Corriente latina" with the student's written response

### 32 · `azu-11` (crowded) — Thank you
- h1: **Thank you** · institution: **CUNY, The Graduate Center · azucena.garciagutierrez39@gc.cuny.edu**
- image: —

## Stephen Zweibel — slides 32–40
From https://zweibel.net/ach-2026-steve/ (9 slides), reformatted into the theme.
All text-only (`crowded`); no images.

### 33 · `steve-1` — intro
- h1: **Tools, Agentic AI, and Scholarly Communication** · institution: **CUNY Graduate Center · Mina Rees Library**

### 34 · `steve-2` — What the Lab Builds and Runs
- How faculty and students build and run their own AI tools
- The impact of agentic AI on research and libraries
- An infrastructure layer for custom tool development

### 35 · `steve-3` — Tools Portal
- tools.ailab.gc.cuny.edu — standalone applications
- Media tools: transcription, OCR, image description; plus a disclosure tool and agentic studios
- Zero-retention: the providers store nothing from prompts or outputs

### 36 · `steve-4` — Working with Agentic AI
- Agent Studio and Site Studio for research tasks
- A shift from conversation toward task delegation
- Faculty and students build tools with minimal coding

### 37 · `steve-5` — Teaching Librarians to Build with AI
- Agentic AI for Library Practice: a 16-week program for CUNY librarians, no programming background needed
- Build working tools — Primo dashboards, LibGuides interfaces — with Claude Code, then investigate what it built
- Spot hallucinations and errors, verify against the docs; better equipped for work with patrons and students

### 38 · `steve-6` — Kale Workbench
- A coding agent in the browser, like Claude Code or Codex — on the lab's Cloudflare infrastructure, with open models
- The lab runs it, so it sets the model and the limits
- Nothing is pushed or published without your approval; hands off to Kale Deploy when ready

### 39 · `steve-7` — Kale Deploy
- Agents deploy it themselves, through an MCP server
- Build with an agent, and it's live at <project>.cuny.qzz.io — the first CUNY home for live web projects
- Hosts many projects at once for very little; users run their own

### 40 · `steve-8` — From Sandbox to a Live Web App
- Sandbox → Workbench → Kale Deploy
- From chat access, through governed development, to publication
- Accountability and institutional control throughout

### 41 · `steve-9` — CUNY-Run AI Infrastructure
- Together they let CUNY run its own AI infrastructure
- Built so the people who use it can inspect and operate it
- institution: CUNY AI Lab · ailab.gc.cuny.edu

---

# Asset audit (`images/`)

**In use (22):**
`ach26.svg` (emblem/favicon) · `favicon.png` · `cail-logo-white.png` (header) ·
`cali-website-home.png` · `cali-books.gif` · `cali-cohort1-slide13.jpg` ·
`cali-cohort2-slide16.png` · `13_cali_to_cail.png` · `zm-step1-signin.png` ·
`zm-step2-chat.png` · `zm-step3-models.png` · `14_zero_retention_flow.png` ·
`owui_comparison_a.png` · `owui_comparison_b.png` · `owui_model_cards.png` ·
`17_communities_hub.png` · `18_thinkering_fellows.png` · `19_amigai_build.png` ·
`azu_dartboard.png` · `azu_amigai_interface.png` · `azu_examples_transcript.png` ·
`azu_thinking.png` (slide 29).

**Orphaned (2 — present in `images/` but not referenced anywhere):**
- `azu_clipboard.png` — slide 32 (`azu-9`) uses a CSS `.json-card` instead.
- `TLC-Logo-v4-No-GC-white.png` — old footer logo, replaced by the CAIL wordmark.

Kept on disk for reference; safe to delete if you want a lean repo.

---

## Editing notes
- Add/reorder slides by editing `<section class="slide" data-slide="…">` blocks;
  `slides.js` re-paginates and the footer counter updates — but **bump the
  scrubber `<input … max="N">` by hand** and **bump the `?v=` cache-buster** on
  the CSS links whenever you touch a stylesheet.
- Keep the `matt-`/`luke-`/`zach-`/`azu-`/`steve-` `data-slide` prefixes so
  accents and the overview view stay correct.
- Components live in `ach-accents.css`: `h2.azu-sub`, `p.impressions-sub`,
  `p.list-label`, `ul.check-bullets`, `.azu-impressions` + `.quote-cols` /
  `.quote-col` / `.col-head`, `img.framed`, `.illus`, `.bubble-cloud`,
  `.json-card`, plus `figure-hero` / `figure-side` / `walk-stage` / `gallery-2`
  and the cali-brooklyn `step-grid`. Dense slides shrink to fit via the `--fit`
  auto-scale (`src/ach-fit.js`); write new sizes as `calc(<size> * var(--fit, 1))`.

---

## Zach — talk track (bullets, spoken not on-slide)
Distilled from `scripts/slides_data.py`; deliver these over each figure.

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
