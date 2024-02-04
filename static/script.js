// function previewImage(event) {
//     var input = event.target;
//     var preview = document.getElementById('image-preview');

//     var reader = new FileReader();
//     reader.onload = function() {
//         preview.src = reader.result;
//     };

//     if (input.files && input.files[0]) {
//         reader.readAsDataURL(input.files[0]);
//     }
// }

   function previewImage(event) {
    var input = event.target;
    var preview = document.getElementById('image-preview');
    var selectedFileName = document.getElementById('selected-file-name');

    var reader = new FileReader();
    reader.onload = function() {
        preview.src = reader.result;
    };

    if (input.files && input.files[0]) {
        reader.readAsDataURL(input.files[0]);
        selectedFileName.textContent = "Selected file: " + input.files[0].name;
    } else {
        selectedFileName.textContent = "Select the Image";
    }
}

// send data to the backend 

function encode() {
    // Get form data
    var image = getElementById('image-preview')
    var user_text = getElementById('user_text')
    var pass = getElementById('pass')

    var formData = new FormData();
    formData.append('input_filename', image.files[0]);
    formData.append('data', user_text.value);
    formData.append('secret_key', pass.value)

    // Send AJAX request
    $.ajax({
        url: '/hide',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            // Handle success response
            // console.log(response);
            console.log("done....")
        },
        error: function(error) {
            // Handle error response
            console.error(error);
        }
    });
}


