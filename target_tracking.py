import matplotlib.pyplot as plt

# Time array
time = np.linspace(0, 1e-3, 1000)  # 1 ms

# Simulate reflected signals with Doppler effect
reflected_signals = [np.sin(2 * np.pi * (frequency + shift) * time) for shift in doppler_shifts]

# Combine signals
combined_signal = np.sum(reflected_signals, axis=0)

# Plot combined signal
plt.figure(figsize=(10, 6))
plt.plot(time, combined_signal, label="Combined Signal")
plt.title("Reflected Signals with Doppler Effect")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
