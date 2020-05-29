
document.addEventListener("DOMContentLoaded",function()
{
    document.getElementById("phone").addEventListener("keypress",isNumberKey,{once:false});
    document.getElementById("phone").addEventListener("paste",isNumberKey,{once:false});
});


function isNumberKey(evt) {
    var theEvent = evt || window.event;
    console.log("key event")
    // Handle paste
    if (theEvent.type === 'paste') {
        key = (event.clipboardData || window.clipboardData).getData('text/plain');
        console.log("Pasted key=%s",key)
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
};
