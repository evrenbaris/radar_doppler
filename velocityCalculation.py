import numpy as np

# Constants
c = 3e8  # Speed of light (m/s)
frequency = 10e9  # Radar frequency (10 GHz)

# Target velocities (m/s)
velocities = [50, 100, 150]  # Example target velocities

# Calculate doppler shifts for each target
doppler_shifts = [(2 * v * frequency) / c for v in velocities]

# Print results
for i, shift in enumerate(doppler_shifts):
    print(f"Target {i + 1}: Doppler Shift = {shift:.2f} Hz, Velocity = {velocities[i]} m/s")
