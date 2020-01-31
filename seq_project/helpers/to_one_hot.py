from numpy import array
from keras.utils import to_categorical

def convert_vector_to_one_hot_vector(numpy_array):
    return to_categorical(numpy_array)