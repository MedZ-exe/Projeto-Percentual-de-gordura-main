window.addEventListener('DOMContentLoaded', (event) => {
    const fileUpload = document.getElementById('file-upload');
    const imagePreview = document.getElementById('image-preview');

    // Função para exibir a imagem no preview
    function displayImage(image) {
        imagePreview.innerHTML = '';
        imagePreview.appendChild(image);
    }

    // Evento de upload de arquivo
    fileUpload.addEventListener('change', (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            const image = document.createElement('img');
            image.src = e.target.result;

            displayImage(image);
        }

        reader.readAsDataURL(file);
    });
});
