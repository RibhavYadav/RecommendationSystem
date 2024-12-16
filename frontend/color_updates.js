const colorButtons = document.querySelectorAll(".color-btn");

colorButtons.forEach(button => {
    button.addEventListener('click', () => {
        const curr_colour = button.style.backgroundColor;
        fetch("http://127.0.0.1:8000/get-colour", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({colour: curr_colour})
        })
        .then(response => response.json())
        .then(() => {
            colorButtons.forEach(btn => {
                fetch("http://127.0.0.1:8000/random-colour")
                    .then(response => response.json())
                    .then(data => {
                        btn.style.backgroundColor = data.colour;
                    });
            });
        });
    });
});
