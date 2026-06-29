import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --------------------------------------------------
# Figure
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(16, 5))

ax.set_xlim(0, 18)
ax.set_ylim(0, 6)

ax.axis("off")

# --------------------------------------------------
# Helper
# --------------------------------------------------

def draw_box(x, y, w, h, text):

    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.20",
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
        fontsize=10
    )

# --------------------------------------------------
# Boxes
# --------------------------------------------------

boxes = [

    ("Historical\nMarket Data", 0.5),

    ("Monte Carlo\nSimulation", 2.9),

    ("Market\nEnvironment", 5.3),

    ("Policy\nNetwork", 7.7),

    ("Portfolio\nUpdate", 10.1),

    ("Risk\nMeasure", 12.5),

    ("Loss\nFunction", 14.9),

]

for text, xpos in boxes:

    draw_box(
        xpos,
        2.3,
        1.9,
        1.1,
        text
    )

# --------------------------------------------------
# Arrows
# --------------------------------------------------

for i in range(len(boxes)-1):

    x1 = boxes[i][1] + 1.9
    x2 = boxes[i+1][1]

    ax.annotate(
        "",
        xy=(x2, 2.85),
        xytext=(x1, 2.85),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2
        )
    )

# --------------------------------------------------
# Gradient Descent Feedback
# --------------------------------------------------

ax.annotate(
    "",
    xy=(8.6,4.6),
    xytext=(15.9,4.6),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=2,
        linestyle="dashed"
    )
)

ax.text(
    12.3,
    4.85,
    "Gradient Descent / Backpropagation",
    fontsize=10,
    ha="center"
)

ax.annotate(
    "",
    xy=(8.6,3.45),
    xytext=(8.6,4.55),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=2,
        linestyle="dashed"
    )
)

# --------------------------------------------------
# Objective Function
# --------------------------------------------------

ax.text(
    9,
    0.8,
    r"$\theta^{*}=\arg\min_{\theta}\rho(X_T^{\theta})$",
    fontsize=17,
    ha="center"
)

# --------------------------------------------------
# Caption
# --------------------------------------------------

ax.text(
    9,
    0.25,
    "Training pipeline of a Deep Hedging framework.",
    fontsize=11,
    ha="center"
)

plt.title(
    "Training Pipeline for Deep Hedging",
    fontsize=18,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_19_training_pipeline.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_19_training_pipeline.pdf",
    bbox_inches="tight"
)

plt.show()
