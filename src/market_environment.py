import numpy as np


def estimate_parameters(close_prices):

    log_returns = np.log(
        close_prices / close_prices.shift(1)
    ).dropna()

    mu = log_returns.mean() * 252

    sigma = log_returns.std() * np.sqrt(252)

    return mu, sigma


def simulate_gbm(
        S0,
        mu,
        sigma,
        T=1,
        steps=252,
        paths=1000,
        seed=42
):

    np.random.seed(seed)

    dt = T / steps

    prices = np.zeros((steps + 1, paths))

    prices[0] = S0

    for t in range(1, steps + 1):

        Z = np.random.normal(size=paths)

        prices[t] = (
            prices[t-1]
            * np.exp(
                (mu - 0.5 * sigma**2) * dt
                + sigma * np.sqrt(dt) * Z
            )
        )

    return prices
