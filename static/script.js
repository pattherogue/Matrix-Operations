document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('matrix-form');
    const resultDiv = document.getElementById('result');

    // Check if the loading element exists in the DOM
    const loadingDiv = document.getElementById('loading');
    if (!loadingDiv) {
        console.error('Loading element not found in the DOM.');
        return;
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        resultDiv.innerHTML = ''; // Clear previous results
        loadingDiv.style.display = 'block'; // Show loading message

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

        formData.append('operation', operation);
        
        // Send data to the server for calculation and display the result
        fetch('/calculate', {
            method: 'POST',
            body: formData, // Use formData here
        })

        .then(response => response.json())
        .then(data => {
            if (loadingDiv) {
                loadingDiv.style.display = 'none'; // Hide loading message
            }

            if (data.result !== undefined) {
                resultDiv.textContent = `Result: ${data.result}`;
            } else if (data.error) {
                resultDiv.textContent = `Error: ${data.error}`;
            } else {
                resultDiv.textContent = 'Invalid input or operation.';
            }
        })
        .catch(error => {
            if (loadingDiv) {
                loadingDiv.style.display = 'none'; // Hide loading message
            }
            resultDiv.textContent = 'Error occurred during calculation.';
        });
    });
});
