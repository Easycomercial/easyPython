var img1 = document.getElementById('img1');
var windowHeight = window.innerHeight;
var windowWidth = window.innerWidth;
var scrollArea = 8000 - windowHeight;

window.addEventListener('scroll', function () {

  var scrollTop = window.pageYOffset || window.scrollTop;
  var scrollPercent = scrollTop/scrollArea || 0;

  img1.style.right = -35 + scrollPercent*window.innerWidth*1 + 'px';

});
