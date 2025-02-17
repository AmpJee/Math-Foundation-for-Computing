import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

def lagrange_interpolation(x, y, x_values):
    m = len(x)
    y_values = np.zeros(len(x_values))
    for i in range(m):
        l = 1
        for j in range(m):
            if i != j:
                l *= (x_values - x[j]) / (x[i] - x[j])
        y_values += y[i] * l
    return y_values

def polynomial_interpolation(x, y, x_values):
    V = np.vander(x, len(x))
    coeffs = np.linalg.solve(V, y)
    return np.polyval(coeffs, x_values)

def parametric_interpolation(x_points, y_points):
    t = np.linspace(0, 1, len(x_points))
    poly_x = np.poly1d(np.polyfit(t, x_points, len(x_points) - 1))
    poly_y = np.poly1d(np.polyfit(t, y_points, len(y_points) - 1))
    return poly_x, poly_y

def plot_interpolation(func_input, a, b, n, method):
    x = sp.symbols('x')
    function = sp.sympify(func_input)

    x_points = np.linspace(a, b, n)
    y_points = [function.subs(x, i) for i in x_points]

    x_values = np.linspace(a, b, 100)
    if method == 'Lagrange':
        y_values = lagrange_interpolation(x_points, y_points, x_values)
    elif method == 'SLE':
        y_values = polynomial_interpolation(x_points, y_points, x_values)
    elif method == 'Parametric':
        poly_x, poly_y = parametric_interpolation(x_points, y_points)
        y_values = poly_y(poly_x(x_values))

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label='Interpolation')
    plt.plot(x_values, [function.subs(x, i) for i in x_values], label='True Function')
    plt.scatter(x_points, y_points, color='black', label='Interpolation Points')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolation Example')
    plt.show()
    plt.savefig('static/plot.png')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'post':
        func_input = request.form['function']
        a = int(request,form['a'])
        b = int(request,form['b'])
        n = int(request,form['n'])
        method = request.form['method']
        plot_interpolation(func_input, a, b, n, method)
        return render_template('index.html', plot='plot.png')
    return render_template('index.html')

