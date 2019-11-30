import pandas
from preprocess_data_files.loadcsvfile import convert_column_to_float

def rolling_mv(df_col,moving_average):
    return df_col.rolling(moving_average).sum()
def ewm_mv(df_col,moving_average):
    return df_col.ewm(span=moving_average).mean()


def add_moving_average_to_data_frame(df, moving_average, col_num, mv_type='moving_average'):
    moving_average_types = {
    'moving_average' : rolling_mv,
    'ewm' : ewm_mv
    }
    func = moving_average_types.get(mv_type, lambda: "Invalid type")
    try:
        mv_col = func(df.ix[:,col_num], moving_average)
    except:
        df.ix[:,col_num] = convert_column_to_float(df, col_num)
        mv_col = func(df.ix[:,col_num], moving_average)

    df.insert(len(df.columns), "{}{}{}".format(col_num,mv_type,moving_average), mv_col)
    return df

def add_list_of_moving_average_to_data_frame(df, moving_average_list):
    df_len = len(df.columns)
    for col in range(1,df_len):
        for moving_average in moving_average_list: 
            print('col=', col)
            print('moving_average=', moving_average)
            df = add_moving_average_to_data_frame(df, moving_average, col, 'moving_average')
            df = add_moving_average_to_data_frame(df, moving_average, col, 'ewm')

    return df
