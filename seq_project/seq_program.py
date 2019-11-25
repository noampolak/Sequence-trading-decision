# build and calc the label data - 1 for buy/sell for nothing
# split the data to lots of timeframes - dev and test for fiting the model
#fit the model
#run the model on the test set
#download updated data and test the model on them
from settings import base_settings
from preprocess_data_files import loadcsvfile

# loading all data files to memory as matrix

files_df = loadcsvfile.load_all_csv_files_in_path(base_settings.HISTORY_INDEX_PATH)
merged_data_frame = loadcsvfile.merge_all_data_frames_by_date_field(files_df)
# first output - the merged data frame in csv file
merged_data_frame.to_csv("{}/merged_data_frame.csv".format(base_settings.OUTPUTS_PATH))