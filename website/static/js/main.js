/*

	Template Name: SeoBin
	Author: Themewinter
	Author URI: https://themeforest.net/user/themewinter
	Description: SeoBin
	Version: 1.0

   1. Menu Active link
   2. Drop down Menu
	3. Main Slideshow
	4. Testimonial Slider
   5. Testimonial Slider
   6. Testimonial Box Carousel
	7. Counter Up
	8. Clients Carousel
   9. Back to top
   10. video Popup
   11. Our Mission Carousel
   12. Map
   13. Contact Form
   14. Service List Box Slider
   15. On Hover Timeline Active Changed
   16. On Click search bar
   17. Onclick off canvas menu visible
   18. Wow Initialize
   19. Accordion
   
  
*/

$(function ($) {
   "use strict";

   $(window).on('load', function(){
      checkScreenSize();
   });

   /* Menu Active link*/
   $('.nav-item ').on('click', function () {
      $('.nav-item ').removeClass('active');
      $(this).addClass('active');
   });

   /* DropDown Menu */
   $(window).on("resize", function (e) {
      checkScreenSize();
   });

   function checkScreenSize() {
      var newWindowWidth = $(window).width();
      if (newWindowWidth < 991) {
         $("li.nav-item a").on("click", function () {
            $(this).parent("li").find(".dropdown-menu").slideToggle();
            $(this).find("i").toggleClass("fa-angle-down fa-angle-up");
         });
      } else {
         $("li.nav-item a").on("click", function () {
            console.log('do nothing');
         });
      }
   }

   /*Main Slideshow*/
   $(".tw-hero-slider").owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      nav: true,
      dots: false,
      autoplayTimeout: 8000,
      autoplayHoverPause: true,
      mouseDrag: false,
      smartSpeed: 1100,
      navText: ['<i class="icon icon-left-arrow2">', '<i class="icon icon-right-arrow2">'],
   });

   /*Testimonial Slider*/
   $(".tw-testimonial-carousel").owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      nav: false,
      dots: true,
      autoplayTimeout: 5000,
      autoplayHoverPause: true,
      mouseDrag: false,
      smartSpeed: 900,
   });

   /* Testimonial Slider */
   if ($(".testimonial-slider").length > 0) {
      $(".testimonial-slider").owlCarousel({
         items: 1,
         loop: true,
         autoplay: true,
         nav: false,
         dots: true,
         autoplayTimeout: 5000,
         autoplayHoverPause: true,
         mouseDrag: true,
         smartSpeed: 900,
      });
   };

   /* Testimonial Slider */
   if ($(".testimonial-carousel-gray").length > 0) {
      $(".testimonial-carousel-gray").owlCarousel({
         items: 2,
         margin: 20,
         loop: true,
         autoplay: true,
         nav: false,
         dots: true,
         autoplayTimeout: 5000,
         autoplayHoverPause: true,
         mouseDrag: true,
         smartSpeed: 900,
      });
   };
   /* Testimonial Box Carousel */
   if ($(".testimonial-box-carousel").length > 0) {
      $(".testimonial-box-carousel").owlCarousel({
         items: 3,
         margin: 20,
         loop: true,
         autoplay: true,
         nav: false,
         dots: true,
         autoplayTimeout: 5000,
         autoplayHoverPause: true,
         mouseDrag: true,
         responsiveClass: true,
         smartSpeed: 900,
         responsive: {
            0: {
               items: 1,
            },
            600: {
               items: 2,
            },
            1000: {
               items: 3,
            }
         }
      });
   };


   /* Counter UP */
   $(".counter").counterUp({
      delay: 10,
      time: 2000
   });

   /* Client carousel */
   $(".clients-carousel").owlCarousel({
      items: 4,
      loop: true,
      nav: false,
      dots: true,
      autoplay: true,
      responsiveClass: true,
      autoplayHoverPause: true,
      mouseDrag: false,
      smartSpeed: 900,
      responsive: {
         0: {
            items: 1,
         },
         600: {
            items: 2,
         },
         1000: {
            items: 4,
         }
      }
   });

   /* Back to top */
   $(window).scroll(function () {
      if ($(this).scrollTop()) {
         $('.back-to-top button').fadeIn();
      } else {
         $('.back-to-top button').fadeOut();
      }
   });
   $(".back-to-top button").on('click', function () {
      $("html, body").animate({
         scrollTop: 0
      }, 1000);
   });

   /* Video Popup */
   if ($('.video-popup').length > 0) {
      $('.video-popup').magnificPopup({
         disableOn: 700,
         type: 'iframe',
         mainClass: 'mfp-fade',
         removalDelay: 160,
         preloader: false,
         fixedContentPos: false
      });
   };

   /* Our Mission Carousel */
   $('.mission-carousel').owlCarousel({
      items: 1,
      loop: true,
      nav: false,
      dots: true,
      autoplay: true,
      autoplayHoverPause: true,
      mouseDrag: false,
      smartSpeed: 900,
      animateOut: 'animated slideInRight',
      animateIn: 'animated slideInRight',
   });

   /* Map */
   if ($('#map').length > 0) {

      var contactmap = {
         lat: -37.816218,
         lng: 144.964068
      };

      $('#map')
         .gmap3({
            zoom: 12,
            center: contactmap,
            scrollwheel: false,
            mapTypeId: "shadeOfGrey",
            mapTypeControlOptions: {
               mapTypeIds: [google.maps.MapTypeId.ROADMAP, "shadeOfGrey"]
            }
         })

         .styledmaptype(
            "shadeOfGrey", [

               {
                  "featureType": "administrative",
                  "elementType": "geometry.stroke",
                  "stylers": [{
                     "color": "#fefefe"
                  }, {
                     "lightness": 17
                  }, {
                     "weight": 1.2
                  }]
               },
               {
                  "featureType": "administrative",
                  "elementType": "geometry.fill",
                  "stylers": [{
                     "color": "#fefefe"
                  }, {
                     "lightness": 20
                  }]
               },
               {
                  "featureType": "transit",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f2f2f2"
                  }, {
                     "lightness": 19
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.icon",
                  "stylers": [{
                     "visibility": "off"
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.text.fill",
                  "stylers": [{
                     "saturation": 36
                  }, {
                     "color": "#333333"
                  }, {
                     "lightness": 40
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.text.stroke",
                  "stylers": [{
                     "visibility": "on"
                  }, {
                     "color": "#ffffff"
                  }, {
                     "lightness": 16
                  }]
               },
               {
                  "featureType": "poi",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f5f5f5"
                  }, {
                     "lightness": 21
                  }]
               },
               {
                  "featureType": "road.local",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 16
                  }]
               },
               {
                  "featureType": "road.arterial",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 18
                  }]
               },
               {
                  "featureType": "road.highway",
                  "elementType": "geometry.stroke",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 29
                  }, {
                     "weight": 0.2
                  }]
               },
               {
                  "featureType": "road.highway",
                  "elementType": "geometry.fill",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 17
                  }]
               },
               {
                  "featureType": "landscape",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f5f5f5"
                  }, {
                     "lightness": 20
                  }]
               },
               {
                  "featureType": "water",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#e9e9e9"
                  }, {
                     "lightness": 17
                  }]
               }
            ], {
               name: "HQ"
            }
         )

         .marker({
            position: contactmap,
            icon: './images/icon/map_marker.png'
         })

         .infowindow({
            position: contactmap,
            content: "16122 Collins Street West. Victoria"
         })

         .then(function (infowindow) {
            var map = this.get(0);
            var marker = this.get(1);
            marker.addListener('click', function () {
               infowindow.open(map, marker);
            });
         });
   };

   /* Contact Form */
   $('#contact-form').submit(function () {

      var $form = $(this),
         $error = $form.find('.error-container'),
         action = $form.attr('action');

      $error.slideUp(750, function () {
         $error.hide();

         var $name = $form.find('.form-name'),
            $phone = $form.find('.form-phone'),
            $email = $form.find('.form-email'),
            $subject = $form.find('.form-subject'),
            $message = $form.find('.form-message');

         $.post(action, {
               name: $name.val(),
               phone: $phone.val(),
               email: $email.val(),
               subject: $subject.val(),
               message: $message.val()
            },
            function (data) {
               $error.html(data);
               $error.slideDown('slow');

               if (data.match('success') != null) {
                  $name.val('');
                  $phone.val('');
                  $email.val('');
                  $subject.val('');
                  $message.val('');
               }
            }
         );

      });

      return false;

   });

   /* Service List Box Slider */
   if ($(".service-list-carousel").length > 0) {
      $(".service-list-carousel").owlCarousel({
         items: 3,
         loop: true,
         margin: 10,
         autoplay: true,
         nav: true,
         navText: ['<i class="icon icon-arrow-left"></i>', '<i class="icon icon-arrow-right"></i>'],
         dots: false,
         autoplayTimeout: 5000,
         autoplayHoverPause: true,
         mouseDrag: true,
         responsiveClass: true,
         smartSpeed: 900,
         responsive: {
            0: {
               items: 1,
            },
            600: {
               items: 2,
            },
            1000: {
               items: 3,
               margin: 5,
            }
         }
      });
   };

   /* On Hover Timeline Active Changed */
   $(".timeline-wrapper .row").hover(function () {
      $(".timeline-item").find(".timeline-badge").removeClass("active");
      $(this).find(".timeline-badge").addClass("active");
   });
   $(".timeline-wrapper .row").hover(function () {
      $(".timeline-item").find(".timeline-date").removeClass("active");
      $(this).find(".timeline-date").addClass("active");
   });

   /* On Click search bar */
   $(".tw-search i, .tw-offcanvas-menu i").on('click', function () {
      $(".search-bar").addClass('active');
   });
   $(".search-bar i.fa-close").on('click', function () {
      $(".search-bar").removeClass('active');
   });

   /* Onclick offcanvas menu visible */
   $(".tw-menu-bar").on("click", function () {
      $(".offcanvas-wrapper").addClass('active');
      $(".offcanvas-menu-overlay").addClass('menu-show');
   });
   $(".menu-close-btn, .offcanvas-menu-overlay").on("click", function () {
      $(".offcanvas-wrapper").removeClass('active');
      $(".offcanvas-menu-overlay").removeClass('menu-show');
   });

   /* Wow Initialize */
   new WOW().init();

   /* Accordion */
   function toggleIcon(e) {
      $(e.target)
         .prev('.card-header')
         .find(".faq-indicator")
         .toggleClass('fa-minus fa-plus');
   }
   $('#accordion').on('hidden.bs.collapse', toggleIcon);
   $('#accordion').on('shown.bs.collapse', toggleIcon);

   /* Navbar fixed */
   $(window).on('scroll', function () {
      if ($(window).scrollTop() > 400) {
         $('.tw-head, .tw-header').addClass('navbar-fixed');
      } else {
         $('.tw-head, .tw-header').removeClass('navbar-fixed');
      }
      if ($(window).scrollTop() < 400) {
         setTimeout(() => {
            $('header').removeClass('off-canvas');
         }, 0);
      } else {
         setTimeout(() => {
            $('header').addClass('off-canvas');
         }, 0);
      }
   });

});