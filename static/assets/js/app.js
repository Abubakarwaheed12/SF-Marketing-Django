//  JS for This ....

$(document).ready(function(){

  $(".test_slider").slick({
    autoplay:true,
    autoplaySpeed:3000,
    prevArrow: $('.slider_left_btn'),
    nextArrow: $('.slider_right_btn'),
    rtl:false
});


$(".areas").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow: $('.slider1_left_btn'),
    nextArrow: $('.slider1_right_btn'),
    autoplay:true,
    autoplaySpeed:3000,
    autoplay:true,
    mobileFirst:true,
 
    /////script for responsive/////
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows:false,
            dots: false,
            prevArrow: false,
            nextArrow: false
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 300,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
});

});

 
  