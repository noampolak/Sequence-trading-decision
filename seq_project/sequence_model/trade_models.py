import numpy as np
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation, BatchNormalization
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform


def trade_dec_model(input_shape, Y_num_column):
    """
    Function creating the trade_dec_model model's graph.
    
    Arguments:
    input_shape -- shape of the input, usually (max_len,)

    Returns:
    model -- a model instance in Keras
    """
    
    ### START CODE HERE ###
    # Define sentence_indices as the input of the graph, it should be of shape input_shape and dtype 'int32' (as it contains indices).
    features =  Input(shape = input_shape, dtype = 'float32')
    
    
    # Propagate features through your batch_layer, you get back the data Normalized 
    batch_layer = BatchNormalization()(features)
    # batch_layer = features
    # Propagate the embeddings through an LSTM layer with 128-dimensional hidden state
    # Be careful, the returned output should be a batch of sequences.
    X = LSTM(input_shape[0]*2, return_sequences=True)(batch_layer)
    # Add dropout with a probability of 0.5
    X = Dropout(0.2)(X)
    # Propagate X trough another LSTM layer with 128-dimensional hidden state
    # Be careful, the returned output should be a single hidden state, not a batch of sequences.
    X = LSTM(input_shape[0]*2,return_sequences=False)(X)
    # Add dropout with a probability of 0.5
    X = Dropout(0.2)(X)
    X = Dense(input_shape[0]*3 ,activation='relu')(X)
    X = Dense(input_shape[0]*2 ,activation='relu')(X)
    X = Dense(input_shape[0] ,activation='relu')(X)
    # Propagate X through a Dense layer with softmax activation to get back a batch of 5-dimensional vectors.
    if Y_num_column > 1:
        X = Dense(Y_num_column,activation='softmax')(X)
        # Add a softmax activation
        X = Activation('softmax')(X)
    else:
        X = Dense(Y_num_column,activation='sigmoid')(X)

    # Create Model instance which Normalize features into X.
    model = Model(inputs=[features],outputs=X)
    
    ### END CODE HERE ###
    
    return model