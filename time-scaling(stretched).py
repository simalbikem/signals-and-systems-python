import numpy as np
import matplotlib.pyplot as plt

# Define the first signal y[n] after amplitude scaling (A = 2)
n_values_1 = np.array([4, -3, -1, 0, 2])
y_values_1 = np.array([-2, 2, 2, 2, 2])

# Define the second signal y[n] after time scaling (stretching by factor k = 2)
n_values_2 = np.array([2, -1.5, -0.5, 0, 1])  # Corrected values after stretching
y_values_2 = np.array([-2, 2, 2, 2, 2])

# Define a range of n for visualization
n_range = np.array([4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2, -2.5, -3, -3.5])

# Initialize y[n] as 0 for both functions
y_n_1 = np.zeros(n_range.shape)
y_n_2 = np.zeros(n_range.shape)

# Assign the values of y[n] for both signals (Amplitude-scaled and Time-scaled)
for n, y in zip(n_values_1, y_values_1):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        y_n_1[idx[0]] = y

for n, y in zip(n_values_2, y_values_2):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        y_n_2[idx[0]] = y

# Plot both signals on the same graph
plt.stem(n_range, y_n_1, basefmt=" ", linefmt='r-', markerfmt='ro', label="Amplitude-Scaling (by A=2)")
plt.stem(n_range, y_n_2, basefmt=" ", linefmt='purple', markerfmt='o', label="Stretching (by factor k=2)")  # Pink color
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Time-Scaling (Stretching) After Amplitude-Scaling')
plt.grid(True)
plt.legend()
plt.show()
