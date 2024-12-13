const colorButtons = document.querySelectorAll(".color-btn");

colorButtons.forEach(button => {
    button.addEventListener('click', () => {
        fetch("http://127.0.0.1:8000/random-colour")
            .then(response => response.json())
            .then(data => {
                button.style.backgroundColor = data.colour;
            })
    });
});
