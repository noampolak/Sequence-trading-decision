# build and calc the label data - 1 for buy/sell for nothing
# split the data to lots of timeframes - dev and test for fiting the model
#fit the model
#run the model on the test set
#download updated data and test the model on them
from settings import base_settings
from preprocess_data_files import loadcsvfile, moving_average

# loading all data files to memory as matrix

files_df = loadcsvfile.load_all_csv_files_in_path(base_settings.HISTORY_INDEX_PATH)
merged_data_frame = loadcsvfile.merge_all_data_frames_by_date_field(files_df)
print("merged_data_frame columns is: ",len(merged_data_frame.columns))
# first output - the merged data frame in csv file
merged_data_frame.to_csv("{}/merged_data_frame.csv".format(base_settings.OUTPUTS_PATH))
# create more fetures - moving averages and deltas
moving_average_list = [3,5,10,20,30,50,100,200]
merged_data_frame_plus_MA = moving_average.add_list_of_moving_average_to_data_frame(merged_data_frame, moving_average_list)
print("merged_data_frame_plus_MA columns is: ",len(merged_data_frame_plus_MA.columns))
# second output - data with moving averages in csv file
merged_data_frame_plus_MA.to_csv("{}/merged_data_frame_plus_MA.csv".format(base_settings.OUTPUTS_PATH))
