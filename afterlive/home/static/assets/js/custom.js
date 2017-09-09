var sdegree = 0;

var lastScrollTop = 0;
$(window).scroll(function(){
   var st = $(this).scrollTop();
   if (st > lastScrollTop){
     // downscroll code
     sdegree-- ;
     sdegree = sdegree - 2 ;

   } else {
      // upscroll code
      sdegree ++ ;
      sdegree = sdegree + 2 ;
   }
   lastScrollTop = st;

   var srotate = "rotate(" + sdegree + "deg)";
   $('.record').css({"-moz-transform" : srotate, "-webkit-transform" : srotate, "transform" : srotate,});
});

$(document).ready(function(){
	$('#nav-menu').click(function(){
		$(this).toggleClass('open');
		$('#nav-dropdown').toggleClass('drop');
		$('#nav-dropdown-addon').toggleClass('drop');
		$('body').toggleClass('nav-no-scroll');
	});
});

window.addEventListener("load", function(){
  $('#load_screen').toggleClass('fadeOut');
  $('body').toggleClass('nav-no-scroll');
});
