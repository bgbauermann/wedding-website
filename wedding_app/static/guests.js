//open modal

const modal = document.querySelector('.modal');
const modalConfirm = document.querySelector('#confirm-delete');

//open modal and add guest delete route
(document.querySelectorAll('.delete') || []).forEach(el => {
    
    el.addEventListener('click', () => {
        modalConfirm.action = el.dataset.guestRoute; 
        modal.classList.add('is-active');
    });
});


// close modals
(document.querySelectorAll('.modal-background, .modal-close')).forEach(el => {
    const target = el.closest('.modal');
    
    el.addEventListener('click', () => {
        target.classList.remove('is-active');
    });
});
