# src/data/preprocess.py

import pandas as pd
import os
import numpy as np
import sys

def load_pjm_dataset(file_path: str, target_col: str = "PJME") -> pd.DataFrame:
    """
    Load the PJM Hourly Energy Consumption dataset.

    Parameters
    ----------
    file_path : str
        Path to the raw CSV file.
    target_col : str, optional
        The column to extract as the main forecasting target (default: "PJME").

    Returns
    -------
    pd.DataFrame
        A DataFrame indexed by datetime with a single target column.

    Notes
    -----
    - Parses the 'Datetime' column into pandas datetime.
    - Sets 'Datetime' as the DataFrame index.
    - Drops rows where the target column is NaN.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")

    # Load dataset
    df = pd.read_csv(file_path)

    # Parse datetime and set as index
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime")

    # Select target column
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in dataset. Available: {list(df.columns)}")

    df = df[[target_col]].dropna()

    return df

def clean_timeseries(df: pd.DataFrame,
                     method: str = "interpolate",
                     clip_outliers: bool = True,
                     lower_quantile: float = 0.01,
                     upper_quantile: float = 0.99) -> pd.DataFrame:
    """
    Clean a time series DataFrame with datetime index.

    Steps:
    1. Handle duplicate timestamps (averages duplicates).
    2. Reindex to continuous hourly frequency.
    3. Handle missing values (forward-fill or interpolation).
    4. Clip outliers to given quantiles (optional).

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with datetime index and a single target column.
    method : str, default "interpolate"
        Missing value handling method: "interpolate" or "ffill".
    clip_outliers : bool, default True
        Whether to clip outliers to given quantiles.
    lower_quantile : float, default 0.01
        Lower quantile for clipping.
    upper_quantile : float, default 0.99
        Upper quantile for clipping.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with continuous hourly index.
    """

    # --- 1. Handle duplicates ---
    if df.index.duplicated().sum() > 0:
        df = df.groupby(df.index).mean()

    # --- 2. Reindex to continuous hourly range ---
    full_index = pd.date_range(start=df.index.min(),
                               end=df.index.max(),
                               freq="H")
    df = df.reindex(full_index)

    # --- 3. Handle missing values ---
    if method == "ffill":
        df = df.fillna(method="ffill")
    elif method == "interpolate":
        df = df.interpolate(method="time")
    else:
        raise ValueError("method must be 'ffill' or 'interpolate'")

    # --- 4. Clip outliers ---
    if clip_outliers:
        lower = df.quantile(lower_quantile)[0]
        upper = df.quantile(upper_quantile)[0]
        df = df.clip(lower=lower, upper=upper)

    return df
