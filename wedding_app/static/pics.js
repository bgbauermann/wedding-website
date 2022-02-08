const imgs = (document.querySelectorAll("#pic_tiles img") || []);
const modal = document.querySelector('.modal');
const modalImg = document.querySelector('.modal img');

//Open modal and set img url to the image clicked
imgs.forEach(el => {
    el.addEventListener('click', () => {
        modalImg.src = el.src;
        modal.classList.add('is-active');
    });
});

// close modals
(document.querySelectorAll('.modal-background, .modal-close, .modal img')).forEach(el => {
    const target = el.closest('.modal');
    
    el.addEventListener('click', () => {
        target.classList.remove('is-active');
    });
});

