import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Simulation Parameters
# --------------------------------------------------

np.random.seed(42)

S0 = 100          # Initial stock price
mu = 0.08         # Expected annual return
sigma = 0.20      # Annual volatility

T = 1.0           # One year
steps = 252       # Trading days
paths = 10        # Display only 10 paths

dt = T / steps

# --------------------------------------------------
# Simulate GBM
# --------------------------------------------------

prices = np.zeros((steps + 1, paths))
prices[0] = S0

for t in range(1, steps + 1):

    Z = np.random.normal(size=paths)

    prices[t] = (
        prices[t-1]
        * np.exp(
            (mu - 0.5 * sigma**2) * dt
            + sigma * np.sqrt(dt) * Z
        )
    )

# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(11,6))

for i in range(paths):

    plt.plot(
        prices[:, i],
        linewidth=1.8
    )

plt.title(
    "Simulated Market Environment (Geometric Brownian Motion)",
    fontsize=16
)

plt.xlabel("Trading Days")

plt.ylabel("Asset Price")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figure_20_market_environment.png",
    dpi=300
)

plt.savefig(
    "figure_20_market_environment.pdf"
)

plt.show()
