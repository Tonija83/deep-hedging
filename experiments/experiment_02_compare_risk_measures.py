import numpy as np

# --------------------------------------------------------
# Simulated Portfolio Profits
# --------------------------------------------------------

np.random.seed(42)

profits = np.random.normal(
    loc=2,
    scale=10,
    size=100000
)

losses = -profits

# --------------------------------------------------------
# Variance
# --------------------------------------------------------

variance = np.var(losses)

# --------------------------------------------------------
# Value at Risk
# --------------------------------------------------------

alpha = 0.95

VaR = np.quantile(
    losses,
    alpha
)

# --------------------------------------------------------
# Conditional Value at Risk
# --------------------------------------------------------

CVaR = losses[
    losses >= VaR
].mean()

# --------------------------------------------------------
# Output
# --------------------------------------------------------

print("="*45)

print("Comparison of Risk Measures")

print("="*45)

print(f"Variance : {variance:.4f}")

print(f"VaR ({alpha:.0%}) : {VaR:.4f}")

print(f"CVaR ({alpha:.0%}) : {CVaR:.4f}")

print("="*45)
