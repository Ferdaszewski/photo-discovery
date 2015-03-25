var imgLoad = new imagesLoaded( '#album-wrapper' );
var imgs_loaded = 0;

imgLoad.on( 'always', function( instance ) {
    $('#pre-load').fadeOut('slow', function() {
        $('#album-wrapper').fadeIn('slow');
    });
    
    // show images now that they are loaded
    console.log("ALWAYS - all images loaded.")

});

imgLoad.on( 'done', function( instance ) {
    console.log("DONE - " + instance.images.length + " images have been successfully loaded")
});

imgLoad.on( 'fail', function( instance ) {
    console.log("FAIL - all images loaded, at least one is broken")
});

imgLoad.on( 'progress', function( instance, image ) {
    if (image.isLoaded) {
        imgs_loaded += 1;
    }
    $('#pl-counter').text(imgs_loaded)
});

// get total number of images in this album and display
var img_total = $('#album-wrapper').find('img').length;
$('#pl-total').text(img_total);
$('#pl-counter').text(imgs_loaded);
