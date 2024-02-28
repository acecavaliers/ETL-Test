import pandas as pd  # Importing the pandas library and aliasing it as pd

def save_to_csv(df: pd.DataFrame, save_path: str):
    '''
    cleans data
    args:
        df (DataFrame): pandas dataframe containing the raw data
    
    returns:
        df (DataFrame): pandas dataframe containing the clean data
    '''

    # drop null values
    df.dropna(inplace=True)

    # remove decimal from year column and convert to string
    df.Year = df.Year.astype('int').astype("str")
    
    return df
