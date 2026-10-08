(() => {
  const input = document.getElementById('q');
  const shelves = [...document.querySelectorAll('.shelf')];
  const empty = document.getElementById('no-results');
  const term = document.getElementById('no-results-term');
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

  shelves.forEach(shelf => {
    shelf.querySelectorAll('.product').forEach(p => { p._search = norm(p.dataset.search); });

    const toggle = shelf.querySelector('.toggle');
    if (toggle) {
      toggle.addEventListener('click', () => {
        const open = shelf.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open);
        toggle.textContent = open ? 'Mostrar menos' : toggle.dataset.label;
      });
    }
  });

  input.addEventListener('input', () => {
    const q = norm(input.value.trim());
    let total = 0;

    shelves.forEach(shelf => {
      let visible = 0;
      shelf.querySelectorAll('.product').forEach(p => {
        const match = !q || p._search.includes(q);
        p.hidden = !match;
        if (match) visible++;
      });
      shelf.hidden = visible === 0;
      shelf.classList.toggle('searching', q !== '');
      total += visible;
    });

    term.textContent = input.value.trim();
    empty.hidden = !(q && total === 0);
  });
})();