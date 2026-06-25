import os, re, html, json, subprocess, sys
from PIL import Image
IMG_DIR = "images"
HOCR_TMP = sys.argv[1]
# images to OCR (skip logos, wordless, vector).
EXCLUDE = {"ach26.svg","favicon.png","cail-logo-white.png","azu_thinking.png","cali-books.gif"}
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
      "function base(s){return (s||'').split('/').pop().split('?')[0];}\n"
      "function active(img){return !img.classList.contains('frag')||img.classList.contains('visible');}\n"
      "function sync(img,layer){layer.classList.toggle('ocr-active',active(img));}\n"
      "function add(img){\n"
      " var fig=img.closest('figure.stage,.figure-stage,.stage'); if(!fig) return;\n"
      " var svg=OCR[base(img.getAttribute('src'))]; if(!svg) return;\n"
      " if(img.dataset.ocrLayer==='1') return;\n"
      " var d=document.createElement('div'); d.innerHTML=svg;\n"
      " var layer=d.firstElementChild; layer.classList.add('ocr-active');\n"
      " if(img.classList.contains('walk-step')) layer.classList.add('ocr-walk-step');\n"
      " if(fig.classList.contains('mkg-gallery')){\n"
      "  var imgs=Array.prototype.slice.call(fig.querySelectorAll('img'));\n"
      "  var i=imgs.indexOf(img); layer.classList.add('ocr-gallery-layer');\n"
      "  layer.dataset.ocrIndex=String(i); layer.style.animationDelay=(i*4.5)+'s';\n"
      " }\n"
      " fig.appendChild(layer); img.dataset.ocrLayer='1';\n"
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
