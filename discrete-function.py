import numpy as np
import matplotlib.pyplot as plt

# Define the n values and corresponding x[n] values
n_values = np.array([-6, -4, 0, 2, 4])  
x_values = np.array([1, 1, 1, 1, -1])   

n_range = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7])

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