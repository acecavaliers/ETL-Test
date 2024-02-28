import pandas as pd  # Importing the pandas library and aliasing it as pd

def save_to_csv(df: pd.DataFrame, save_path: str):
    '''
    Writes pandas DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): Pandas DataFrame containing the clean data.
        save_path (str): Path to save the CSV file.

    Returns:
        None
    '''
    # Write DataFrame to CSV
    df.to_csv(save_path, index=False)
    return
