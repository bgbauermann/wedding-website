const menu = document.querySelector("#open-menu");
const modal = document.querySelector('.modal');
const modalImg = document.querySelector('.modal img');

//Open modal
menu.addEventListener('click', () => {
        modal.classList.add('is-active');
});

// close modals
(document.querySelectorAll('.modal-background, .modal-close, .modal img')).forEach(el => {
    const target = el.closest('.modal');
    
    el.addEventListener('click', () => {
        target.classList.remove('is-active');
    });
});

