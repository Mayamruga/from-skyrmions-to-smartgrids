# src/data/preprocess.py

import pandas as pd
import os

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
