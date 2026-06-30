import os
import numpy as np
import matplotlib.pyplot as plt

from src.market_data import load_market_data
from src.market_environment import (
    estimate_parameters,
    simulate_gbm
)

from config import *

# --------------------------------------------------------
# Create output folder
# --------------------------------------------------------

os.makedirs(RESULT_FOLDER, exist_ok=True)

# --------------------------------------------------------
# Load historical data
# --------------------------------------------------------

print("Loading market data...")

data = load_market_data(
    ticker=TICKER,
    start=START_DATE,
    end=END_DATE
)

close = data["Close"]

# --------------------------------------------------------
# Estimate parameters
# --------------------------------------------------------

mu, sigma = estimate_parameters(close)

print(f"Estimated drift      : {mu:.4f}")
print(f"Estimated volatility : {sigma:.4f}")

# --------------------------------------------------------
# Monte Carlo simulation
# --------------------------------------------------------

prices = simulate_gbm(
    S0=float(close.iloc[-1]),
    mu=float(mu),
    sigma=float(sigma),
    T=MATURITY,
    steps=NUMBER_OF_TIME_STEPS,
    paths=NUMBER_OF_PATHS,
    seed=RANDOM_SEED
)

# --------------------------------------------------------
# Save simulation
# --------------------------------------------------------

np.save(
    f"{RESULT_FOLDER}/market_paths.npy",
    prices
)

print("Monte Carlo paths saved.")

# --------------------------------------------------------
# Plot
# --------------------------------------------------------

plt.figure(figsize=(10,6))

for i in range(min(20, NUMBER_OF_PATHS)):
    plt.plot(prices[:, i])

plt.title("Simulated Market Environment")

plt.xlabel("Trading Day")

plt.ylabel("Asset Price")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{RESULT_FOLDER}/experiment_01_market_environment.png",
    dpi=DPI
)

plt.show()
