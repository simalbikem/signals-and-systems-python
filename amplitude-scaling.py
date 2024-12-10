import numpy as np
import matplotlib.pyplot as plt

# Define the n values and corresponding x[n] values
n_values = np.array([-6, -4, 0, 2, 4])  
x_values = np.array([2, 2, 2, 2, -2])

n_range = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7])

# Initialize x[n] as 0 for all n
x_n = np.zeros(n_range.shape)

# Assign the values of x[n] where n is in the defined set
for n, x in zip(n_values, x_values):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        x_n[idx[0]] = x

# Apply amplitude scaling (A = 2)
A = 2
y_values = np.array([A * val for val in x_values])  # Scale the original x_values by A

# Plot the original and scaled signals
plt.stem(n_range, x_n, basefmt=" ", linefmt="b-", markerfmt="bo", label="Orijinal x[n]")
plt.stem(n_values, y_values, basefmt=" ", linefmt="r-", markerfmt="ro", label=f"Genlik-Ölçeklendirme y[n] (A={A})")
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title(f'Genlik-Ölçeklendirilmiş Ayrık-Zaman Sinyali')
plt.grid(True)
plt.legend()
plt.show()