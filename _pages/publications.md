---
layout: page
permalink: /publications/
title: publications
description: Journal articles and conference papers, in reverse-chronological order. The first tag on each paper shows the research area.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->
{% include lee_style.liquid jn=30 cn=52 %}

<div class="pub-jump">
  <a href="#journal-articles">Journal Articles <span>29</span></a>
  <a href="#conference-papers">Conference Papers <span>51</span></a>
</div>

{% include bib_search.liquid %}

<div class="publications pub-numbered">

<h2 class="bibliography-section-title" id="journal-articles">Journal Articles</h2>
<div class="journal-list">
{% bibliography --query @article %}
</div>

<h2 class="bibliography-section-title" id="conference-papers">Conference Papers</h2>
<div class="conf-list">
{% bibliography --query @inproceedings %}
</div>

</div>
