document.addEventListener('DOMContentLoaded', () => {

    const modales = document.querySelectorAll('.modal')
    modales.forEach((mod, index) => {
    mod.classList.add('modalid-'+(index+1))
    });

    const buttonmodals = document.querySelectorAll('.openmodal')
    buttonmodals.forEach((but, index) => {
        but.classList.add('openmodal-'+(index+1))
        but.addEventListener('click', ()=>{
            initModal(index+1)
        })
    });
})
    function initModal(ident){
        const len = document.querySelectorAll('.modal').length
        let openModal = (OpenModalButton, ModalWindow)=>{
            let buttonModal = document.querySelector('.openmodal-'+ident);
            if(buttonModal.dataset.modal == 'modal'){
                ModalWindow.classList.add('is-active');
            }
        }

        let closeModal = (ModalWindow)=>{
            ModalWindow.addEventListener('click', e=>{
            let elementClose = e.target;
                if(elementClose.classList.contains('delete') || elementClose.classList.contains('modal-background') || elementClose.classList.contains('closemodal')){
                    ModalWindow.classList.remove('is-active')
                }
            })
        }
        let Modal = ModalWindow =>{
            openModal(document.querySelector('.openmodal-'+ident), ModalWindow)
            closeModal(ModalWindow)
        }

        Modal(document.querySelector('.modalid-'+ident))
        
    }
