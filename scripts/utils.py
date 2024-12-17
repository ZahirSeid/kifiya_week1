import pandas as pd

def load_csv(filepath):
    """
    Load a CSV file into a DataFrame.
    """
    return pd.read_csv(filepath)

def clean_column_names(df):
    """
    Cleans column names by converting them to lowercase and replacing spaces with underscores.
    """
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

