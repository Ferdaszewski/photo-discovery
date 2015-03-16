document.addEventListener('DOMContentLoaded', function() {

    // Get form elements
    var form = document.getElementById('upload-form');
    var imageSelect = document.getElementById('image-select');
    var uploadButton = document.getElementById('upload-button');
    var csrftoken = form.children.namedItem('csrfmiddlewaretoken').value
    var album_name = document.getElementById('album-name')


    // AJAX upload of multiple files
    form.onsubmit = function(event) {
        event.preventDefault();
        uploadButton.innerHTML = "Uploading...";
        var images = imageSelect.files;

        // List of allowed MIME types
        var allowedImageTypes = ['image/jpeg'];

        // Load each of the images into formData
        var formData = new FormData();
        for (var i = 0; i < images.length; i++) {
            var image = images[i]

            // Check that images are of allowed type(s)
            if (allowedImageTypes.indexOf(image.type) > -1) {
                // Load image into AJAX payload
                formData.append('image_list', image, image.name);
            } else {                
                // Add some error feedback here, for now, just exclude these images
                continue;
            }

        }

        // Load album name into AJAX payload
        formData.append('album_name', album_name.value)

        // Setup AJAX request object
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '', true);
        xhr.setRequestHeader("X-CSRFToken", csrftoken)

        // Set event handler for when the request is completed successfully
        xhr.onload = function () {
            if (xhr.status === 200) {
                // Files uploaded, do more visual feedback here
                uploadButton.innerHTML = 'Uploaded!';
            } else {
                alert("An error occurred with the file upload!");
                uploadButton.innerHTML = 'Error!';
            }
        };

        // Send the images!
        xhr.send(formData)

        // TODO: Get response (JSON?) then display success or errors.
    };
});