# build and calc the label data - 1 for buy/sell for nothing
# split the data to lots of timeframes - dev and test for fiting the model
#fit the model
#run the model on the test set
#download updated data and test the model on them
from settings import base_settings
from preprocess_data_files import loadcsvfile

# loading all data files to memory as matrix

files_df = loadcsvfile.load_all_csv_files_in_path(base_settings.HISTORY_INDEX_PATH)