import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1337)


def init_grid(size):
    return 2 * rng.integers(2, size=(size, size)) - 1


def wolff_algorithm(grid, temperature):
    L = len(grid)
    i, j = rng.integers(0, L, size=2)

    cluster = {(i, j)}
    to_flip = {(i, j)}

    while to_flip:
        i, j = to_flip.pop()
        neighbors = [
            ((i + 1) % L, j),
            ((i - 1) % L, j),
            (i, (j + 1) % L),
            (i, (j - 1) % L),
        ]

        for neighbor in neighbors:
            if (
                neighbor not in cluster
                and grid[neighbor] == grid[i, j]
                and rng.random() < 1 - np.exp(-2 / temperature)
            ):
                to_flip.add(neighbor)
                cluster.add(neighbor)

    for i, j in cluster:
        grid[i, j] = -grid[i, j]


# Wolff algorithm simulation
def simulate_wolff(grid_size, temperature, num_steps):
    grid = init_grid(grid_size)
    history = []

    for _ in range(num_steps):
        wolff_algorithm(grid, temperature)
        magnetization = np.sum(grid)
        history.append(magnetization)

    return history


# Parameters
grid_size = 3
temperature = 2.0
num_steps = 1000

# Simulation
history = simulate_wolff(grid_size, temperature, num_steps)

print(len(history))

# Plotting
_, ax = plt.subplots(figsize=(8, 4))
ax.scatter(range(num_steps), history)
ax.set(
    xlabel="Monte Carlo Steps",
    ylabel="Magnetization",
    title=f"Wolff Algorithm - {grid_size}x{grid_size} Ising Model at T={temperature}",
)
plt.show()
