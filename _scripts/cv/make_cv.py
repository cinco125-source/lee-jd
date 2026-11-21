# Builds cv.tex from _bibliography/papers.bib. The deploy workflow runs it and compiles cv.tex with xelatex,
# so the public CV PDF always matches the bib. Local run: python _scripts/cv/make_cv.py && xelatex cv.tex
import re, json, os, sys, datetime
OUT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(OUT, "..", ".."))
bib = open(f"{SITE}/_bibliography/papers.bib", encoding="utf-8").read()

def esc(s):
    s = s.replace("\&", "&")
    s = s.replace("σ", "$\sigma$")
    for a, b in [("&", "\&"), ("%", "\%"), ("#", "\#"), ("_", "\_")]:
        s = s.replace(a, b)
    s = s.replace("--", "--")
    return s

def field(body, k):
    m = re.search(r"\n\s*" + k + r"\s*=\s*\{(.*?)\},?\s*\n", body + "\n", re.S)
    return m.group(1).strip() if m else ""

entries = []
for typ, key, body in re.findall(r"@(article|inproceedings)\{(\w+),(.*?)\n\}", bib, re.S):
    e = {k: field(body, k) for k in ["title", "author", "journal", "booktitle", "year", "month", "note", "doi", "scope", "volume", "number", "pages"]}
    e["type"], e["key"] = typ, key
    entries.append(e)

MON = {m: i for i, m in enumerate(["", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
def sortkey(e): return (-int(e["year"] or 0), -MON.get(e["month"], 0))

def authors(a):
    a = a.replace("{", "").replace("}", "")
    others = a.endswith(" and others")
    a = a.replace(" and others", "")
    names = [n.strip() for n in a.split(" and ")]
    names = [r"\textbf{Jayden Dongwoo Lee}" if n in ("Jayden Dongwoo Lee", "이동우") else esc(n) for n in names]
    return ", ".join(names) + (", et al." if others else "")

def item(e):
    venue = e["journal"] if e["type"] == "article" else e["booktitle"]
    s = f"{authors(e['author'])}, ``{esc(e['title'].replace('{','').replace('}',''))},'' \\textit{{{esc(venue)}}}"
    if e["volume"]: s += f", vol. {e['volume']}"
    if e["number"]: s += f", no. {e['number']}"
    if e["pages"]: s += f", pp. {e['pages']}"
    s += f", {e['year']}."
    if e["note"]: s += f" \\textsc{{({e['note']})}}"
    if e["doi"]: s += f" \\href{{https://doi.org/{e['doi']}}}{{[doi]}}"
    return r"\item " + s

def section(typ, scope):
    L = sorted([e for e in entries if e["type"] == typ and e["scope"] == scope], key=sortkey)
    return len(L), "\n".join(item(e) for e in L)

nJ, J = section("article", "international")
nDJ, DJ = section("article", "domestic")
nC, C = section("inproceedings", "international")
nDC, DC = section("inproceedings", "domestic")
print("counts", nJ, nDJ, nC, nDC)

tpl = open(os.path.join(OUT, "cv_template.tex"), encoding="utf-8").read()
tex = (tpl.replace("%%JOURNALS%%", J).replace("%%DJOURNALS%%", DJ).replace("%%CONFS%%", C).replace("%%DCONFS%%", DC)
          .replace("%%DATE%%", datetime.date.today().strftime("%B %-d, %Y") if os.name != "nt" else datetime.date.today().strftime("%B %d, %Y"))
          .replace("%%NJ%%", str(nJ)).replace("%%NDJ%%", str(nDJ)).replace("%%NC%%", str(nC)).replace("%%NDC%%", str(nDC)))
open(os.path.join(OUT, "cv.tex"), "w", encoding="utf-8").write(tex)
