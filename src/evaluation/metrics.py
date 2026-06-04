import numpy as np

# -----------------------------
# Hedging Error
# -----------------------------
def hedging_error(portfolio, payoff):
    return portfolio - payoff


# -----------------------------
# Mean Error
# -----------------------------
def mean_error(errors):
    return np.mean(errors)


# -----------------------------
# Variance of Hedging Error
# -----------------------------
def variance_error(errors):
    return np.var(errors)


# -----------------------------
# Mean Squared Error
# -----------------------------
def mse_error(errors):
    return np.mean(errors ** 2)


# -----------------------------
# CVaR (Expected Shortfall)
# -----------------------------
def cvar(errors, alpha=0.95):
    """
    Conditional Value at Risk (loss tail)
    """
    sorted_errors = np.sort(errors)
    index = int((1 - alpha) * len(sorted_errors))
    return np.mean(sorted_errors[:index])


# -----------------------------
# Transaction Cost
# -----------------------------
def transaction_cost(positions, cost_rate=0.001):
    """
    positions: array of hedge positions over time
    """
    turnover = np.abs(np.diff(positions))
    return cost_rate * np.sum(turnover)


# -----------------------------
# Full Evaluation Report
# -----------------------------
def evaluation_report(portfolio, payoff, positions=None):
    errors = hedging_error(portfolio, payoff)

    report = {
        "mean_error": mean_error(errors),
        "variance": variance_error(errors),
        "mse": mse_error(errors),
        "cvar_95": cvar(errors, 0.95),
    }

    if positions is not None:
        report["transaction_cost"] = transaction_cost(positions)

    return report
