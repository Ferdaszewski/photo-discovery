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


$( '#album-wrapper' ).click(function( event ) {
    if ( $(event.target).hasClass('delete-btn') ) {
        event.preventDefault();

        // send AJAX call to delete the album
        var element_id = $(event.target).data('album-id')
        var csrf_token = getCookie('csrftoken');
        $.post('', {id: element_id, csrfmiddlewaretoken: csrf_token}, function( resp ) {
            var share_id = resp['share_id']

            // Remove deleted album from the DOM - in menu drop-down and album list
            $("li." + share_id).fadeOut(duration=1000, complete=function() {this.remove()});
        });
    } else {
        return;
    }
});