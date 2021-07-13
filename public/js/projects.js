let masonry = new Masonry('.grid', {
  itemSelector: '.grid-item',
  gutter: 20
});

function onload(ev) {
  window.dispatchEvent(new Event('resize'));
}

window.onload = onload;
