---
layout: page
permalink: /publications/
title: publications
description: Journal articles and conference papers, in reverse-chronological order. <sup>*</sup> denotes corresponding/first author where applicable.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->
{% include bib_search.liquid %}

<div class="publications">

<h2 class="bibliography-section-title">Journal Articles</h2>
{% bibliography --query @article %}

<h2 class="bibliography-section-title">Conference Papers</h2>
{% bibliography --query @inproceedings %}

</div>
