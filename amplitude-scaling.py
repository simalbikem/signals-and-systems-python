import numpy as np
import matplotlib.pyplot as plt

# Define the n values and corresponding x[n] values
n_values = np.array([4, -3, -1, 0, 2])
x_values = np.array([-1, 1, 1, 1, 1])

# Define the n_range as per your request (4, 3, 2, 1, 0, -1, -2)
n_range = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

# Initialize x[n] as 0 for all n
x_n = np.zeros(n_range.shape)

# Assign the values of x[n] where n is in the defined set
for n, x in zip(n_values, x_values):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        x_n[idx[0]] = x

# Apply amplitude scaling (A = 2)
A = 2
y_values = np.array([-A, A, A, A, A])  # Scaled values for the original non-zero points

# Plot the original and scaled signals
plt.stem(n_range, x_n, basefmt=" ", linefmt="b-", markerfmt="bo", label="Original x[n]")
plt.stem(n_values, y_values, basefmt=" ", linefmt="r-", markerfmt="ro", label=f"Amplitude-Scaling y[n] (A={A})")
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title(f'Amplitude-Scaled Discrete-Time Signal')
plt.grid(True)
plt.legend()
plt.show()