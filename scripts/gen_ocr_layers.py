import os, re, html, json, subprocess, sys
from PIL import Image
IMG_DIR = "images"
HOCR_TMP = sys.argv[1]
# images to OCR (skip logos, wordless, vector). JS only applies to single-image stages.
EXCLUDE = {"ach26.svg","favicon.png","cail-logo-white.png","azu_thinking.png","cali-books.gif"}
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
js = ("/* ocr-layers.js — AUTO-GENERATED. Adds a transparent, selectable OCR text\n"
      "   layer over each single-image figure stage so the text inside screenshots\n"
      "   can be highlighted/copied. Regenerate with scripts/gen_ocr_layers (deck).\n"
      "   The SVG viewBox matches the image pixels and uses preserveAspectRatio meet,\n"
      "   so the transparent words track the contain-fit image as it scales. */\n"
      "(function(){'use strict';\n"
      "var OCR=" + json.dumps(data,separators=(',',':')) + ";\n"
      "function base(s){return (s||'').split('/').pop().split('?')[0];}\n"
      "function add(img){\n"
      " var fig=img.closest('figure.stage,.figure-stage,.stage'); if(!fig) return;\n"
      " if(fig.querySelectorAll('img').length!==1) return;\n"            # single-image stages only
      " var svg=OCR[base(img.getAttribute('src'))]; if(!svg) return;\n"
      " if(fig.querySelector('.ocr-layer')) return;\n"
      " var d=document.createElement('div'); d.innerHTML=svg;\n"
      " fig.appendChild(d.firstElementChild);\n"
      "}\n"
      "function run(){document.querySelectorAll('figure.stage img,.figure-stage img,.stage img').forEach(add);}\n"
      "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();\n"
      "})();\n")
open("src/ocr-layers.js","w").write(js)
print("wrote src/ocr-layers.js", len(js), "bytes;", len(data), "images")
