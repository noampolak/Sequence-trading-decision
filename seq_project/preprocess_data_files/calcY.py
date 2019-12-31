from . import loadcsvfile
from .findLongY import find_long_Y
import numpy as np


def Y_date_and_ind(y_file, wanted_yield=0.1, capLeverage=5):
  df = loadcsvfile.load_file_to_csv(y_file)
  # we asume that the source file has first row - title, first column is date
  # and last is the yield
  # we now convert the yield
  df.iloc[:,-1] = loadcsvfile.convert_column_to_float(df, df.shape[1] -1).to_frame()
  df.iloc[:,-1] = df.iloc[:,-1] 
  df = df.sort_values(by=df.columns[0])
  rows_num = df.shape[0]
  print('df.iloc[:,-1]= ', df.iloc[:,-1])
  yieldArray = find_long_Y(capLeverage, wanted_yield*100, df.iloc[:,-1])
  # Y = np.array(df.iloc[:,0].to_numpy(),yieldArray)
  print('yieldArray=',yieldArray)
  print('df.iloc[:,0].to_numpy()=',df.iloc[:,0].dt.strftime("%Y%m%d").astype(int).to_numpy())
  Y = np.append(df.iloc[:,0].dt.strftime("%Y%m%d").astype(int).to_numpy(), yieldArray)
  Y = Y.reshape(2,rows_num).transpose()
  return Y