from flask import Flask, render_template, request, jsonify
import numpy as np
from matrix_operations import add_matrices, subtract_matrices, multiply_matrices, find_determinant

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    matrix1 = []
    matrix2 = []

    # Helper function to convert input to float with error handling
    def convert_to_float(value):
        if value is not None:
            try:
                return float(value)
            except ValueError:
                # Handle the case where the input cannot be converted to a float
                print(f"Invalid numeric input: {value}")
        return 0.0  # Provide a default value or handle it as needed

    # Convert matrix1 elements to floats with error handling
    for i in range(3):
        row = [convert_to_float(request.form.get(f'matrix1_{i}_{j}')) for j in range(3)]
        matrix1.append(row)

    # Convert matrix2 elements to floats with error handling
    for i in range(3):
        row = [convert_to_float(request.form.get(f'matrix2_{i}_{j}')) for j in range(3)]
        matrix2.append(row)

    if operation == 'add':
        result = add_matrices(matrix1, matrix2)
    elif operation == 'subtract':
        result = subtract_matrices(matrix1, matrix2)
    elif operation == 'multiply':
        result = multiply_matrices(matrix1, matrix2)
    elif operation == 'determinant':
        result = find_determinant(matrix1)
    else:
        result = None

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
