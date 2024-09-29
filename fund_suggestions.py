def etf_suggestions():
    """
    Returns a list of popular ETFs categorised by asset class.

    Returns:
        dict: Dictionary of ETFs and their asset classes.
    """
    etfs = {
        "VTI": "US Total Stock Market",
        "AGG": "US Bond Market",
        "VNQ": "Real Estate",
        "SPY": "S&P 500",
        "BNDX": "International Bonds",
        "TIP": "Inflation-Protected Bonds",
        "GLD": "Gold",
        "QQQ": "Nasdaq 100"
    }
    
    return etfs

