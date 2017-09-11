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


  window.onload = function () {

	var parallaxBox = document.getElementById ( 'box' );
	var c4left = document.getElementById ( 'layer' ).offsetLeft,
	c4top = document.getElementById ( 'layer' ).offsetTop;

	parallaxBox.onmousemove = function ( event ) {
		event = event || window.event;
		var x = event.clientX - parallaxBox.offsetLeft,
		y = event.clientY - parallaxBox.offsetTop;

		mouseParallax ( 'layer', c4left, c4top, x, y, 65 );
	}

}

function mouseParallax ( id, left, top, mouseX, mouseY, speed ) {
	var obj = document.getElementById ( id );
	var parentObj = obj.parentNode,
	containerWidth = parseInt( parentObj.offsetWidth ),
	containerHeight = parseInt( parentObj.offsetHeight );
	obj.style.left = left - ( ( ( mouseX - ( parseInt( obj.offsetWidth ) / 2 + left ) ) / containerWidth ) * speed ) + 'px';
	obj.style.top = top - ( ( ( mouseY - ( parseInt( obj.offsetHeight ) / 2 + top ) ) / containerHeight ) * speed ) + 'px';
}