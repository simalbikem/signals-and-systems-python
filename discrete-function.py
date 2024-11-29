import numpy as np
import matplotlib.pyplot as plt

# Define the n values and corresponding x[n] values
n_values = np.array([4, -3, -1, 0, 2])  # The specific n values
x_values = np.array([-1, 1, 1, 1, 1])   # The corresponding x[n] values

# Define the n_range as per your request (4, 3, 2, 1, 0, -1, -2)
n_range = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

# Initialize x[n] as 0 for all n
x_n = np.zeros(n_range.shape)

# Assign the values of x[n] where n is in the defined set
for n, x in zip(n_values, x_values):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        x_n[idx[0]] = x

# Plot the sequence
plt.stem(n_range, x_n, basefmt=" ")  # Removed 'use_line_collection'
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete-Time Signal x[n]')
plt.grid(True)
plt.show()