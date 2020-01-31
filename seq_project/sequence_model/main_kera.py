import numpy as np
from .trade_models import trade_dec_model
from helpers import to_one_hot
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform

def build_model(X, Y, model_type):
    data_shape = (X.shape)[-2:]
    print('data_shape = ' , data_shape)
    Y_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y)
    try:
        model = trade_dec_model(data_shape, Y_one_hot.shape[1])
    except:
        # case Y is binary vector
        model = trade_dec_model(data_shape, 1)
    return model

def analize_model(model):
    model.summary()
def compile_model(model, loss='categorical_crossentropy' , optimizer='adam',metrics=['categorical_accuracy']): 
    
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


def fit_model(model, X, Y, epochs =50, batch_size =32, shuffle=True,class_weight=None):
    Y_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y)
    model.fit(X, Y_one_hot, epochs = epochs, batch_size = batch_size, shuffle=shuffle,class_weight=class_weight)

def evaluate_model(model, X_test, Y_test, batch_size =32, callbacks=['BaseLogger']):
    print("X_test shape  = ", X_test.shape)
    print("Y_test shape  = ", Y_test.shape)
    Y_test_one_hot = to_one_hot.convert_vector_to_one_hot_vector(Y_test)
    score = model.evaluate(X_test, Y_test_one_hot, batch_size)
    print("Test score = ", score)
    
def predict_model(model, X_test):
    return model.predict(X_test)

def save_model(model,filename):
    model.save(filename)