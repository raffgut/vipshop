document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
            const links = document.getElementsByClassName('linkwhite');
            for(i=0; i<links.length;i++){
                links[i].classList.add('linkblack')   
            }   
          
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
          
        
        });
      });
    }

    const modales = document.querySelectorAll('.modal')
    modales.forEach((mod, index) => {
      mod.classList.add('modalid-'+(index+1))
    });

    const buttonmodals = document.querySelectorAll('.openmodal')
    buttonmodals.forEach((but, index) => {
      but.classList.add('openmodal-'+(index+1))
    });

    const deletes = document.querySelectorAll('.delete')
    deletes.forEach((del, index) => {
      del.classList.add('delete-'+(index+1))
    });

    const backgrounds = document.querySelectorAll('.modal-background')
    backgrounds.forEach((back, index) => {
      back.classList.add('modal-background-'+(index+1))
    });

    const closes = document.querySelectorAll('.closemodal')
    closes.forEach((clouse, index) => {
      clouse.classList.add('closemodal-'+(index+1))
    });

    const len = document.querySelectorAll('.modal').length
        for(i=1; i<=len; i++){
          let buttonModal = document.querySelector('.openmodal-' + i);
          console.log(buttonModal)
          const openModal = (OpenModalButton, ModalWindow)=>{
            if(buttonModal.dataset.modal == 'modal'){
              OpenModalButton.addEventListener('click',()=>{
                ModalWindow.classList.add('is-active');
              })
            }
          }

          const closeModal = (ModalWindow)=>{
            ModalWindow.addEventListener('click', e=>{
              const elementClose = e.target;
              if(elementClose.classList.contains('delete') || elementClose.classList.contains('modal-background') || elementClose.classList.contains('closemodal')){
                ModalWindow.classList.remove('is-active')
              }
          })
          }
          const Modal = ModalWindow =>{
            openModal(document.querySelector('.openmodal-' + i), ModalWindow)
            closeModal(ModalWindow)
          }

          Modal(document.querySelector('.modal-' + i))
        }

});

$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
        
    });
});