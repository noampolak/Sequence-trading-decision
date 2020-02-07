import pandas
from preprocess_data_files.loadcsvfile import convert_column_to_float


def simple_delta(df_col,delta):
    return -df_col.diff(periods=delta)

def add_delta_to_data_frame(df, delta, col_num, mv_type='simple_delta'):
    delta_types = {
    'simple_delta' : simple_delta,
    }
    func = delta_types.get(mv_type, lambda: "Invalid type")
    try:
        mv_col = func(df.iloc[:,col_num], delta)
    except:
        df.iloc[:,col_num] = convert_column_to_float(df, col_num)
        mv_col = func(df.iloc[:,col_num], delta)
    print(len(df.columns))
    df.insert(len(df.columns), "{}{}{}".format(col_num,mv_type,delta), mv_col)

def add_list_of_deltas_to_data_frame(df, deltas_list):
    df_len = len(df.columns)
    print('df before adding is:',df)
    for col in range(1,df_len):
        for delta in deltas_list: 
            print('col=', col)
            print('moving_average=', delta)
            try:
                add_delta_to_data_frame(df, delta, col, 'simple_delta')
            except:
                print('not able to convert column' , col)
    print('df after adding is:',df)
    return df