import os
import glob
import pandas
from helpers import clean_number
# load csv file and concat all of them

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
    return merged_frame.sort_values('Date')

def fix_missing_data(data_frame):
    data_frame.fillna(0)

def convert_column_to_float(df,col_num):
    # return df.iloc[:,col_num].apply(clean_number.clean_number).astype('float')
    return df.iloc[:,col_num].str.replace('$', '').str.replace(',', '').str.replace('K', '').str.replace('M', '').str.replace('%', '').astype('float')
    # if df.iloc[:,col_num].str.contains('%').any():
    #     print("remove %")
    #     return df.iloc[:,col_num].str.rstrip('%').astype('float') / 100.0
    # if df.iloc[:,col_num].str.contains(',').any():
    #     print("convert to float")
    #     return df.iloc[:,col_num].str.rstrip(',').astype('float')
    # return df.iloc[:, col_num].apply(pandas.to_numeric)
    # return pandas.to_numeric(df.iloc[:,col_num], errors='coerce')

def convert_date_to_number(df_column):
    return df_column.dt.strftime("%Y%m%d").astype(int).to_numpy()

def convert_all_date_fields_to_number(df):
    g = df.columns.to_series().groupby(df.dtypes).groups
    g = {k.name: v for k, v in g.items()}
    if 'datetime64[ns]' in g:
        dates_fields = g['datetime64[ns]']
        for field in dates_fields:
            df[field] = convert_date_to_number(df[field])
    return df