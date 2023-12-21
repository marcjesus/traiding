import pandas as pd

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))


def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.
    
    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date
    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    # TODO: Implement Function
    
    return (close - close.shift(1))/close.shift(1)

calculate_returns(calculate_returns)