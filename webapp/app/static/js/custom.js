/*!
* Start Bootstrap - Grayscale v7.0.5 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

//Hand the submit button for uploading a image
$("#photoUpload").on("click", function(){
     // clear any old form validation
     $(".needs-validation").removeClass('was-validated')
     $(".needs-validation").text("")
     let formData = new FormData();
     formData.append("photo", $('#photo').prop('files')[0]);
     $.ajax({
        url: "api/process_image",
        processData: false, // important
        contentType: false, // important
        method: "post",
        data: formData,
        success: function(result){
            if (result.status != "error"){
                console.log(result)
                // update the #detected_photo with the new image
                $("#detect_photo").attr("src", "data:image/jpg;base64,"+result.img);
            }
            else {
                $(".needs-validation").text(result.reason)
                $(".needs-validation").addClass('was-validated')
            }
        },
        error: function(e){
            console.log(e);
        }
     });
})