import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --------------------------------------------------
# Figure setup
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 7))

ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

# --------------------------------------------------
# Colors
# --------------------------------------------------

RL_COLOR = "#DCEEFF"
HEDGE_COLOR = "#FFE7D6"
MID_COLOR = "#EAEAEA"
EDGE_COLOR = "#333333"

# --------------------------------------------------
# Box helper (strukturierte Box mit Inhalt)
# --------------------------------------------------

def labeled_box(x, y, w, h, title, applications, formula, facecolor="white"):

    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.5,rounding_size=0.08",
        linewidth=1.5,
        edgecolor=EDGE_COLOR,
        facecolor=facecolor
    )
    ax.add_patch(rect)

    # Title
    ax.text(
        x + w / 2,
        y + h * 0.78,
        title,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold"
    )

    # Applications
    ax.text(
        x + w / 2,
        y + h * 0.45,
        applications,
        ha="center",
        va="center",
        fontsize=11
    )

    # Formula
    ax.text(
        x + w / 2,
        y + h * 0.15,
        formula,
        ha="center",
        va="center",
        fontsize=16
    )

# --------------------------------------------------
# Left: Reinforcement Learning
# --------------------------------------------------

labeled_box(
    0.7,
    6.3,
    4,
    2.8,
    "Classical Reinforcement Learning",
    "AlphaGo\nRobotics\nAutonomous Driving\nResource Allocation",
    r"$\max_{\pi}\; \mathbb{E}[R]$",
    facecolor=RL_COLOR
)

# --------------------------------------------------
# Right: Deep Hedging
# --------------------------------------------------

labeled_box(
    9.3,
    6.3,
    4,
    2.8,
    "Deep Hedging",
    "Options\nDerivatives\nPortfolio Hedging\nRisk Management",
    r"$\min_{\theta}\; \rho(X_T^{\theta})$",
    facecolor=HEDGE_COLOR
)

# --------------------------------------------------
# Middle blocks
# --------------------------------------------------

def simple_box(x, y, w, h, text):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.4,rounding_size=0.08",
        linewidth=1.5,
        edgecolor=EDGE_COLOR,
        facecolor=MID_COLOR
    )
    ax.add_patch(rect)

    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold"
    )

simple_box(5.4, 4.2, 3.2, 1.4, "Policy Learning")
simple_box(5.4, 2.0, 3.2, 1.4, "Neural Networks")

# --------------------------------------------------
# Arrows
# --------------------------------------------------

arrow = dict(
    arrowstyle="-|>",
    linewidth=2,
    color="#444444",
    shrinkA=0,
    shrinkB=0
)

# left -> middle
ax.annotate("", xy=(5.4, 7.7), xytext=(4.7, 7.7), arrowprops=arrow)

# vertical flow
ax.annotate("", xy=(7, 5.6), xytext=(7, 6.3), arrowprops=arrow)
ax.annotate("", xy=(7, 3.4), xytext=(7, 4.2), arrowprops=arrow)

# middle -> right
ax.annotate("", xy=(9.3, 7.7), xytext=(8.6, 7.7), arrowprops=arrow)

# --------------------------------------------------
# Bottom statement
# --------------------------------------------------

statement = (
    "Deep Hedging transfers Reinforcement Learning to\n"
    "financial risk management by replacing reward maximization\n"
    "with direct risk minimization."
)

ax.text(
    7,
    0.5,
    statement,
    ha="center",
    fontsize=12,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="#F2F2F2",
        edgecolor=EDGE_COLOR
    )
)

# --------------------------------------------------
# Title
# --------------------------------------------------

plt.title(
    "Vom Reinforcement Learning zum Deep Hedging",
    fontsize=18,
    pad=20
)

plt.tight_layout()

# --------------------------------------------------
# Save outputs
# --------------------------------------------------

plt.savefig("figure_rl_to_deep_hedging.png", dpi=300, bbox_inches="tight")
plt.savefig("figure_rl_to_deep_hedging.pdf", bbox_inches="tight")

plt.show()
