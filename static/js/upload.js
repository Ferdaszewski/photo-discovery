// var uploader = new plupload.Uploader({
//     runtimes: "html5, flash, silverlight, html4",
//     browse_button: "pickfiles",
//     container: "uploader",
//     url: "/",

//     filters: {
//         max_file_size: "10mb",
//         mime_types: [
//             {title: "Image files", extensions: "jpg,jpeg"}
//         ]
//     },

//     // Flash settings
//     flash_swf_url: "/static/plupload/js/Moxie.swf",

//     // Silverlight settings
//     silverlight_xap_url: "/static/plupload/js/Moxie.xap",

//     init: {
//         PostInit: function() {
//             document.getElementById("filelist").innerHTML = "";

//             document.getElementById("upload-button").onclick = function(event) {
//                 uploader.start();
//                 return false;
//             };
//         },

//         FilesAdded: function(up, files) {
//             plupload.each(files, function(file) {
//                 document.getElementById("filelist").innerHTML += '<div id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ') <b></b></div>';
//             });
//         },

//         UploadProgress: function(up, file) {
//             document.getElementById(file.id).getElementsByTagName("b")[0].innerHTML = '<span>' + file.percent + '%</span>';
//         },

//         Error: function(up, err) {
//             document.getElementById("error_display").appendChild(document.createTextNode("\nError #" + err.code + ": " + err.message));
//         }
//     }
// });

// uploader.init();

// Custom example logic

