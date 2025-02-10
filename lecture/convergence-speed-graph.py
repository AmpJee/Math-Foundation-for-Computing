import matplotlib.pyplot as plt

def f(x):
    return x*x - 4

def f_prime(x):
    return 2*x

def g(x):
    return -1/4 * f(x) + x

def bisection_method(a,b, eps = 1e-20, iterations = 100):
    x_values = []
    for _ in range(iterations):
        # print(x)
        xnew = (a + b)/2
        if abs(f(xnew)) < eps:
            break
        if f(xnew) * f(a) < 0:
            b = xnew
        else:
            a = xnew
        x = xnew
        x_values.append(x)
    return x_values

def fixed_point_method(x, eps = 1e-20, iterations = 100):
    x_values = []
    for i in range(iterations):
        xnew = g(x)
        if abs(x - xnew) < eps:
            break
        x = xnew
        x_values.append(x)
    return x_values

def newton_method(x , eps = 1e-20 , iterations = 100):
    x_values = []
    for i in range(iterations):
        xnew = x - f(x)/f_prime(x)
        if abs(x - xnew) < eps:
            break
        x = xnew
        x_values.append(x)
    return x_values

def main():
    global x, eps, alpha, real_root
    x = 4
    a = -2
    b = 5
    eps = 1e-6
    alpha = 0.5
    real_root = 2.0
    bisection_values = bisection_method(a, b)
    fixed_point_values = fixed_point_method(x)
    newton_values = newton_method(x)
    # print(bisection_values)

    def calculate_error(values):
        return [abs(real_root - value) for value in values]
    
    bisection_error = calculate_error(bisection_values)
    fixed_point_error = calculate_error(fixed_point_values)
    newton_error = calculate_error(newton_values)

    plt.plot(bisection_error, label='Bisection Method')
    plt.plot(fixed_point_error, label='Fixed Point Method')
    plt.plot(newton_error, label='Newton Method')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Convergence Speed Graph')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

