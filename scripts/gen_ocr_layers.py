import os, re, html, json, subprocess, sys
from PIL import Image
IMG_DIR = "images"
HOCR_TMP = sys.argv[1]
# images to OCR (skip logos, wordless, vector).
EXCLUDE = {
    "ach26.svg","favicon.png","cail-logo-white.png","azu_thinking.png",
    "cali-books.gif","cail-homepage.png","cail-team-leadership.png","cail-team-fellows.png",
    "cail-site-home-team.png","cail-site-home-fellows.png",
}
TEXT_ONLY = {
    "cail-site-home-team.png": "CUNY AI Lab. Home. About. Tools. Resources. Team. Contact. CAIL Sandbox. A Graduate Center Initiative. AI Infrastructure for CUNY, by CUNY. The CUNY AI Lab is a faculty- and staff-led initiative that develops and maintains AI tools for teaching, learning, and research. We prioritize privacy, transparency, and thoughtful integration of AI into academic work. About the Lab. Explore Tools. Guiding Principles. Privacy by Design: We use providers that don't retain or train on user data. Transparency: We prioritize open-weight models that can be examined and understood. Environmental Accountability: Tools include visibility into computational costs. Criticality: AI literacy over AI dependency. Leadership. Matthew K. Gold. Laurie Hurson. Stefano Morello. Zach Muhlbauer. Maura Smale. Luke Waltzer. Stephen Zweibel.",
    "cail-site-home-fellows.png": "CUNY AI Lab. Home. About. Tools. Resources. Team. Contact. CAIL Sandbox. A Graduate Center Initiative. AI Infrastructure for CUNY, by CUNY. The CUNY AI Lab is a faculty- and staff-led initiative that develops and maintains AI tools for teaching, learning, and research. Guiding Principles. Fellows. Ellen Siyuan Pan. Jonathan Toro. Nicole Walker. Ian G. Williams. Collaborating Units. Graduate Center Digital Initiatives. Teaching and Learning Center. Mina Rees Library. American Social History Project.",
    "demo-asr.gif": "CUNY AI Lab. All Tools. Privacy Notice: Your audio/video files are sent to Fireworks AI API for transcription. When diarization is enabled, files are sent to AssemblyAI; transcripts are deleted immediately after processing. Data is not stored by the API providers. If you prefer local on-premises processing for sensitive content, please contact us at ailab@gc.cuny.edu. Audio Transcription. Upload audio or video files to generate automated transcriptions with optional speaker identification. Important: All AI-generated transcriptions should be reviewed manually for accuracy before use. Drag and drop a file here, or click to browse. Supports MP3, M4A, WAV, MP4, and other audio/video formats. Maximum file size: 1GB. Advanced Settings. Transcribe. Clear. Back to Tools.",
    "site-studio-new-project.png": "Site Studio. Create websites with your AI assistant. New Project. Create New Project. Choose a starting template - you can customize it to create anything you want using the AI assistant. Personal Pages. Simple landing pages and profiles. Minimal: Clean, centered landing page. Bold: Vibrant page with featured work. Sidebar: Sidebar navigation layout. Card: Card-based profile with content grid. CV and Resume. Academic and professional CVs.",
    "agent-studio-live.png": "Agent Studio. What would you like to work on? Search APIs, analyze data, create visualizations, or build tools. See what's possible. Ask anything or describe what you want to build. Try these: What can you do? Search papers. Analyze trends. Find books. Build a tool. Start blank. Built for the CUNY community.",
    "pdf-accessibility.png": "CUNY AI Lab PDF Accessibility. This tool is currently in beta. Results may vary; please review output carefully. Upload. Dashboard. Make PDFs accessible. Upload a PDF and we'll analyze its structure, generate alt text for images, add accessibility tags, and validate compliance. Upload PDF documents. Drag and drop PDF files, or click to browse. Multiple files supported for batch processing. What to expect: Processing typically takes one to three minutes. You'll get an accessible PDF with proper structure tags, alt text for images, and a compliance report. Checks include Classify, OCR, Structure, Alt Text, Tag, Validate, and Fidelity.",
}
MANUAL_OCR = {
    "cali-books.gif": [
        "Austerity Blues: Fighting for the Soul of Public Higher Education; Michael Fabricant and Stephen Brier",
        "Silicon Empires; Nick Srnicek",
        "The Campus Crisis Toolkit: Strategies and Solidarity for the Rest of Us; Lisa M. Di Bartolomeo and Kevin M. Gannon",
        "The AI Con: How To Fight Big Tech's Hype and Create the Future We Want; Emily M. Bender and Alex Hanna",
        "Atlas of AI; Kate Crawford",
        "Debates in the Digital Humanities 2023; Matthew K. Gold and Lauren F. Klein, editors",
        "Empire of AI: Dreams and Nightmares in Sam Altman's OpenAI; Karen Hao",
        "Pedagogy of the Oppressed; Paulo Freire",
        "Teaching to Transgress: Education as the Practice of Freedom; bell hooks",
        "Teaching Machines: The History of Personalized Learning; Audrey Watters",
        "The Great Mistake: How We Wrecked Public Universities and How We Can Fix Them; Christopher Newfield",
    ],
    "cail-homepage.png": [
        "CUNY AI Lab",
        "A Graduate Center Initiative",
        "AI Infrastructure for CUNY, by CUNY",
        "The CUNY AI Lab is a faculty- and staff-led initiative that develops and maintains AI tools for teaching, learning, and research.",
        "We prioritize privacy, transparency, and thoughtful integration of AI into academic work.",
        "About the Lab",
        "Explore Tools",
        "Guiding Principles",
        "Privacy by Design: We use providers that don't retain or train on user data",
        "Transparency: We prioritize open-weight models that can be examined and understood",
        "Environmental Accountability: Tools include visibility into computational costs",
        "Criticality: AI literacy over AI dependency",
        "2026 CUNY AI Lab",
    ],
    "cail-team-leadership.png": [
        "CUNY AI Lab",
        "Home; About; Tools; Resources; Blog; CAIL Sandbox",
        "Our Team",
        "The CUNY AI Lab is a collaborative initiative developed by faculty and staff at the Graduate Center with and for the CUNY community.",
        "Leadership",
        "Matthew K. Gold: Associate Professor of English and Digital Humanities; Director, Graduate Center Digital Initiatives",
        "Laurie Hurson: Assistant Director of Open Education; Teaching and Learning Center",
        "Stefano Morello: Assistant Director for Digital Projects; American Social History Project; Center for Media and Learning",
        "Zach Muhlbauer: Presidential Research Fellow; Teaching and Learning Center; Technical Lead, Critical AI Literacy Institute",
        "Maura Smale: Executive Chief Librarian; Mina Rees Library",
        "Luke Waltzer: Director; Teaching and Learning Center",
        "Stephen Zweibel: Associate Professor, Digital Scholarship Librarian; Mina Rees Library",
    ],
    "cail-team-fellows.png": [
        "Fellows",
        "Ellen Siyuan Pan",
        "Jonathan Toro",
        "Nicole Walker",
        "Ian G. Williams",
        "Collaborating Units",
        "Graduate Center Digital Initiatives",
        "Teaching and Learning Center",
        "Mina Rees Library",
        "American Social History Project",
    ]
}
def words_from_hocr(path):
    import xml.etree.ElementTree as ET
    t = ET.parse(path); out=[]
    for el in t.iter():
        if el.get('class')=='ocrx_word':
            m=re.search(r'bbox (\d+) (\d+) (\d+) (\d+)', el.get('title') or '')
            txt=''.join(el.itertext()).strip()
            if m and txt: out.append((tuple(map(int,m.groups())), txt))
    return out
def build_svg(img, words):
    W,H = Image.open(img).size
    spans=[]
    for (x0,y0,x1,y1),txt in words:
        fs=max(6,y1-y0)
        spans.append(f'<text x="{x0}" y="{y1-fs*0.18:.1f}" font-size="{fs}" textLength="{max(1,x1-x0)}" lengthAdjust="spacingAndGlyphs">{html.escape(txt)}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'preserveAspectRatio="xMidYMid meet" class="ocr-layer" aria-hidden="true">'
            f'<g font-family="sans-serif">{"".join(spans)}</g></svg>'), len(words)

def build_manual_svg(img, lines):
    W,H = Image.open(img).size
    fs = max(18, min(36, H // 44))
    line_w = max(1, W - fs * 2)
    step = fs * 1.55
    y = fs * 1.6
    spans=[]
    for line in lines:
        spans.append(f'<text x="{fs}" y="{y:.1f}" font-size="{fs}" textLength="{line_w}" lengthAdjust="spacingAndGlyphs">{html.escape(line)}</text>')
        y += step
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'preserveAspectRatio="xMidYMid meet" class="ocr-layer" aria-hidden="true">'
            f'<g font-family="sans-serif">{"".join(spans)}</g></svg>'), len(lines)
data={}
for f in sorted(os.listdir(IMG_DIR)):
    if not f.lower().endswith(('.png','.jpg','.jpeg')) or f in EXCLUDE: continue
    p=os.path.join(IMG_DIR,f)
    base=os.path.join(HOCR_TMP, os.path.splitext(f)[0])
    subprocess.run(["tesseract",p,base,"hocr"],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    hp=base+".hocr"
    if not os.path.exists(hp): continue
    words=words_from_hocr(hp)
    if len(words)<3: continue   # nothing worth a layer
    svg,n=build_svg(p,words); data[f]=svg
    print(f"  {f}: {n} words")
for f,lines in MANUAL_OCR.items():
    p=os.path.join(IMG_DIR,f)
    if not os.path.exists(p): continue
    svg,n=build_manual_svg(p,lines); data[f]=svg
    print(f"  {f}: {n} manual lines")
js = ("/* ocr-layers.js — AUTO-GENERATED. Adds transparent, selectable OCR text\n"
      "   layers over figure-stage images so the text inside screenshots\n"
      "   can be highlighted/copied. Regenerate with scripts/gen_ocr_layers (deck).\n"
      "   The SVG viewBox matches the image pixels and uses preserveAspectRatio meet,\n"
      "   so the transparent words track the contain-fit image as it scales. */\n"
      "(function(){'use strict';\n"
      "var OCR=" + json.dumps(data,separators=(',',':')) + ";\n"
      "var TEXT=" + json.dumps(TEXT_ONLY,separators=(',',':')) + ";\n"
      "var uid=0;\n"
      "function base(s){return (s||'').split('/').pop().split('?')[0];}\n"
      "function active(img){return !img.classList.contains('frag')||img.classList.contains('visible');}\n"
      "function sync(img,layer){layer.classList.toggle('ocr-active',active(img));}\n"
      "function text(layer){return Array.prototype.map.call(layer.querySelectorAll('text'),function(t){return t.textContent.trim();}).filter(Boolean).join(' ');}\n"
      "function describeText(img,txt){\n"
      " if(!txt) return;\n"
      " var id='ocr-text-'+(++uid); var span=document.createElement('span');\n"
      " span.id=id; span.className='sr-only ocr-text'; span.textContent='Text in image: '+txt;\n"
      " img.insertAdjacentElement('afterend',span);\n"
      " var cur=(img.getAttribute('aria-describedby')||'').trim().split(/\\s+/).filter(Boolean);\n"
      " if(cur.indexOf(id)<0) cur.push(id); img.setAttribute('aria-describedby',cur.join(' '));\n"
      "}\n"
      "function describe(img,layer){\n"
      " describeText(img,text(layer));\n"
      "}\n"
      "function add(img){\n"
      " var fig=img.closest('figure.stage,.figure-stage,.stage'); if(!fig) return;\n"
      " var name=base(img.getAttribute('src')); var svg=OCR[name]; var txt=TEXT[name]; if(!svg&&!txt) return;\n"
      " if(img.dataset.ocrLayer==='1') return;\n"
      " if(!svg){ describeText(img,txt); img.dataset.ocrLayer='1'; return; }\n"
      " var d=document.createElement('div'); d.innerHTML=svg;\n"
      " var layer=d.firstElementChild; layer.classList.add('ocr-active');\n"
      " if(img.classList.contains('walk-step')) layer.classList.add('ocr-walk-step');\n"
      " if(fig.classList.contains('mkg-gallery')){\n"
      "  var imgs=Array.prototype.slice.call(fig.querySelectorAll('img'));\n"
      "  var i=imgs.indexOf(img); layer.classList.add('ocr-gallery-layer');\n"
      "  layer.dataset.ocrIndex=String(i); layer.style.animationDelay=(i*4.5)+'s';\n"
      " }\n"
      " fig.appendChild(layer); describe(img,layer); img.dataset.ocrLayer='1';\n"
      " if(img.classList.contains('walk-step')){\n"
      "  sync(img,layer);\n"
      "  new MutationObserver(function(){sync(img,layer);}).observe(img,{attributes:true,attributeFilter:['class']});\n"
      " }\n"
      "}\n"
      "function run(){document.querySelectorAll('figure.stage img,.figure-stage img,.stage img').forEach(add);}\n"
      "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();\n"
      "})();\n")
open("src/ocr-layers.js","w").write(js)
print("wrote src/ocr-layers.js", len(js), "bytes;", len(data), "images")
