/* ach-fit.js — auto-shrink-to-fit for slide content.
   The cali-narst theme sizes type with viewport clamps, which can overflow a
   slide when the text is dense (Azucena's quote boards, long bullet stacks).
   This watches the *active* slide (inactive slides are display:none, so they
   can't be measured) and lowers a per-slide `--fit` multiplier until the
   content fits its box — the type tokens in ach-accents.css are written as
   `calc(token * var(--fit))`, so everything scales together. No theme files
   are touched. */
(function () {
  'use strict';
  var MIN = 0.58;   // never shrink below 58% — past that, rethink the slide
  var STEP = 0.03;

  function fit(slide) {
    if (!slide || !slide.classList || !slide.classList.contains('active')) return;
    var content = slide.querySelector(':scope > .content');
    if (!content) return;
    content.style.setProperty('--fit', '1');
    var cs = getComputedStyle(slide);
    var avail = slide.clientHeight
      - parseFloat(cs.paddingTop || 0)
      - parseFloat(cs.paddingBottom || 0);
    if (avail <= 0) return;                       // slide not laid out yet
    var k = 1;
    for (var i = 0; i < 20 && k > MIN; i++) {
      if (content.clientHeight <= avail + 2) break;
      k = Math.max(MIN, k - STEP);
      content.style.setProperty('--fit', k.toFixed(3));
      void content.offsetHeight;                  // force reflow before re-measure
    }
  }

  function fitActive() {
    var s = document.querySelector('section.slide.active');
    if (s) fit(s);
  }

  function init() {
    var slides = document.querySelectorAll('section.slide');
    if (!slides.length) return;

    // Re-fit whenever a slide gains `.active` (covers every nav path the theme
    // uses: arrows, scrubber, hash, overview exit).
    var obs = new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        var t = muts[i].target;
        if (t.classList && t.classList.contains('active')) {
          requestAnimationFrame(function () { fit(t); });
        }
      }
    });
    slides.forEach(function (s) {
      obs.observe(s, { attributes: true, attributeFilter: ['class'] });
    });

    // Fragment reveals (clicks / arrow keys) change content height without
    // toggling `.active`; re-fit the active slide on the next frame.
    var refit = function () { requestAnimationFrame(fitActive); };
    document.addEventListener('keydown', refit, { passive: true });
    document.addEventListener('click', refit, true);

    var rt;
    window.addEventListener('resize', function () {
      clearTimeout(rt); rt = setTimeout(fitActive, 120);
    });

    // First paint — wait for webfonts so we measure the real metrics.
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(fitActive);
    }
    requestAnimationFrame(fitActive);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
