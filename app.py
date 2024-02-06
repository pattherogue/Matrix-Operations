from flask import Flask, render_template, request, jsonify
import numpy as np
from matrix_operations import add_matrices, subtract_matrices, multiply_matrices, find_determinant


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    matrix1 = [[float(request.form.get(f'matrix1_{i}_{j}')) for j in range(3)] for i in range(3)]
    matrix2 = [[float(request.form.get(f'matrix2_{i}_{j}')) for j in range(3)] for i in range(3)]

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
