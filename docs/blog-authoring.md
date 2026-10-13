# Blog writing guide

The Blog lives at `/blog/` on the main research website. `Updates` continues to
hold conference, presentation and award announcements at its existing URLs.

## Choose one group

| `blog_group` | Label | Use for |
| --- | --- | --- |
| `paper-reviews` | Paper Reviews | Paper explanations, limitations and personal interpretation |
| `tech-industry` | Tech & Industry | Aerospace, defense and industry commentary |
| `research-notes` | Research Notes | Implementation, experiments, code and lessons learned |
| `reflections` | Reflections | Personal reflections and research life |

Groups are defined in `_data/blog_groups.yml`. Counts and lists are generated
from posts with `blog_group`, so existing Updates posts are not mixed into the Blog.
Empty groups remain available with an explicit empty state.

## Add a post

Create `_posts/YYYY-MM-DD-short-slug.md`:

```yaml
---
layout: blog-post
title: "A descriptive title"
date: 2026-10-12 09:00:00 +0900
blog_group: research-notes
lang: en
description: "A short summary for the post list and feed."
tags: [GNC, SINDy]
math: true
toc: true
related_posts: false
---
```

Write the article below the front matter. Choose the real publication date.
Use ordinary tags for technical topics. Tag links collect relevant articles
across groups. A topic should not become another `blog_group`.

Optional cover:

```yaml
image:
  path: /assets/img/posts/my-post/cover.png
  alt: "Description of the figure"
```

## Two languages in one post

Keep the title, description, and first body in English. To add Korean, add this
front matter to the same file:

```yaml
korean:
  title: "한국어 제목"
  description: "한국어 요약"
```

After the English body, put this separator on its own line, with blank lines
above and below, then write the Korean body:

```markdown
<!-- lang:ko -->

## 한국어 본문

여기부터 한국어 글을 작성합니다.
```

Publish only this one file. Lists, topic archives, counts, and RSS contain one
entry. The article's English / 한국어 switch changes the title, summary, body,
and contents links in place. The rest of the site stays in English.

Initial reading language follows the browser (Korean for `ko`, English otherwise)
unless the reader has saved a choice. Explicit `?lang=en` or `?lang=ko` links
override that preference. The switch remembers manual choices when browser
storage is available. A post without Korean stays readable in English. With
JavaScript disabled, both versions appear sequentially.

For paper reviews, identify the paper, authors and source link first. Distinguish
the source's findings from your interpretation. Preserve figure attribution.

Blog-specific RSS: `/blog/feed.xml`. The site's existing feed remains available.

## Migration notes

The original three language editions from `cinco125-source.github.io` are now
two posts: one bilingual SINDy review and one welcome note. Original figures
are preserved. Same-origin `/posts/slug/` compatibility pages and the former
`/blog/2026/sindy-mpc-multirotor-collision-avoidance-en/` URL redirect to the
combined article. English legacy links explicitly select `?lang=en`.

The source blog is retained. Redirecting its public GitHub Pages domain should
happen only after the integrated Blog is deployed and verified. No separate
`blog.lee-jd.com` DNS setup is needed for this architecture.

## Validation

Build with `JEKYLL_ENV=production bundle exec jekyll build`. As in the existing
deployment workflow, install ImageMagick and Python nbconvert first. Check Blog,
all four groups, tag archives, both language editions, feed and mobile layout.
Also check the homepage, Publications and Updates for regressions.
