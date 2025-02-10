import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import Flask, render_template, request
import sympy as sp
import io
import base64

app = Flask(__name__)

def bisection_method(a,b, eps = 1e-20, iterations = 1000):
    x_values = []
    for _ in range(iterations):
        # print(x)
        xnew = (a + b)/2
        x_values.append(xnew)
        if abs(f(xnew)) < eps:
            break
        if f(xnew) * f(a) < 0:
            b = xnew
        else:
            a = xnew
        x = xnew
    return x_values

# def fixed_point_method(x, eps = 1e-20, iterations = 100):
#     x_values = []
#     for i in range(iterations):
#         xnew = g(x)
#         if abs(x - xnew) < eps:
#             break
#         x = xnew
#         x_values.append(x)
#     return x_values

def newton_method(x , eps = 1e-20 , iterations = 100):
    x_values = []
    for i in range(iterations):
        xnew = x - f(x)/f_prime(x)
        if abs(x - xnew) < eps:
            break
        x = xnew
        x_values.append(x)
    return x_values

def calculate_error(values, real_root):
    return [abs(value - real_root) for value in values]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func_input = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        eps = float(request.form['eps'])

        x = sp.symbols('x')
        func = sp.sympify(func_input)
        real_root = sp.nsolve(func, x, 0)
        initial_guess = 5
        global f, f_prime
        f = lambda x: func.evalf(subs={sp.Symbol('x'): x})
        f_prime = lambda x: func.diff().evalf(subs={sp.Symbol('x'): x})

        bisection_values = bisection_method(a, b, eps)
        newton_values = newton_method(initial_guess, eps)

        bisection_errors = calculate_error(bisection_values, float(real_root))
        newton_errors = calculate_error(newton_values, float(real_root))

        plt.figure(figsize=(10, 6))
        plt.semilogy(range(len(bisection_errors)), bisection_errors, 'b-', label='Bisection')
        plt.semilogy(range(len(newton_errors)), newton_errors, 'r-', label='Newton')
        plt.xlabel('Iteration')
        plt.ylabel('Error')
        plt.legend()
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.title('Convergence Comparison')
        plt.tight_layout()
        buf.seek(0)
        img_data = base64.b64encode(buf.getvalue()).decode()
        plt.close()

        return render_template('index.html', 
                     bisection_root=bisection_values[-1],
                     newton_root=newton_values[-1],
                     bisection_iterations=len(bisection_values),
                     newton_iterations=len(newton_values),
                     img_data=img_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)