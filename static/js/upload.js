function start_upload(up, name) {
  if (name.length === 0) {
    display_message("Please enter an Album Name");
    return;
  }

  // Starting upload process, warn when navigating away form page
  $( window ).on( "beforeunload", function() {
    return "Exiting will cancel upload.\nAre you sure?";
  });

  // Ajax call to create album, display error if album name is not created
  $.ajax({
    url: "album/",
    contentType: "application/json",
    data: JSON.stringify({
      album_name: album_name,
      album_create: true
    }),
    type: "POST",
    dataType: "json",
    headers: { "X-CSRFToken": getCookie( 'csrftoken' ) },

    success: function(response_json) {
      if (response_json['created'] && response_json['unique']) {      

        // Start plupload upload of images
        up.start();

      } else {
        display_message("Error: " + response_json['message_text']);
        return;
      }
    },

    error: function(xhr, status, errorThrown) {
      display_message("Error: Ajax error when creating the album.");
      console.log(errorThrown);
      return;
    }
  });
}


function display_message(message, type) {

  // Message type of alert is the default
  type = type || "alert";

  var error_message = "<div data-alert class='alert-box " + type + " radius'>" + 
                        message +
                        "<a href='#' class='close'>&times;</a>" +
                      "</div>"
  $('#error-display').html(error_message);

  // Attach foundation listiners and events to the alert box
  $(document).foundation('alert', 'reflow');
}


var uploader = new plupload.Uploader({
  // Plupload settings
  runtimes: 'html5,flash,silverlight',
  browse_button: 'file-select',
  url : "/visualize/upload/image/",
  file_data_name:'image',
  flash_swf_url: "/static/plupload/js/Moxie.swf",
  silverlight_xap_url: "/static/plupload/js/Moxie.xap",
  
  // Jpgs under 10mb only
  filters: {
    max_file_size: '10mb',
    mime_types: [
      {title: "Image files", extensions: "jpg, jpeg"},
    ]
  },

  // Plupload callback functions
  init: {
    PostInit: function(up) {

      // Plupload is loaded! Remove the requirement text and show the form.
      $('#plupload-requirments').fadeOut('fast', function() {
        $(this).remove();
        $("#plupload-form").fadeIn('fast');
      });

      document.getElementById('upload-btn').onclick = function() {

        // Verify there are files
        if (up.total.queued > 0) {              
          up.settings.album_name = $.trim(document.getElementById("album-name").value);
          album_response = start_upload(uploader, up.settings.album_name);
        } else {
          display_message("Please select at lease one file to upload.")
        }
        
        // start_upload only returns on an error, otherwise starts the upload
        return false;
      };
    },

    FilesAdded: function(up, files) {
      plupload.each(files, function(file) {

        // Add li to the DOM for each file selected
        var li_item = '<li id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ')<span class="file-upload-progress"></span></li>';
        
        var item = $( li_item ).prependTo( $( "#filelist" ) );
        var image = $( new Image() ).prependTo( item );

        // Instantiate the mOxie Image object.
        var preloader = new mOxie.Image();

        preloader.onload = function() {
          preloader.downsize(width=180, height=180, crop=true, preserveHeaders=false);
          image.prop("src", preloader.getAsDataURL());

          // Explicitly destroy the object to release it from memory
          preloader.destroy();
        }

        preloader.load(file.getSource());
      });

      document.getElementById("file-select").disabled = true;
      $( '#file-select' ).html("Files Selected").addClass("success")
      up.settings.total_files = up.total.queued;
      document.getElementById('upload-progress').innerHTML = 
      "<span>" + up.total.uploaded + "/" + up.settings.total_files + " Files Uploaded</span>";
    },

    // Add csrf token required by Django and the the other form elements to request
    BeforeUpload: function(up, file) {
      document.getElementById("upload-btn").disabled = true;
      $( '#upload-btn' ).html("Upload Started").addClass("success")

      // Remove check for album uniqueness
      $( '#album-name' ).unbind('blur');

      // Remove any error message that is displayed
      $('#error-display').children().fadeOut('fast', function() {
        $(this).remove();
      });

      up.settings.multipart_params = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        album_name: up.settings.album_name
      };
    },

    FileUploaded: function(up, file) {
      document.getElementById('upload-progress').innerHTML = 
      "<span>" + up.total.uploaded + "/" + up.settings.total_files + " Files Uploaded</span>";
      $( '#progress-bar' ).css('width', up.total.percent + "%");

      // Remove photo when it has been uploaded
      $( '#' + file.id ).fadeOut('slow', function( event ) {
        $( this ).remove()
      });
    },

    Error: function(up, err) {
      display_message("\nError #" + err.code + ": " + err.message);
    },

    UploadComplete: function() {
      // Remove window unload callback now that upload has completed
      $( window ).off( "beforeunload" );
    }
  }
});


// Initialize the plupload unloader
uploader.init();


// Check album name when the input field looses focus and give album name feedback
$( '#album-name' ).blur( function() {
  album_name = $.trim( $( '#album-name' ).val() );

  if (album_name.length === 0) {
  return;
  }

  // Ajax call to check album uniqueness
  $.ajax({
    url: "album/",
    contentType: "application/json",
    data: JSON.stringify({
      album_name: album_name,
      album_create: false
    }),
    type: "POST",
    dataType: "json",
    headers: { "X-CSRFToken": getCookie( 'csrftoken' ) },

    success: function(response_json) {
      if (response_json['unique']) {
        display_message("Album Name OK!", "success")
      } else {
        display_message("Error: " + response_json['message_text']);
        return;
      }
    },

    error: function(xhr, status, errorThrown) {
      display_message("Error: Ajax error when creating the album.");
      console.log(errorThrown);
      return;
    }
  });
});
