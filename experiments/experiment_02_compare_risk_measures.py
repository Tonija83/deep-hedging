import numpy as np

from config import *

# --------------------------------------------------------
# Load Monte Carlo simulation
# --------------------------------------------------------

prices = np.load(
    f"{RESULT_FOLDER}/market_paths.npy"
)

# --------------------------------------------------------
# Portfolio Loss
# --------------------------------------------------------

initial_price = prices[0]

terminal_price = prices[-1]

portfolio_profit = terminal_price - initial_price

loss = -portfolio_profit

# --------------------------------------------------------
# Variance
# --------------------------------------------------------

variance = np.var(loss)

# --------------------------------------------------------
# VaR
# --------------------------------------------------------

VaR = np.quantile(
    loss,
    CVAR_ALPHA
)

# --------------------------------------------------------
# CVaR
# --------------------------------------------------------

CVaR = loss[
    loss >= VaR
].mean()

# --------------------------------------------------------
# Expected Loss
# --------------------------------------------------------

expected_loss = np.mean(loss)

# --------------------------------------------------------
# Print Results
# --------------------------------------------------------

print("="*50)

print("Comparison of Risk Measures")

print("="*50)

print(f"Expected Loss : {expected_loss:.4f}")

print(f"Variance      : {variance:.4f}")

print(f"VaR           : {VaR:.4f}")

print(f"CVaR          : {CVaR:.4f}")

print("="*50)
