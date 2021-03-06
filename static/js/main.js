// Utility function to get a user's cookie.
// Primarily used to get the Django CSRF token for AJAX.
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Select text when user clicks in the field
$( '.share-url' ).on( 'mouseup', function( event ) {
    event.preventDefault();
    $( this ).children( 'input' ).select();
});