import numpy as np
from scipy.optimize import minimize

def sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate=0):
    """
    Calculates the Sharpe ratio for the portfolio.
    
    Args:
        weights (ndarray): Portfolio weights.
        expected_returns (ndarray): Expected annual returns for each asset.
        cov_matrix (DataFrame): Covariance matrix of asset returns.
        risk_free_rate (float): Risk-free rate (default 0).

    Returns:
        float: Sharpe ratio of the portfolio.
    """
    portfolio_return = np.dot(weights, expected_returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return (portfolio_return - risk_free_rate) / portfolio_risk

def mean_variance_optimisation(expected_returns, cov_matrix):
    """
    Optimises the portfolio using mean-variance analysis.
    
    Args:
        expected_returns (ndarray): Expected returns for each asset.
        cov_matrix (DataFrame): Covariance matrix of asset returns.

    Returns:
        ndarray: Optimised portfolio weights.
    """
    num_assets = len(expected_returns)
    bounds = tuple((0, 1) for asset in range(num_assets))
    constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}
    initial_weights = num_assets * [1. / num_assets]
    
    result = minimize(lambda weights: -sharpe_ratio(weights, expected_returns, cov_matrix),
                      initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.x

