//videos do youtube//
const videoYtbLazy = document.getElementById('videoYtbLazy');

videoYtbLazy.addEventListener('click',snippetYtbLazyPlay)

function snippetYtbLazyPlay(evt) {
evt.currentTarget.removeEventListener('click', snippetYtbLazyPlay);
evt.currentTarget.innerHTML = `<iframe src="https://www.youtube.com/embed/${evt.currentTarget.dataset.id}?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>`;
}