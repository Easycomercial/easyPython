var img1 = document.getElementById('img1');
var img2 = document.getElementById('img2');
var img3 = document.getElementById('img3');
var windowHeight = window.innerHeight;
var windowHeight = window.innerHeight;
var windowWidth = window.innerWidth;
var scrollArea = 8000 - windowHeight;

window.addEventListener('scroll', function () {

  var scrollTop = window.pageYOffset || window.scrollTop;
  var scrollPercent = scrollTop/scrollArea || 0;

  img1.style.right = -220 + scrollPercent*window.innerWidth*2 + 'px';
  img2.style.left =  -220 + scrollPercent*window.innerWidth + 'px';
  img3.style.right = -220 + scrollPercent*window.innerWidth*1 + 'px';

});
