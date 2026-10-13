(() => {
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

  // ----- catalog.html: filtro por categoria e ordenação -----
  const grid = document.getElementById('product-grid');
  if (grid) {
    const cards = [...grid.querySelectorAll('.product')];
    const chips = [...document.querySelectorAll('[data-filter]')];
    const sort = document.getElementById('sort');
    const empty = document.getElementById('grid-empty');
    let type = '';

    const sorters = {
      name: (a, b) => a.dataset.name.localeCompare(b.dataset.name, 'pt-BR'),
      'price-asc': (a, b) => a.dataset.price - b.dataset.price,
      'price-desc': (a, b) => b.dataset.price - a.dataset.price,
    };

    const apply = () => {
      cards.sort(sorters[sort ? sort.value : 'name']).forEach(card => grid.appendChild(card));
      let shown = 0;
      cards.forEach(card => {
        const on = !type || card.dataset.type === type;
        card.hidden = !on;
        if (on) shown++;
      });
      if (empty) empty.hidden = shown > 0;
    };

    chips.forEach(chip => chip.addEventListener('click', () => {
      type = chip.dataset.filter;
      chips.forEach(other => other.setAttribute('aria-pressed', other === chip));
      apply();
    }));
    if (sort) sort.addEventListener('change', apply);
    apply();
  }

  // ----- item_admin.html: busca na tabela -----
  const q = document.getElementById('admin-q');
  if (q) {
    const rows = [...document.querySelectorAll('#admin-rows tr')];
    const count = document.getElementById('admin-count');
    const empty = document.getElementById('admin-empty');
    rows.forEach(row => { row._search = norm(row.dataset.search); });

    q.addEventListener('input', () => {
      const term = norm(q.value.trim());
      let shown = 0;
      rows.forEach(row => {
        const match = !term || row._search.includes(term);
        row.hidden = !match;
        if (match) shown++;
      });
      count.textContent = `${shown} ${shown === 1 ? 'item' : 'itens'}`;
      empty.hidden = shown > 0;
    });
  }
  // ----- ratings.html: galeria de fotos do item -----
  const main = document.getElementById('gallery-main');
  if (main) {
    const thumbs = [...document.querySelectorAll('.gallery-thumb')];
    thumbs.forEach(btn => btn.addEventListener('click', () => {
      main.src = btn.dataset.src;
      thumbs.forEach(other => other.setAttribute('aria-pressed', other === btn));
    }));
  }
})();