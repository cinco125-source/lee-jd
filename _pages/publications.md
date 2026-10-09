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
  <a href="#intl-journals">International Journals <span>24</span></a>
  <a href="#dom-journals">Domestic Journals <span>5</span></a>
  <a href="#intl-conferences">International Conferences <span>29</span></a>
  <a href="#dom-conferences">Domestic Conferences <span>22</span></a>
</div>

{% include bib_search.liquid %}

<div class="publications pub-numbered">

<h2 class="bibliography-section-title" id="intl-journals">International Journals</h2>
<div class="num-list" style="counter-reset: pubnum 25;" data-prefix="J">
{% bibliography --query @article[scope=international] %}
</div>

<h2 class="bibliography-section-title" id="dom-journals">Domestic Journals</h2>
<div class="num-list" style="counter-reset: pubnum 6;" data-prefix="DJ">
{% bibliography --query @article[scope=domestic] %}
</div>

<h2 class="bibliography-section-title" id="intl-conferences">International Conferences</h2>
<div class="num-list" style="counter-reset: pubnum 30;" data-prefix="C">
{% bibliography --query @inproceedings[scope=international] %}
</div>

<h2 class="bibliography-section-title" id="dom-conferences">Domestic Conferences</h2>
<div class="num-list" style="counter-reset: pubnum 23;" data-prefix="DC">
{% bibliography --query @inproceedings[scope=domestic] %}
</div>

</div>
