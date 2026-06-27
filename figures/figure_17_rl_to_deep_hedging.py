import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --------------------------------------------------
# Figure
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 7))

ax.set_xlim(0, 14)
ax.set_ylim(0, 10)

ax.axis("off")

# --------------------------------------------------
# Helper function
# --------------------------------------------------

def box(x, y, w, h, text, fontsize=12):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.3",
        linewidth=2,
        facecolor="white"
    )
    ax.add_patch(rect)

    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize
    )

# --------------------------------------------------
# Left side
# --------------------------------------------------

box(
    0.7,
    6.3,
    4,
    2.8,
    "Classical\nReinforcement Learning",
    fontsize=13
)

ax.text(
    2.7,
    5.8,
    "Applications",
    ha="center",
    fontsize=12,
    fontweight="bold"
)

ax.text(
    2.7,
    4.8,
    "• AlphaGo\n"
    "• Robotics\n"
    "• Autonomous Driving\n"
    "• Resource Allocation",
    ha="center",
    fontsize=11
)

ax.text(
    2.7,
    2.3,
    r"$\max_{\pi}\; \mathbb{E}[R]$",
    fontsize=18,
    ha="center"
)

# --------------------------------------------------
# Right side
# --------------------------------------------------

box(
    9.3,
    6.3,
    4,
    2.8,
    "Deep Hedging",
    fontsize=13
)

ax.text(
    11.3,
    5.8,
    "Applications",
    ha="center",
    fontsize=12,
    fontweight="bold"
)

ax.text(
    11.3,
    4.8,
    "• Options\n"
    "• Derivatives\n"
    "• Portfolio Hedging\n"
    "• Risk Management",
    ha="center",
    fontsize=11
)

ax.text(
    11.3,
    2.3,
    r"$\min_{\theta}\; \rho(X_T^{\theta})$",
    fontsize=18,
    ha="center"
)

# --------------------------------------------------
# Middle transition
# --------------------------------------------------

box(
    5.4,
    4.2,
    3.2,
    1.4,
    "Policy Learning",
    fontsize=12
)

box(
    5.4,
    2.0,
    3.2,
    1.4,
    "Neural Networks",
    fontsize=12
)

arrow = dict(
    arrowstyle="->",
    linewidth=2
)

# left -> middle

ax.annotate(
    "",
    xy=(5.4, 7.7),
    xytext=(4.7, 7.7),
    arrowprops=arrow
)

# middle vertical

ax.annotate(
    "",
    xy=(7, 5.6),
    xytext=(7, 6.3),
    arrowprops=arrow
)

ax.annotate(
    "",
    xy=(7, 3.4),
    xytext=(7, 4.2),
    arrowprops=arrow
)

# middle -> right

ax.annotate(
    "",
    xy=(9.3, 7.7),
    xytext=(8.6, 7.7),
    arrowprops=arrow
)

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
        boxstyle="round",
        facecolor="#F0F0F0",
        edgecolor="black"
    )
)

# --------------------------------------------------
# Title
# --------------------------------------------------

plt.title(
    "From Reinforcement Learning to Deep Hedging",
    fontsize=18,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_17_rl_to_deep_hedging.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_17_rl_to_deep_hedging.pdf",
    bbox_inches="tight"
)

plt.show()
