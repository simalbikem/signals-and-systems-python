import numpy as np
import matplotlib.pyplot as plt

# Define the first signal y[n] after amplitude scaling (A = 2)
n_values_1 = np.array([-6, -4, 0, 2, 4])  
y_values_1 = np.array([2, 2, 2, 2, -2])

# Define the second signal y[n] after time scaling (stretching by factor k = 2)
n_values_2 = np.array([-3, -2, 0, 1, 2])  
y_values_2 = np.array([2, 2, 2, 2, -2])  

# Define a range of n for visualization (extended to cover both signals)
n_range = np.array([5,  4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7])

# Initialize y[n] as 0 for both functions
y_n_1 = np.zeros(n_range.shape)
y_n_2 = np.zeros(n_range.shape)

# Assign the values of y[n] for the amplitude-scaled signal
for n, y in zip(n_values_1, y_values_1):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        y_n_1[idx[0]] = y

# Assign the values of y[n] for the time-scaled signal
for n, y in zip(n_values_2, y_values_2):
    idx = np.where(n_range == n)[0]
    if len(idx) > 0:
        y_n_2[idx[0]] = y

# Plot both signals on the same graph
plt.stem(n_range, y_n_1, basefmt=" ", linefmt='r-', markerfmt='ro', label="Genlik-Ölçeklendirme (A=2)")
plt.stem(n_range, y_n_2, basefmt=" ", linefmt='purple', markerfmt='^', label="Zamanda-Germe (k=2)")
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Zaman-Ölçeklendirme (Germe) Genlik-Ölçeklendirmenin Ardından')
plt.grid(True)
plt.legend()
plt.show()