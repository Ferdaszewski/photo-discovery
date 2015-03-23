$( '#photo-wrapper' ).click(function( event ) {
    if ( $(event.target).hasClass('delete-btn') ) {
        event.preventDefault();

        // send AJAX call to delete the album
        var element_id = $(event.target).data('photo-id')
        var csrf_token = getCookie('csrftoken');
        $.post('', {id: element_id, csrfmiddlewaretoken: csrf_token}, function( resp ) {
            // Remove deleted photo from the DOM
            $("li." + element_id).fadeOut(duration=1000, complete=function() {this.remove()});
        });
    } else {
        return;
    }
});