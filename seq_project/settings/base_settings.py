import os
# setting file will store global variables and some more important values
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_INDEX_PATH = os.path.join(BASE_DIR, 'history_indexes')
OUTPUTS_PATH = os.path.join(BASE_DIR, 'outputs')
CAPLEVERAGE = 5
WANTED_YIELD = 0.1