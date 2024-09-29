import yfinance as yf
import pandas as pd

def fetch_etf_data(selected_etfs):
    """
    Fetches returns, expected returns, and covariance matrix for the selected ETFs.
    
    Args:
        selected_etfs (list): List of selected ETFs.
    
    Returns:
        Tuple of returns, expected returns, and covariance matrix.
    """
    etf_data = yf.download(selected_etfs)
    returns = etf_data['Adj Close'].pct_change().dropna()
    expected_returns = returns.mean()
    cov_matrix = returns.cov()
    return returns, expected_returns, cov_matrix

def calculate_portfolio_performance(returns, weights):
    """
    Calculate daily and monthly portfolio performance based on returns and weights.
    
    Args:
        returns (pd.DataFrame): DataFrame containing daily returns for the ETFs.
        weights (list): Portfolio weights for the selected ETFs.
    
    Returns:
        Tuple of daily and monthly portfolio performance.
    """
    portfolio_returns = returns.dot(weights)
    daily_performance = portfolio_returns
    monthly_performance = portfolio_returns.resample('ME').ffill().pct_change().fillna(0)
    return daily_performance, monthly_performance

def fetch_global_markets():
    """
    Fetch global market data (e.g., stock indices).
    
    Returns:
        dict: Dictionary of market data with index names as keys and their data.
    """
    markets = {
        "S&P 500": "SPY",
        "NASDAQ": "QQQ",
        "Dow Jones": "^DJI",  # Changed from 'DIA' to '^DJI'
        "FTSE 100": "^FTSE"
    }

    tickers = " ".join(markets.values())  # Combine all tickers into a single string
    try:
        data = yf.download(tickers, period="1d", threads=True)  # Use threading for faster download
        market_data = {}
        for name, ticker in markets.items():
            market_data[name] = {
                "last_price": data['Close'][ticker].iloc[-1],
                "change": data['Close'][ticker].iloc[-1] - data['Open'][ticker].iloc[-1],
                "percent_change": (data['Close'][ticker].iloc[-1] - data['Open'][ticker].iloc[-1]) / data['Open'][ticker].iloc[-1] * 100
            }
    except Exception as e:
        print(f"An error occurred while fetching market data: {e}")
        market_data = {name: {"last_price": None, "change": None, "percent_change": None} for name in markets}

    return market_data