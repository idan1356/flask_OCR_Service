// Get references to HTML elements
const imageInput = document.getElementById('user_image');
const textArea = document.getElementById('text_area');
const imageElement = document.getElementById('image');

// Add an event listener to the image input
imageInput.addEventListener('change', () => {
    const selectedFile = imageInput.files[0];
    imageElement.src = URL.createObjectURL(selectedFile);
    textArea.value = null
    if (selectedFile) {
        const formData = new FormData();
        formData.append('user_image', selectedFile);

        fetch('/api/decipher-text?get_processed_image=true', {method: 'POST', body: formData})
        .then(response => response.json())
        .then(data => {
            textArea.value = data["reader_data"].map(item => item[1]).join(', ');
            imageElement.src = "data:content/jpeg;base64," + data["base64_processed_image_content"];
        })
        .catch(error => {
            console.error('Error:', error);
            imageElement.src = null
        });
    }
});
