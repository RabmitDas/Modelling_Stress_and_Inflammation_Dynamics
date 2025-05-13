import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def model(params, x, y):
    a, b, c, d = params
    return a * np.log(y) - b * y + c * np.log(x) - d * x

def residuals(params, points):
    return [model(params, x, y) for x, y in points]

def solve_coefficients(points):
    if len(points) < 3:
        raise ValueError("At least 3 points are required to fit a, b, c, and d.")
    
    initial_guess = np.ones(4)  # Initial guess for a, b, c, d
    bounds = (np.zeros(4), np.inf)  # Enforce positivity constraints
    result = least_squares(residuals, initial_guess, args=(points,), bounds=bounds)
    
    if result.success:
        return {"a": result.x[0], "b": result.x[1], "c": result.x[2], "d": result.x[3]}
    else:
        raise RuntimeError("Optimization failed to converge.")

# Example usage
points = [(p1, a1), (p2, a2), (p3, a3)]  # Replace with actual (pro-stress, anti-stress) values for different time points in a condition
coefficients = solve_coefficients(points)
[a,b,c,d] = coefficients

def phase(x,y, a = a, b=b, c=c, d=d):
    dx = a*x - b*x*y
    dy = -c*y + d*x*y
    return dx, dy
# Example vector field data
X, Y = np.meshgrid(np.linspace(-100, 15000, 30), np.linspace(-100, 15000, 30))
X_dot, Y_dot = phase(x=X, y=Y)
x = c/d
y = a/b

# Creating a stream plot
plt.figure()
stream = plt.streamplot(X, Y, X_dot, Y_dot, color='gray')
plt.scatter(x, y, c="black")
plt.text(x+0.13, y - 0.05, "({:.4f}, {:.4f})".format(x, y), ha='center')
plt.xlabel('Pro-stress')
plt.ylabel('Anti-stess')
plt.title('Condition')
plt.show()
