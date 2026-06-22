import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------
# Simulated time axis
# ----------------------------------

time = np.linspace(0, 1, 250)

# ----------------------------------
# Classical Delta Hedging
# (Residual risk remains approximately constant)
# ----------------------------------

replication_error = np.full_like(time, 0.08)

# ----------------------------------
# Deep Hedging
# (Risk decreases during training)
# ----------------------------------

deep_hedging_error = (
    0.35 * np.exp(-4 * time)
    + 0.015
)

# ----------------------------------
# Plot
# ----------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    time,
    replication_error,
    linewidth=3,
    label="Classical Replication"
)

plt.plot(
    time,
    deep_hedging_error,
    linewidth=3,
    label="Deep Hedging"
)

plt.xlabel("Training / Rebalancing Time")

plt.ylabel("Residual Risk")

plt.title("Replication vs. Risk Minimization")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("figures/figure_06_replication_vs_risk.png", dpi=300)

plt.savefig("figures/figure_06_replication_vs_risk.pdf")

plt.show()
