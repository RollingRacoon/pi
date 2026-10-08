(() => {
  const radios = [...document.querySelectorAll('input[name="item_type"]')];
  const groups = [...document.querySelectorAll('.specs')];
  const hint = document.getElementById('specs-hint');
  if (!radios.length) return;

  // Fieldset desabilitado não é enviado: só a categoria escolhida chega ao Flask.
  const show = key => {
    groups.forEach(g => {
      const on = g.dataset.type === key;
      g.hidden = !on;
      g.disabled = !on;
    });
    hint.hidden = Boolean(key);
  };

  radios.forEach(r => r.addEventListener('change', () => show(r.value)));

  const checked = radios.find(r => r.checked);
  show(checked ? checked.value : null);
})();