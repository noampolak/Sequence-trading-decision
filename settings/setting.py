import os
# setting file will store global variables and some more important values
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, '..')
HISTORY_INDEX_PATH = os.path.join(BASE_DIR, 'history_indexes')