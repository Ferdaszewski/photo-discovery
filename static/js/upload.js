function start_upload(up, name) {
  if (name.length === 0) {
    display_error("Please enter an Album Name");
    return;
  }

  // Ajax call to create album, display error if album name is not unique
  $.ajax({
    url: "album/",
    data: {
      album_name: name,
      csrfmiddlewaretoken: getCookie('csrftoken')
    },
    type: "POST",
    dataType: "json",

    success: function(json) {
      if (json['success']) {            
        // Start plupload upload of images
        up.start();
      } else {
        display_error(json['error_message']);
        return;
      }
    },

    error: function(xhr, status, errorThrown) {
      display_error("Ajax error");
      error-display.log(errorThrown);
      return;
    }
  });
}


function display_error(message) {
  var error_message = "<div data-alert class='alert-box alert radius'>" + 
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
          display_error("Please select at lease one file to upload.")
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
      up.settings.total_files = up.total.queued;
    },

    // Add csrf token required by Django and the other form elements to request
    BeforeUpload: function(up, file) {
      document.getElementById("upload-btn").disabled = true;

      // Remove any error that is displayed
      $('#error-display').children().fadeOut('fast', function() {
        $(this).remove();
      });

      up.settings.multipart_params = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        album_name: up.settings.album_name
      };
    },

    UploadProgress: function(up, file) {
      document.getElementById(file.id).getElementsByClassName('file-upload-progress')[0].innerHTML = " " + file.percent + "%";
    },

    FileUploaded: function(up, file) {
      document.getElementById('upload-progress').innerHTML = 
      "<span>" + up.total.uploaded + "/" + up.settings.total_files + " - " + up.total.percent + "%</span>"
    },

    Error: function(up, err) {
      document.getElementById('error-display').appendChild(document.createTextNode("\nError #" + err.code + ": " + err.message));
    }
  }
});


uploader.init();

