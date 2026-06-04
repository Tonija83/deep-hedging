import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Example synthetic results
# (replace with your backtest output)
# -----------------------------
np.random.seed(42)

delta_errors = np.random.normal(0, 1.0, 10000)
rl_errors = np.random.normal(0, 0.7, 10000)


# -----------------------------
# 1. Histogram comparison
# -----------------------------
plt.figure()

plt.hist(delta_errors, bins=50, alpha=0.6, label="Delta Hedging")
plt.hist(rl_errors, bins=50, alpha=0.6, label="Deep RL Hedging")

plt.title("Distribution of Hedging Errors")
plt.legend()
plt.show()


# -----------------------------
# 2. CVaR comparison
# -----------------------------
def cvar(x, alpha=0.95):
    x_sorted = np.sort(x)
    idx = int((1 - alpha) * len(x))
    return np.mean(x_sorted[:idx])

methods = ["Delta", "Deep RL"]
cvars = [cvar(delta_errors), cvar(rl_errors)]

plt.figure()
plt.bar(methods, cvars)
plt.title("CVaR Comparison (95%)")
plt.show()


# -----------------------------
# 3. Risk profile plot
# -----------------------------
plt.figure()
plt.boxplot([delta_errors, rl_errors], labels=["Delta", "Deep RL"])
plt.title("Hedging Error Risk Profile")
plt.show()
