import numpy as np
import matplotlib.pyplot as plt

# Define N1 and set the values for N in all three cases
N1 = 2
N_a = 4 * N1 + 1  # Case (a)
N_b = 8 * N1 + 1  # Case (b)
N_c = 10 * N1 + 1  # Case (c)

# Create arrays to store results for all three cases
x_a = np.zeros(2 * N_a + 1)
x_b = np.zeros(2 * N_b + 1)
x_c = np.zeros(2 * N_c + 1)

# Define the functions
def func_x(t):
    return (t >= -2) & (t <= 2)

def fourier(t, N):
    return np.sum(np.exp(-1j * t * 2 * np.pi * np.arange(-2, 3) / N)) / N

# Calculate x values for all three cases
for t in range(-N_a, N_a + 1):
    x_a[t + N_a] = func_x(t)

for t in range(-N_b, N_b + 1):
    x_b[t + N_b] = func_x(t)

for t in range(-N_c, N_c + 1):
    x_c[t + N_c] = func_x(t)

# Calculate Fourier series coefficients for all three cases
ak_a = np.zeros(N_a, dtype=complex)
ak_b = np.zeros(N_b, dtype=complex)
ak_c = np.zeros(N_c, dtype=complex)

for k in range(1, N_a + 1):
    ak_a[k - 1] = fourier(k, N_a)

for k in range(1, N_b + 1):
    ak_b[k - 1] = fourier(k, N_b)

for k in range(1, N_c + 1):
    ak_c[k - 1] = fourier(k, N_c)

# Plot the signals and Fourier series for all three cases
plt.figure(figsize=(12, 12))

# Case (a)
plt.subplot(3, 2, 1)
plt.stem(range(-N_a, N_a + 1), x_a, 'b', markerfmt='bo', linefmt='-b', basefmt=' ')
plt.title('x[n] for N = 4N1 + 1')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(range(1, N_a + 1), np.real(ak_a), 'r', markerfmt='ro', linefmt='-r', basefmt=' ')
plt.title('Fourier series for N = 4N1 + 1')
plt.xlabel('k')
plt.ylabel('Re(ak)')
plt.grid(True)

# Case (b)
plt.subplot(3, 2, 3)
plt.stem(range(-N_b, N_b + 1), x_b, 'b', markerfmt='bo', linefmt='-b', basefmt=' ')
plt.title('x[n] for N = 8N1 + 1')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(range(1, N_b + 1), np.real(ak_b), 'r', markerfmt='ro', linefmt='-r', basefmt=' ')
plt.title('Fourier series for N = 8N1 + 1')
plt.xlabel('k')
plt.ylabel('Re(ak)')
plt.grid(True)

# Case (c)
plt.subplot(3, 2, 5)
plt.stem(range(-N_c, N_c + 1), x_c, 'b', markerfmt='bo', linefmt='-b', basefmt=' ')
plt.title('x[n] for N = 10N1 + 1')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(3, 2, 6)
plt.stem(range(1, N_c + 1), np.real(ak_c), 'r', markerfmt='ro', linefmt='-r', basefmt=' ')
plt.title('Fourier series for N = 10N1 + 1')
plt.xlabel('k')
plt.ylabel('Re(ak)')
plt.grid(True)

plt.suptitle('Signal x[n] and its Fourier Series for Different N')
plt.tight_layout()
plt.show()
