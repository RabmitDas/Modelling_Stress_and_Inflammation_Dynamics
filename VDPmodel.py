import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

# Given Metabolite Data
time_points = np.array([t1, t2, t3])  # time points
pro_stress = np.array([p1, p2, p3]) # pro stress values corresponding to each timepoint in that condition
anti_stress = np.array([a1, a2, a3]) # anti stress values corresponding to each timepoint in that condition

# Normalize the data
def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

pro_norm = normalize(pro_inflammatory)
anti_norm = normalize(anti_inflammatory)

# Rescale to [-1, 1]
x_scaled = 2 * pro_norm - 1
y_scaled = 2 * anti_norm - 1

# Define Van der Pol Model
def van_der_pol(t, z, mu):
    x, y = z
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return [dxdt, dydt]

# Loss Function to Optimize μ (Minimize MSE)
def objective(mu_array):
    mu = mu_array[0]  # Extract scalar from array
    solution = solve_ivp(van_der_pol, (0, 12), [x_scaled[0], y_scaled[0]], args=(mu,), t_eval=time_points)

    if not solution.success:
        return np.inf  # Return a large error if integration fails

    x_sim, y_sim = solution.y[0], solution.y[1]
    mse_x = np.mean((x_sim - x_scaled) ** 2)
    mse_y = np.mean((y_sim - y_scaled) ** 2)
    return mse_x + mse_y  # Total MSE

# Optimize μ using scipy's minimize()
mu_initial_guess = 1.0  # Start with μ = 1.0
result = minimize(objective, mu_initial_guess, method='Nelder-Mead')
optimal_mu = result.x[0]

print(f"Optimal μ: {optimal_mu:.4f}")

# Solve system with optimal μ
t_eval = np.linspace(0, 12, 1000)
solution_opt = solve_ivp(van_der_pol, (0, 12), [x_scaled[0], y_scaled[0]], args=(optimal_mu,), t_eval=t_eval)
x_sim_opt, y_sim_opt = solution_opt.y

# Plot Optimized Model vs. Metabolite Data
plt.figure(figsize=(8, 6))
plt.plot(x_sim_opt, y_sim_opt, label=f"μ={optimal_mu:.2f}", color="blue")
plt.scatter(x_scaled, y_scaled, color="red", label="Observed Metabolite Data", zorder=3, s=80, edgecolors="black")
# Label each observed point with its corresponding time point
for i, txt in enumerate(time_points):
    plt.annotate(f"{txt}w", (x_scaled[i], y_scaled[i]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=10, color="black")

plt.xlabel("Pro-stress(Scaled)")
plt.ylabel("Anti-stress(Scaled)")
plt.title("Condition")
plt.legend()
plt.grid()
plt.show()
