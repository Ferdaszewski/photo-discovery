// Instantiate a new imagesLoaded object
var imgLoad = new imagesLoaded( '#album-wrapper' );

// Set variables to track number of photos loaded/total and display them
var imgs_loaded = 0;
var img_total = $( '#album-wrapper' ).find( 'img' ).length;
$( '#pl-total' ).text( img_total );
$( '#pl-counter' ).text( imgs_loaded );


// Set event listeners on imagesLoaded events
imgLoad.on( 'always', function( instance ) {

    // Images are finished loading, remove loading info and show images
    $( '#pre-load' ).fadeOut( 'slow', function() {
        $( '.thumbscrubber' ).fadeIn( 'slow' );

        // Remove pre-load DOM node as we no longer need it
        $( this ).remove();
        albumScrubber();
    });
});

imgLoad.on( 'done', function( instance ) {
    console.log("DONE - " + instance.images.length + " images have been successfully loaded")
});

imgLoad.on( 'fail', function( instance ) {
    console.log("FAIL - all images loaded, at least one is broken")
});

imgLoad.on( 'progress', function( instance, image ) {

    // Display the new number of images successfully loaded
    if ( image.isLoaded ) {
        imgs_loaded += 1;
    }
    $( '#pl-counter' ).text(imgs_loaded)
});


// Image Scrubber
// Based on an idea from Sage Arslan. http://zurb.com/forrst/posts/iPhoto_like_Thumbnail_Scrubber_with_jQuery-Gc2
function albumScrubber() {
    var as_previous;
    var as_current = 1;
    changeImage();

    var width = $( '#album-wrapper' ).innerWidth();
    var numslides = img_total;

    function changeImage() {
        $( '#album-inner > .as-current' ).removeClass( 'as-current' );
        $( '#album-inner > :nth-child(' + as_current + ')' ).addClass( 'as-current' );

        // Change background color to match displayed image
        var hexrgb = $( '#album-inner > .as-current' ).data( 'hexrgb' )
        $( 'body' ).css( 'background-color' , hexrgb );
    };

    $( document ).on( 'mousemove', 'body', function( e ) {
        x = e.pageX - $(this).offset().left;
        as_current = Math.floor(x / (width / numslides)) + 1;

        if( as_current != as_previous ){
          as_previous = as_current;
          changeImage();
        }
        return false;
    });
}
