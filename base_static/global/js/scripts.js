(() => {
    const forms = document.querySelectorAll('.form-delete');
    
    for(const form of forms){
        form.addEventListener('submit', function (e){
            e.preventDefault();

            const confirmed = confirm('Do you really want to delete this recipe?');

            if (confirmed){
                form.submit();
            }
        })
    }
})();

(()=>{
    const buttonCloseMenu = document.querySelector('.button-close-menu');
    const buttonShowMenu = document.querySelector('.button-show-menu');
    const menuContainer = document.querySelector('.menu-container');

    const buttonShowMenuVisibleClass = 'button-show-menu-visible';
    const menuHiddenClass='menu-hidden';

    const showMenu = () =>{
        buttonShowMenu.classList.remove(buttonShowMenuVisibleClass);
        menuContainer.classList.remove(menuHiddenClass);
    }

    const closeMenu = () =>{
        buttonShowMenu.classList.add(buttonShowMenuVisibleClass);
        menuContainer.classList.add(menuHiddenClass);
    }

    if(buttonCloseMenu){
        buttonCloseMenu.removeEventListener('click', closeMenu);
        buttonCloseMenu.addEventListener('click', closeMenu);
    }
    if(buttonShowMenu){
        buttonShowMenu.removeEventListener('click', showMenu);
        buttonShowMenu.addEventListener('click', showMenu);
    }

})();

(() =>{
    const authorsLogoutLink = document.querySelectorAll('.authors-logout-link');
    const formLogout = document.querySelector('.form-logout');

    for (const link of authorsLogoutLink){
        link.addEventListener('click', (e) =>{
            e.preventDefault();
            formLogout.submit()
        })
    }
})();

