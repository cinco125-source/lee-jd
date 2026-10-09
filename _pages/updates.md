---
layout: page
permalink: /updates/
title: updates
description: Talks, conferences, awards, and other updates.
nav: true
nav_order: 4
---

{% include lee_style.liquid %}

{% assign items = site.posts | where_exp: "p", "p.categories contains 'updates'" %}
{% assign years = items | group_by_exp: "p", "p.date | date: '%Y'" %}

<div class="upd-years">
{% for y in years %}<a href="#y{{ y.name }}">{{ y.name }}</a>{% endfor %}
</div>

{% for y in years %}
<h2 class="upd-year" id="y{{ y.name }}">{{ y.name }}</h2>
<div class="upd-grid">
  {% for p in y.items %}
  <a class="upd-card" href="{{ p.url | relative_url }}">
    <div class="upd-img"><img src="{{ p.thumbnail | relative_url }}" alt="{{ p.title | escape }}" loading="lazy"></div>
    <div class="upd-body">
      <div class="upd-date">{{ p.date | date: "%b %d, %Y" }}</div>
      <div class="upd-title">{{ p.title }}</div>
      <p class="upd-excerpt">{{ p.content | strip_html | strip_newlines | truncate: 120 }}</p>
    </div>
  </a>
  {% endfor %}
</div>
{% endfor %}
