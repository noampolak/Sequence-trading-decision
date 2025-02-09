# build and calc the label data - 1 for buy/sell for nothing
# split the data to lots of timeframes - dev and test for fiting the model
#fit the model
#run the model on the test set
#download updated data and test the model on them
from settings import base_settings
from preprocess_data_files import loadcsvfile, moving_average, deltas, calcY, fit_fetures_to_Y, split_data
from helpers import df_to_matrix
from sequence_model import main_kera
import numpy as np


# loading all data files to memory as matrix

files_df = loadcsvfile.load_all_csv_files_in_path(base_settings.HISTORY_INDEX_PATH)
merged_data_frame = loadcsvfile.merge_all_data_frames_by_date_field(files_df)
print("merged_data_frame columns is: ",len(merged_data_frame.columns))
# first output - the merged data frame in csv file
# merged_data_frame.to_csv("{}/merged_data_frame.csv".format(base_settings.OUTPUTS_PATH))
# create more fetures - moving averages and deltas
# moving_average_list = [3,5,10,20,30,50,100,200]
moving_average_list = [5]
merged_data_frame_plus_MA = moving_average.add_list_of_moving_average_to_data_frame(merged_data_frame, moving_average_list)
print("merged_data_frame_plus_MA columns is: ",len(merged_data_frame_plus_MA.columns))
# second output - data with moving averages in csv file
merged_data_frame_plus_MA.to_csv("{}/merged_data_frame_plus_MA.csv".format(base_settings.OUTPUTS_PATH))
# deltas_list = [1,3,5,10,20,30,50,100,200]
deltas_list = [1]

merged_data_frame_plus_MA_plus_Deltas = deltas.add_list_of_deltas_to_data_frame(merged_data_frame_plus_MA, deltas_list)
merged_data_frame_plus_MA_plus_Deltas.to_csv("{}/merged_data_frame_plus_MA_plus_Deltas.csv".format(base_settings.OUTPUTS_PATH))
# generate the Y - labeled data when 1 == buy/sell and 0 == do nothing
Y = calcY.Y_date_and_ind('{}/S&P 500 Historical Data.csv'.format(base_settings.Y_FILES), base_settings.WANTED_YIELD, base_settings.CAPLEVERAGE)
np.savetxt("{}/Y.csv".format(base_settings.OUTPUTS_PATH), Y, delimiter=",")
# convert X and the features to matrix
fetures_only_numbers = loadcsvfile.convert_all_date_fields_to_number(merged_data_frame_plus_MA_plus_Deltas)
matrix_fetures = df_to_matrix.convert_df_to_matrix(fetures_only_numbers)
# adjust the dates of the fetures to the Y matrix 
# and remove the first N days where the MA fetures are not correct form Y and fetures matrix
matrix_fetures_sorted, Y_matrix_sorted = fit_fetures_to_Y.adjust_dates_of_fetures_and_Y_matrix(matrix_fetures, Y, base_settings.FIRST_ROWS_TO_DELETE)
# np.savetxt("{}/matrix_fetures_sorted.csv".format(base_settings.OUTPUTS_PATH), matrix_fetures_sorted, delimiter=",")
np.savetxt("{}/Y_matrix_sorted.csv".format(base_settings.OUTPUTS_PATH), Y_matrix_sorted, delimiter=",")
# for Recurrent neural network it is needed to take all the dev data and split him to bulk of 200 for examples
X , Y = split_data.create_bulk_matrix(matrix_fetures_sorted, Y_matrix_sorted, base_settings.FIRST_ROWS_TO_DELETE)
# split the model to dev and test set
print('X.shape= ',X.shape, 'Y.shape= ',Y.shape)

X_dev, X_test, Y_dev, Y_test = split_data.split_to_dev_and_test(X, Y, base_settings.TEST_SET_SIZE)
print('X_dev.shape= ',X_dev.shape, 'X_test.shape= ',X_test.shape, 'Y_dev.shape= ', Y_dev.shape, 'Y_test.shape= ', Y_test.shape)
np.savetxt("{}/Y_dev_bulked.csv".format(base_settings.OUTPUTS_PATH), Y_dev, delimiter=",")

# build the sequence model
model = main_kera.build_model(X_dev, Y_dev, None)
# analizing
main_kera.analize_model(model)
# compile_model
main_kera.compile_model(model,'binary_crossentropy' , 'adam', ['binary_accuracy','mean_squared_error', 'mean_absolute_error', 'mean_absolute_percentage_error', 'cosine_proximity'])
# train
main_kera.fit_model(model, X_dev, Y_dev, base_settings.EPOCH, base_settings.BATCH_SIZE, True)
# validate
main_kera.evaluate_model(model, X_test, Y_test)
# create prediction file
y_pred = main_kera.predict_model(model, X_test)
np.savetxt("{}/Y_prediction.csv".format(base_settings.OUTPUTS_PATH), y_pred, delimiter=",")
np.savetxt("{}/Y_real.csv".format(base_settings.OUTPUTS_PATH), Y_test, delimiter=",")

