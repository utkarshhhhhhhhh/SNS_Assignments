import numpy as np
import matplotlib.pyplot as plt

# Define the time axis for continuous signal
t_continuous = np.arange(0, 18.001, 0.001)  # Adjust the time step as needed for continuous signal

# Define the period of the signal
T = 6

# Create a continuous signal x(t) that repeats three times within the range from 0 to 18
x_continuous = np.mod(t_continuous, T)

# Plot the continuous signal x(t) for three periods (0 to 18)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t_continuous, x_continuous, 'b', linewidth=2)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Continuous Signal x(t) with 3 Periodic Repetitions (0 to 18)')
plt.grid(True)
plt.show()
