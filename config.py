# =====================================================
# GENERAL
# =====================================================

PROJECT_NAME = "Deep Hedging Project"

RANDOM_SEED = 42

# =====================================================
# MARKET DATA
# =====================================================

# Yahoo Finance ticker
# Examples:
# "^ATX"      -> Austrian Traded Index
# "OMV.VI"
# "EBS.VI"
# "VER.VI"

TICKER = "^ATX"

START_DATE = "2026-01-01"
END_DATE = "2026-06-29"

TRADING_DAYS = 179

# =====================================================
# OPTION PARAMETERS
# =====================================================

OPTION_TYPE = "European Call"

INITIAL_PRICE = 100.0

STRIKE_PRICE = 100.0

MATURITY = 1.0

RISK_FREE_RATE = 0.02

DIVIDEND_YIELD = 0.00

# =====================================================
# MARKET MODEL
# =====================================================

# Estimated automatically from historical data
# (used only as fallback values)

MU = 0.08

SIGMA = 0.20

# =====================================================
# MONTE CARLO
# =====================================================

NUMBER_OF_PATHS = 1000

NUMBER_OF_TIME_STEPS = 252

# =====================================================
# HEDGING
# =====================================================

INITIAL_PORTFOLIO = 0.0

INITIAL_CASH = 0.0

TRANSACTION_COST = 0.001

REBALANCING_FREQUENCY = 1

# =====================================================
# RISK MEASURE
# =====================================================

RISK_MEASURE = "CVaR"

CVAR_ALPHA = 0.95

ENTROPIC_GAMMA = 1.0

# =====================================================
# REINFORCEMENT LEARNING
# =====================================================

STATE_DIMENSION = None

ACTION_DIMENSION = 1

DISCOUNT_FACTOR = 1.0

# =====================================================
# NEURAL NETWORK
# =====================================================

INPUT_SIZE = None

OUTPUT_SIZE = 1

HIDDEN_LAYER_1 = 64

HIDDEN_LAYER_2 = 64

HIDDEN_LAYER_3 = 64

ACTIVATION = "ReLU"

# =====================================================
# TRAINING
# =====================================================

EPOCHS = 200

BATCH_SIZE = 256

LEARNING_RATE = 1e-3

OPTIMIZER = "Adam"

# =====================================================
# OUTPUT FOLDERS
# =====================================================

DATA_FOLDER = "data"

RAW_DATA_FOLDER = "data/raw"

PROCESSED_DATA_FOLDER = "data/processed"

FIGURE_FOLDER = "figures"

PYTHON_FIGURES = "figures/python"

PNG_FOLDER = "figures/png"

PDF_FOLDER = "figures/pdf"

TIKZ_FOLDER = "figures/tikz"

RESULT_FOLDER = "results"

EXPERIMENT_FOLDER = "experiments"

# =====================================================
# FIGURE STYLE
# =====================================================

FIGURE_WIDTH = 10

FIGURE_HEIGHT = 6

DPI = 300

FONT_SIZE = 12

TITLE_SIZE = 16

LINE_WIDTH = 2.0

GRID = True

# =====================================================
# SAVE OPTIONS
# =====================================================

SAVE_PNG = True

SAVE_PDF = True

SHOW_FIGURE = True

# =====================================================
# LOGGING
# =====================================================

VERBOSE = True
