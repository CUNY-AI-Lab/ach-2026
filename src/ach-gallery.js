/* ach-gallery.js — horizontal scroll for the First Impressions quote galleries.
   The vendored cali-narst slides.js navigates the deck on horizontal wheel and
   touch-swipe (document-level listeners). Inside a .quote-gallery we want those
   same gestures to scroll the cards instead. So we catch the events on the
   gallery (they bubble through it before reaching document), stop them, and drive
   the horizontal scroll ourselves. Presentation pagination — arrows, space, the
   footer scrubber — is untouched, so the deck still advances slide-by-slide. */
(function () {
  function bind(g) {
    // Wheel / trackpad: keep slides.js from advancing, scroll by the dominant axis
    // so a vertical mouse wheel also moves the gallery sideways.
    g.addEventListener('wheel', function (e) {
      e.stopPropagation();
      var d = Math.abs(e.deltaX) >= Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      if (d) { g.scrollLeft += d; e.preventDefault(); }
    }, { passive: false });
    // Touch: let the browser scroll the overflow natively; just shield slides.js.
    ['touchstart', 'touchmove', 'touchend'].forEach(function (t) {
      g.addEventListener(t, function (e) { e.stopPropagation(); }, { passive: true });
    });
  }
  function init() {
    var galleries = document.querySelectorAll('.quote-gallery');
    for (var i = 0; i < galleries.length; i++) bind(galleries[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
