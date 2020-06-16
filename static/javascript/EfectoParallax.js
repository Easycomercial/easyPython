var img1 = document.getElementById('img1');
var img2 = document.getElementById('img2');
var img3 = document.getElementById('img3');
var windowHeight = window.innerHeight;
var windowWidth = window.innerWidth;
var scrollArea = 20000;

window.addEventListener('scroll', function () {

  var scrollTop = window.pageYOffset || window.scrollTop;
  var scrollPercent = scrollTop/scrollArea || 0;

  img1.style.right = -230 + scrollPercent*window.innerWidth * 1 +  'px';
  img2.style.left =  -320 + scrollPercent*window.innerWidth * 0.8 + 'px';
  img3.style.right = -200 + scrollPercent*window.innerWidth * 0.8 + 'px';

});
