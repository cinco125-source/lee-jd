# lee-jd.com — Personal website (al-folio)

Personal academic website for **Jayden Dongwoo Lee** (이동우), built on the
[al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Content lives in

| What | Where |
|------|-------|
| Name / identity / site meta | `_config.yml` |
| Homepage bio | `_pages/about.md` |
| Profile photo | `assets/img/prof_pic.jpg` |
| Publications (56 entries) | `_bibliography/papers.bib` |
| CV (education, awards, patents, service) | `_data/cv.yml` |
| News items | `_news/*.md` |
| Social links / email | `_data/socials.yml` |

## To finish (fill in when ready)
- `_data/socials.yml`: add `scholar_userid`, `orcid_id`, and a `cv_pdf` path.
- Drop your CV PDF at `assets/pdf/cv.pdf` and set `cv_pdf` in `_pages/cv.md`.

## Deploy
**GitHub Pages (recommended for al-folio):** push this folder to a repo, enable
Pages → GitHub Actions. al-folio ships a `.github/workflows/deploy.yml`. Add a
`CNAME` file containing `lee-jd.com` and point the domain's DNS to GitHub Pages.

**Vercel:** set the project *Root Directory* to this folder. Vercel needs a Ruby
build (`bundle exec jekyll build`, output `_site`); GitHub Pages is the smoother
path for Jekyll.

## Local preview
```
bundle install
bundle exec jekyll serve
```
