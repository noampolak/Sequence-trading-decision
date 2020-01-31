import pandas as pd
from sklearn import preprocessing

def normalize_dataframe(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(df)
    return pd.DataFrame(x_scaled)