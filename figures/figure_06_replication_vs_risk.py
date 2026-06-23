import numpy as np
import matplotlib.pyplot as plt

# Create output directory if needed
os.makedirs("figures", exist_ok=True)

# Time axis
time = np.linspace(0, 1, 250)

# Classical replication
replication_error = np.full_like(time, 0.08)

# Deep hedging
deep_hedging_error = 0.35 * np.exp(-4 * time) + 0.015

# Plot
plt.figure(figsize=(10, 6))

plt.plot(
    time,
    replication_error,
    linewidth=3,
    label="Classical Replication",
)

plt.plot(
    time,
    deep_hedging_error,
    linewidth=3,
    label="Deep Hedging",
)

plt.xlabel("Training / Rebalancing Time")
plt.ylabel("Residual Risk")
plt.title("Replication vs. Risk Minimization")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    "figures/figure_06_replication_vs_risk.png",
    dpi=300,
    bbox_inches="tight",
)

plt.savefig(
    "figures/figure_06_replication_vs_risk.pdf",
    bbox_inches="tight",
)

plt.show()
