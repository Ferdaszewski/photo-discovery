$( '#photo-wrapper' ).click(function( event ) {
    if ( $(event.target).hasClass('delete-btn') ) {
        event.preventDefault();
        var element_id = $(event.target).data('photo-id')
        var csrf_token = getCookie('csrftoken');

        // Open modal conformation window
        $( '#del-confirm-modal' ).foundation( 'reveal', 'open' );

        // Set listener for modal close button
        $( '#del-confirm-modal .close-modal' ).click(function( event ) {
            event.preventDefault();
            $( '#del-confirm-modal' ).foundation( 'reveal', 'close' );
        });

        //Set listener for delete conformation button on modal window
        $( '#del-confirm-modal .delete-confirm-btn' ).click(function( event ) {
            event.preventDefault();

            // send AJAX call to delete the album
            $.post('', {id: element_id, csrfmiddlewaretoken: csrf_token}, function( resp ) {

                // Remove deleted photo from the DOM
                $("li." + element_id).fadeOut(duration=1000, complete=function() {this.remove()});

                // Close modal window
                $( '#del-confirm-modal' ).foundation( 'reveal', 'close' );                
            });
        });
    } else {
        return;
    }
});