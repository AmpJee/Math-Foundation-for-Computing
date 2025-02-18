import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import sys

def solve_sle_interpolation(x_points, y_points):
    degree = len(x_points) - 1
    A = np.vander(x_points, degree + 1)
    coefs = np.linalg.solve(A, y_points)
    return np.poly1d(coefs)

def lagrange_interpolation(x, y, x_values):
    m = len(x)
    y_values = np.zeros(len(x_values))
    for i in range(m):
        l = np.ones(len(x_values))
        for j in range(m):
            if i != j:
                l *= (x_values - x[j]) / (x[i] - x[j])
        y_values += y[i] * l
    return y_values

def parametric_interpolation(x_points, y_points):
    t = np.linspace(0, 1, len(x_points))
    poly_x = np.poly1d(np.polyfit(t, x_points, len(x_points) - 1))
    poly_y = np.poly1d(np.polyfit(t, y_points, len(y_points) - 1))
    return poly_x, poly_y

def plot_interpolation(x_values, y_values, polynomials, methods):
    x_plot = np.linspace(min(x_values), max(x_values), 1000)
    plt.scatter(x_values, y_values, color='red', label='Data Points')
    
    for method in methods:
        if method == 'SLE':
            y_plot = np.polyval(polynomials['SLE'], x_plot)
            plt.plot(x_plot, y_plot, label='SLE Interpolation')
        if method == 'Lagrange':
            y_plot = lagrange_interpolation(x_values, y_values, x_plot)
            plt.plot(x_plot, y_plot, label='Lagrange Interpolation')
        if method == 'Parametric':
            t_plot = np.linspace(0, 1, 1000)
            x_interp = np.polyval(polynomials['Parametric']["x"], t_plot)
            y_interp = np.polyval(polynomials['Parametric']["y"], t_plot)
            plt.plot(x_interp, y_interp, label='Parametric Interpolation')
    
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolation Polynomials")
    plt.show()

def main():
    choice = input("Enter '1' to input a function or '2' to upload a file with points: ")
    
    if choice == '1':
        func_expr = input("Enter a function (e.g., x*sin(x) - x^2 + 1): ")
        a, b = map(float, input("Enter interval (start, end): ").split())
        degree = int(input("Enter polynomial degree: "))
        x_values = np.linspace(a, b, degree + 1)
        func = sp.lambdify(sp.Symbol('x'), sp.sympify(func_expr))
        y_values = func(x_values)
    elif choice == '2':
        filename = input("Enter filename: ")
        data = np.loadtxt(filename, delimiter=',')
        x_values, y_values = data[:, 0], data[:, 1]
    else:
        print("Invalid input.")
        sys.exit(1)
    
    methods = input("Select methods (SLE, Lagrange, Parametric) separated by space: ").split()
    polynomials = {}
    
    if 'SLE' in methods:
        polynomials['SLE'] = solve_sle_interpolation(x_values, y_values)
    if 'Lagrange' in methods:
        polynomials['Lagrange'] = y_values
    if 'Parametric' in methods:
        poly_x, poly_y = parametric_interpolation(x_values, y_values)
        polynomials['Parametric'] = {'x': poly_x, 'y': poly_y}
    
    plot_interpolation(x_values, y_values, polynomials, methods)
    
    while True:
        try:
            eval_point = float(input("Enter a point to evaluate or 'q' to quit: "))
            for method in methods:
                if method == 'SLE':
                    print(f"SLE({eval_point}) = {np.polyval(polynomials['SLE'], eval_point)}")
                if method == 'Lagrange':
                    print(f"Lagrange({eval_point}) = {lagrange_interpolation(x_values, y_values, np.array([eval_point]))[0]}")
                if method == 'Parametric':
                    print(f"Parametric x({eval_point}) = {np.polyval(polynomials['Parametric']['x'], eval_point)}, y({eval_point}) = {np.polyval(polynomials['Parametric']['y'], eval_point)}")
        except ValueError:
            break

if __name__ == "__main__":
    main()
