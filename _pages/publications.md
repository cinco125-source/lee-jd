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
{% include bib_search.liquid %}

<div class="publications">

<h2 class="bibliography-section-title">Journal Articles</h2>
{% bibliography --query @article %}

<h2 class="bibliography-section-title">Conference Papers</h2>
{% bibliography --query @inproceedings %}

</div>
