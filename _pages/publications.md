---
layout: page
permalink: /publications/
title: publications
description: Journal articles and conference papers, in reverse-chronological order. The first tag on each paper shows the research area.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->
{% include lee_style.liquid %}

<div class="pub-jump">
  <a href="#intl-journals" data-tab="intl-journals">International Journals <span>24</span></a>
  <a href="#dom-journals" data-tab="dom-journals">Domestic Journals <span>6</span></a>
  <a href="#intl-conferences" data-tab="intl-conferences">International Conferences <span>29</span></a>
  <a href="#dom-conferences" data-tab="dom-conferences">Domestic Conferences <span>22</span></a>
</div>

{% include bib_search.liquid %}

<div class="publications pub-numbered">

<div class="pub-tab" id="intl-journals">
<h2 class="bibliography-section-title">International Journals</h2>
<div class="num-list" style="counter-reset: pubnum 25;" data-prefix="J">
{% bibliography --query @article[scope=international] %}
</div>
</div>

<div class="pub-tab" id="dom-journals">
<h2 class="bibliography-section-title">Domestic Journals</h2>
<div class="num-list" style="counter-reset: pubnum 7;" data-prefix="DJ">
{% bibliography --query @article[scope=domestic] %}
</div>
</div>

<div class="pub-tab" id="intl-conferences">
<h2 class="bibliography-section-title">International Conferences</h2>
<div class="num-list" style="counter-reset: pubnum 30;" data-prefix="C">
{% bibliography --query @inproceedings[scope=international] %}
</div>
</div>

<div class="pub-tab" id="dom-conferences">
<h2 class="bibliography-section-title">Domestic Conferences</h2>
<div class="num-list" style="counter-reset: pubnum 23;" data-prefix="DC">
{% bibliography --query @inproceedings[scope=domestic] %}
</div>
</div>

</div>

<script>
  (function () {
    var tabs = document.querySelectorAll(".pub-tab");
    var btns = document.querySelectorAll(".pub-jump a");
    function show(id, scrollTo) {
      var found = false;
      tabs.forEach(function (t) { var on = t.id === id; t.style.display = on ? "" : "none"; if (on) found = true; });
      if (!found) return false;
      btns.forEach(function (b) { b.classList.toggle("active", b.dataset.tab === id); });
      if (scrollTo) { var el = document.getElementById(scrollTo); if (el) setTimeout(function () { el.scrollIntoView({ block: "center" }); }, 50); }
      return true;
    }
    function route() {
      var h = decodeURIComponent(location.hash.slice(1));
      if (h && show(h)) return;
      var el = h && document.getElementById(h);
      var tab = el && el.closest(".pub-tab");
      if (tab) { show(tab.id, h); return; }
      show("intl-journals");
    }
    btns.forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); history.replaceState(null, "", "#" + b.dataset.tab); show(b.dataset.tab); }); });
    window.addEventListener("hashchange", route);
    route();
  })();
</script>
