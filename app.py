from flask import Flask, render_template, request, jsonify
import numpy as np
import logging

app = Flask(__name__, static_url_path='/static')

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG or INFO
logger = logging.getLogger(__name__)  # Create a logger object for your app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        operation = request.form.get('operation')

        # Define the list of expected operation values
        expected_operations = ['add', 'subtract', 'multiply', 'determinant']

        # Check if the operation is one of the expected values
        if operation in expected_operations:
            matrix1 = []
            matrix2 = []

            # Helper function to convert input to float with error handling
            def convert_to_float(value):
                try:
                    return float(value)
                except ValueError:
                    # Handle the case where the input cannot be converted to a float
                    logger.error("Invalid numeric input: %s", str(value))
                    return None  # Return None for invalid input

            # Convert matrix1 elements to floats with error handling
            for i in range(3):
                row = [convert_to_float(request.form.get(f'matrix1_{i}_{j}')) for j in range(3)]
                matrix1.append(row)

            # Convert matrix2 elements to floats with error handling
            for i in range(3):
                row = [convert_to_float(request.form.get(f'matrix2_{i}_{j}')) for j in range(3)]
                matrix2.append(row)

            # Check for None values in matrices and handle them
            if any(None in row for row in matrix1) or any(None in row for row in matrix2):
                return jsonify(error="Invalid numeric input in matrices. Please provide valid numbers."), 400

            # Perform matrix operation based on the selected operation
            if operation == 'add':
                result = np.add(matrix1, matrix2)
            elif operation == 'subtract':
                result = np.subtract(matrix1, matrix2)
            elif operation == 'multiply':
                result = np.dot(matrix1, matrix2)
            elif operation == 'determinant':
                if len(matrix1) == 2:
                    result = np.linalg.det(matrix1)
                elif len(matrix1) == 3:
                    result = np.linalg.det(matrix1)
                else:
                    return jsonify(error="Unsupported matrix size. Please provide a 2x2 or 3x3 matrix."), 400
            else:
                result = None

            return jsonify(result=result)
        else:
            # The operation is not valid; handle the error
            error_message = "Invalid operation parameter. Expected one of: 'add', 'subtract', 'multiply', 'determinant'."
            return jsonify(error=error_message), 400  # Return a 400 Bad Request status code

    except Exception as e:
        # Log the exception with details
        logger.exception("An error occurred while processing the request: %s", str(e))
        return jsonify(error="An internal server error occurred."), 500  # Return a 500 Internal Server Error response

if __name__ == '__main__':
    app.run(debug=True)
