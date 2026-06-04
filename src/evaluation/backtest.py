import numpy as np
from .metrics import evaluation_report


def run_backtest(model, env, n_paths=10000):
    """
    Generic backtest loop:
    - model: hedging strategy (delta or RL)
    - env: market simulator (GBM / Heston)
    """

    portfolios = []
    payoffs = []
    positions = []

    for _ in range(n_paths):

        S_path = env.simulate_path()
        payoff = env.payoff(S_path)

        portfolio_path, position_path = model.hedge(S_path)

        portfolios.append(portfolio_path)
        payoffs.append(payoff)
        positions.append(position_path)

    portfolios = np.array(portfolios)
    payoffs = np.array(payoffs)

    results = evaluation_report(portfolios, payoffs)

    return results
