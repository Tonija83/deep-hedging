import yfinance as yf
import pandas as pd


def load_market_data(
    ticker="^ATX",
    start="2015-01-01",
    end="2025-12-31"
):
    """
    Downloads historical market data.

    Parameters
    ----------
    ticker : str
        Yahoo Finance ticker.

    start : str
        Start date.

    end : str
        End date.

    Returns
    -------
    pandas.DataFrame
    """

    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True
    )

    return data
