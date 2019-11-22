import os
import glob
import pandas
# load scv file and concat all of them

def load_file_to_csv(path):
    df = pandas.read_csv("../history_indexes/Brent Oil Futures Historical Data.csv", parse_dates=['Date'])
    return df

# load all the files in dir path - return list of data frames from the files beening loaded
def load_all_csv_files_in_path(dir_path):
    # get all files in dir_Path which are in csv format 
    extension = 'csv'
    os.chdir(dir_path)
    file_names = glob.glob('*.{}'.format(extension))
    # list_df = [load_file_to_csv()]
    # return list_df
    print(file_names)
