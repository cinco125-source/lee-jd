(() => {
  const article = document.querySelector('.blog-article');
  if (!article) return;

  const panels = [...article.querySelectorAll('[data-blog-language]')];
  const choices = [...article.querySelectorAll('[data-blog-language-choice]')];
  const available = new Set(panels.map(panel => panel.dataset.blogLanguage));
  const storageKey = 'blog-reading-language';
  const validLanguage = value => value === 'en' || value === 'ko';
  let saved;
  try { saved = localStorage.getItem(storageKey); } catch { /* Storage is optional. */ }

  function showLanguage(language) {
    const selected = available.has(language) ? language : 'en';
    panels.forEach(panel => { panel.hidden = panel.dataset.blogLanguage !== selected; });
    choices.forEach(choice => {
      if (choice.dataset.blogLanguageChoice === selected) choice.setAttribute('aria-current', 'true');
      else choice.removeAttribute('aria-current');
    });

    const toc = article.querySelector('.blog-toc');
    if (toc) {
      const list = toc.querySelector('[data-blog-toc-list]');
      const headings = article.querySelectorAll(`.blog-prose [data-blog-language="${selected}"] h2, .blog-prose [data-blog-language="${selected}"] h3`);
      list.replaceChildren();
      headings.forEach((heading, index) => {
        if (!heading.id) heading.id = `${selected}-section-${index}`;
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = `#${heading.id}`;
        link.textContent = heading.textContent;
        if (heading.tagName === 'H3') item.className = 'blog-toc-subheading';
        item.append(link);
        list.append(item);
      });
      toc.querySelector('summary').textContent = selected === 'ko' ? '이 글의 목차' : 'Contents';
      toc.hidden = headings.length === 0;
    }
  }

  function languageFromLocation() {
    const explicit = new URL(location.href).searchParams.get('lang');
    if (validLanguage(explicit)) return explicit;
    if (location.hash) {
      try {
        const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
        const panel = target?.closest('[data-blog-language]');
        if (panel) return panel.dataset.blogLanguage;
      } catch { /* Ignore malformed fragments. */ }
    }
    return validLanguage(saved) ? saved : (navigator.language.toLowerCase().startsWith('ko') ? 'ko' : 'en');
  }

  showLanguage(languageFromLocation());
  choices.forEach(choice => choice.addEventListener('click', event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    saved = choice.dataset.blogLanguageChoice;
    try { localStorage.setItem(storageKey, saved); } catch { /* Reading still works without storage. */ }
    const url = new URL(location.href);
    url.searchParams.set('lang', saved);
    url.hash = '';
    history.pushState(null, '', url);
    showLanguage(saved);
  }));
  window.addEventListener('popstate', () => showLanguage(languageFromLocation()));
})();
