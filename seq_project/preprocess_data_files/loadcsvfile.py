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
def merge_all_data_frames_by_date_field(list_of_data_frames):
    merged_frame = list_of_data_frames.pop(0)
    for df in list_of_data_frames:
        merged_frame = pandas.merge_ordered(merged_frame, df, fill_method='ffill', on='Date',how='outer')
        # merged_frame = pandas.merge_ordered(merged_frame, df, on='Date',how='outer')
    return merged_frame
def fix_missing_data(data_frame):
    data_frame.fillna(0)
def convert_column_to_float(df,col_num):
    print(col_num)
    print(df.iloc[:,col_num])
    if df.iloc[:,col_num].str.contains('%').any():
        print("remove %")
        return df.iloc[:,col_num].str.rstrip('%').astype('float') / 100.0
    if df.iloc[:,col_num].str.contains(',').any():
        print("convert to float")
        print(df.iloc[:,col_num].str.rstrip(','))
        return df.iloc[:,col_num].str.rstrip(',').astype('float') / 100.0
    print('df.iloc[:,col_num]: ',df.iloc[:,col_num])
    return df.iloc[:, col_num].apply(pandas.to_numeric)
    # return pandas.to_numeric(df.iloc[:,col_num], errors='coerce')