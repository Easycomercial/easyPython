
// document.addEventListener('DOMContentLoaded',function()
// {
//     document.querySelector('#phone').addEventListener('input',isNumberKey)
// })
$(document).ready(function(){
    $('[id^=phone]').keypress(isNumberKey)
    $('[id^=phone]').bind("paste",isNumberKey)
});


function isNumberKey(evt) {
    var theEvent = evt || window.event;
    //console.log("key event")
    // Handle paste
    if (theEvent.type === 'paste') {
        key = (event.clipboardData || window.clipboardData).getData('text/plain');
        //console.log("Pasted key=%s",key)
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }