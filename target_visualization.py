# Target positions over time
positions = [[v * t for t in time] for v in velocities]

# Plot target movements
plt.figure(figsize=(10, 6))
for i, pos in enumerate(positions):
    plt.plot(time, pos, label=f"Target {i + 1}")
plt.title("Target Movements Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid()
plt.legend()
plt.show()
