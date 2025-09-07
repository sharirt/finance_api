import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import pandas_ta
from computations import compute_macd, compute_atr

def get_garman_klass_vol(df: pd.DataFrame):
    """
    Compute Garman-Klass volatility estimator.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with columns ['open', 'high', 'low', 'adj close'].

    Returns
    -------
    pd.Series
        Garman-Klass volatility values.
    """
    return ((np.log(df['high'])-np.log(df['low']))**2)/2-(2*np.log(2)-1)*((np.log(df['adj close'])-np.log(df['open']))**2)

def get_rsi(df: pd.DataFrame):
    """
    Calculate 20-period Relative Strength Index (RSI).

    Parameters
    ----------
    df : pd.DataFrame
        Multi-index DataFrame with 'adj close' and 'ticker' as level 1 index.

    Returns
    -------
    pd.Series
        RSI values aligned with input index.
    """
    return df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=20))

def get_atr(df: pd.DataFrame):
    """
    Compute standardized 14-period Average True Range (ATR).

    Parameters
    ----------
    df : pd.DataFrame
        Multi-index DataFrame with ['high', 'low', 'close'] and 'ticker' as level 1 index.

    Returns
    -------
    pd.Series
        Z-score normalized ATR values.
    """


    return df.groupby(level=1, group_keys=False).apply(compute_atr)

def get_macd(df: pd.DataFrame):
    """
    Compute standardized MACD signal.

    Parameters
    ----------
    df : pd.DataFrame
        Multi-index DataFrame with 'adj close' and 'ticker' as level 1 index.

    Returns
    -------
    pd.Series
        Z-score normalized MACD values.
    """
    return df.groupby(level=1, group_keys=False)['adj close'].apply(compute_macd)

def get_dollar_volume(df: pd.DataFrame):
    """
    Compute dollar trading volume (in millions).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with ['adj close', 'volume'].

    Returns
    -------
    pd.Series
        Dollar volume values in millions.
    """
    return (df['adj close']*df['volume'])/1e6
