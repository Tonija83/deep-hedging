import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --------------------------------------------------------
# Parameters
# --------------------------------------------------------

alpha = 0.95

x = np.linspace(-4, 4, 1000)

pdf = norm.pdf(x)

var = norm.ppf(alpha)

cvar = norm.pdf(var) / (1 - alpha)

# --------------------------------------------------------
# Plot
# --------------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    x,
    pdf,
    linewidth=3,
    label="Loss Distribution"
)

# Shade CVaR region

plt.fill_between(
    x,
    pdf,
    where=(x >= var),
    alpha=0.35,
    label=f"CVaR ({int(alpha*100)}%)"
)

# VaR line

plt.axvline(
    var,
    linestyle="--",
    linewidth=2,
    label="VaR"
)

plt.text(
    var + 0.05,
    max(pdf)*0.9,
    "VaR",
    fontsize=11
)

plt.text(
    var + 0.55,
    0.05,
    "Tail Risk",
    fontsize=11
)

plt.title(
    "Loss Function: Variance versus CVaR",
    fontsize=16
)

plt.xlabel("Portfolio Loss")

plt.ylabel("Density")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "figure_21_loss_function.png",
    dpi=300
)

plt.savefig(
    "figure_21_loss_function.pdf"
)

plt.show()
