import pandas as pd
from pandas.core.frame import DataFrame

def extract(file_path: str) -> DataFrame:
    '''
    extracts csv data and converts to pandas Dataframe
    args:
        file_path (str): path to the csv file
    
    returns:
        df (DataFrame): pandas dataframe containing the csv data
    '''

    # exracts the csv data as pandas daaframe
    df = pd.read_csv(file_path)

    return df