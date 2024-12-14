const colorButtons = document.querySelectorAll(".color-btn");

colorButtons.forEach(button => {
    button.addEventListener('click', () => {
        const oldColor = button.style.backgroundColor;
        fetch("http://127.0.0.1:8000/random-colour")
            .then(response => response.json())
            .then(data => {
                button.style.backgroundColor = data.colour;
                return fetch("http://127.0.0.1:8000/get-colour", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({colour: oldColor})
                });
            })
            .then(response => response.json());
    });
});
