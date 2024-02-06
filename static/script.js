document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('matrix-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        resultDiv.innerHTML = ''; // Clear previous results

        const formData = new FormData(form);
        const operation = formData.get('operation');
        const data = {};

        for (let i = 0; i < 3; i++) {
            data[`matrix1_${i}`] = [];
            data[`matrix2_${i}`] = [];
            for (let j = 0; j < 3; j++) {
                data[`matrix1_${i}`][j] = parseFloat(formData.get(`matrix1_${i}_${j}`));
                data[`matrix2_${i}`][j] = parseFloat(formData.get(`matrix2_${i}_${j}`));
            }
        }

        // Send data to the server for calculation and display the result
        fetch('/calculate', {
            method: 'POST',
            body: JSON.stringify({ operation, data }),
            headers: { 'Content-Type': 'application/json' },
        })
        .then(response => response.json())
        .then(data => {
            if (data.result !== undefined) {
                resultDiv.textContent = `Result: ${data.result}`;
            } else {
                resultDiv.textContent = 'Invalid input or operation.';
            }
        })
        .catch(error => {
            resultDiv.textContent = 'Error occurred during calculation.';
        });
    });
});
