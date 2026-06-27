import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# -------------------------------------------------
# Figure setup
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 9))

ax.set_xlim(0, 12)
ax.set_ylim(0, 15)

ax.axis("off")

# -------------------------------------------------
# Helper function
# -------------------------------------------------

def draw_box(x, y, w, h, text, fontsize=12):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.25",
        linewidth=2,
        facecolor="white"
    )
    ax.add_patch(box)

    ax.text(
        x + w/2,
        y + h/2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize
    )

# -------------------------------------------------
# Coordinates
# -------------------------------------------------

x = 4
w = 4
h = 0.9
step = 1.45

labels = [

    "Market State\n$s_t$",

    "Policy Network\n$\\pi_\\theta$",

    "Trading Action\n$a_t$",

    "Portfolio Update",

    "Transaction Costs",

    "Terminal Portfolio\n$X_T$",

    "Risk Measure\n$\\rho(X_T)$",

    "Loss Function",

    "Gradient Descent",

    "Updated Parameters\n$\\theta$"

]

y_positions = []

current_y = 13

for label in labels:

    draw_box(x, current_y, w, h, label)

    y_positions.append(current_y)

    current_y -= step

# -------------------------------------------------
# Arrows
# -------------------------------------------------

for i in range(len(y_positions)-1):

    ax.annotate(

        "",

        xy=(6, y_positions[i]-0.05),

        xytext=(6, y_positions[i+1]+h),

        arrowprops=dict(

            arrowstyle="->",

            linewidth=2

        )

    )

# -------------------------------------------------
# Side annotation
# -------------------------------------------------

ax.text(

    10.3,

    7.2,

    "Training Loop",

    fontsize=13,

    rotation=90,

    fontweight="bold"

)

# -------------------------------------------------
# Objective function
# -------------------------------------------------

ax.text(

    6,

    -0.3,

    r"$\theta^{*}=\arg\min_{\theta}\rho(X_T^{\theta})$",

    fontsize=18,

    ha="center"

)

# -------------------------------------------------
# Bottom explanation
# -------------------------------------------------

ax.text(

    6,

    -1.1,

    "The neural network learns an optimal hedging strategy by minimizing a financial risk measure.",

    fontsize=11,

    ha="center"

)

# -------------------------------------------------
# Title
# -------------------------------------------------

plt.title(

    "Deep Hedging System Architecture",

    fontsize=18,

    pad=20

)

plt.tight_layout()

plt.savefig(

    "figure_17_deep_hedging_system_architecture.png",

    dpi=300,

    bbox_inches="tight"

)

plt.savefig(

    "figure_17_deep_hedging_system_architecture.pdf",

    bbox_inches="tight"

)

plt.show()
