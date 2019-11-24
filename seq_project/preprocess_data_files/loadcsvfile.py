import os
import glob
import pandas
# load scv file and concat all of them

def load_file_to_csv(path):
    df = pandas.read_csv(path, parse_dates=['Date'])
    return df

# load all the files in dir path - return list of data frames from the files beening loaded
def load_all_csv_files_in_path(path):
    # get all files in dir_Path which are in csv format 
    extension = 'csv'
    os.chdir(path)
    file_names = glob.glob('*.{}'.format(extension))
    print(file_names)
    files_df = []
    for csv_file in file_names:
        print(csv_file)
        files_df.append(load_file_to_csv(os.path.join(path,csv_file)))
    print('files_df=',len(files_df))
    return files_df
def merge_all_data_frames_by_date_field(list_of_date_frames):
    left = list_of_date_frames.pop(0)
    for df in list_of_date_frames:
        left = pandas.merge(left, df, on='Date',how='outer')
    return left