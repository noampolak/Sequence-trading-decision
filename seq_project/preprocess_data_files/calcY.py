from . import loadcsvfile
from .findLongY import find_long_Y
from .findShortY import find_short_Y
import numpy as np


def Y_date_and_ind(df, wanted_yield=0.1, capLeverage=5):
  # df = loadcsvfile.load_file_to_csv(y_file)
  # we asume that the source file has first row - title, first column is date
  # and last is the yield
  # we now convert the yield
  df.iloc[:,-1] = loadcsvfile.convert_column_to_float(df, df.shape[1] -1).to_frame()
  df.iloc[:,-1] = df.iloc[:,-1] 
  df = df.sort_values(by=df.columns[0])
  rows_num = df.shape[0]
  print('df.iloc[:,-1]= ', df.iloc[:,-1])
  yieldArray = find_long_Y(capLeverage, wanted_yield*100, df.iloc[:,-1])
  yieldArray_neg = find_short_Y(capLeverage, wanted_yield*100, df.iloc[:,-1])
  # merge yieldArray and yieldArray_neg to one matrix
  mixed_y = np.zeros((yieldArray.shape))
  mixed_y += yieldArray + yieldArray_neg
  # Y = np.array(df.iloc[:,0].to_numpy(),yieldArray)
  print('yieldArray=',yieldArray)
  print('df.iloc[:,0].to_numpy()=',df.iloc[:,0].dt.strftime("%Y%m%d").astype(int).to_numpy())
  Y = np.append(df.iloc[:,0].dt.strftime("%Y%m%d").astype(int).to_numpy(), mixed_y)
  Y = Y.reshape(2,rows_num).transpose()
  return Y

def load_Y_files(Y_files_path, wanted_yield=0.1, capLeverage=5):
  # load the Y files
  df_files = loadcsvfile.load_all_csv_files_in_path(Y_files_path)
  Y_np = np.zeros(())
  for Y_file in df_files:
    Y_np = Y_date_and_ind(Y_file, wanted_yield, capLeverage)

  return Y_np