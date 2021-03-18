import os
# setting file will store global variables and some more important values
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_INDEX_PATH = os.path.join(BASE_DIR, 'history_indexes/2021')
Y_FILES = os.path.join(BASE_DIR, 'y_files/2021')
OUTPUTS_PATH = os.path.join(BASE_DIR, 'outputs')
CAPLEVERAGE = 5
WANTED_YIELD = 0.1
# optional - to delete the first rows and start only where most fetures are calculate right
FIRST_ROWS_TO_DELETE = 150
VAL_SET_SIZE = 380
TEST_SET_SIZE = 380
EPOCH = 450
BATCH_SIZE = 256
# first date to exam
START_DATE = 20060210
CLASS_WEIGHT = {0: 1.,
                1: 7.14,
                2: 10.2}
