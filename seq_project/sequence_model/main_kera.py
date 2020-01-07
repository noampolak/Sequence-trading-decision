import numpy as np
from trade_models import trade_dec_model
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform

def build_model(X, Y, model_type):
    data_shape = X.shape
    model = trade_dec_model(data_shape)
    return model

def analize_model(model):
    model.summary()
def compile_model(model, loss='binary_crossentropy' , optimizer='adam',metrics=['accuracy']): 
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


def fit_model(model, X, Y, epochs =50, batch_size =32, shuffle=True):
    model.fit(X, Y, epochs = epochs, batch_size = batch_size, shuffle=shuffle)

def evaluate_model(model, X_test, Y_test):
    loss, acc = model.evaluate(X_test, Y_test)
    print("Test loss = ", loss)
    print("Test accuracy = ", acc)