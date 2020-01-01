import numpy as np

def split_to_dev_and_test(X, Y, test_size):
    return X[:-test_size, :], X[test_size:, :], Y[:-test_size, :], Y[test_size:, :]

# for Recurrent neural network it is needed to take all the dev data and split him to bulk of 200 for examples
def create_bulk_matrix(X, Y, bulk):
    print('X.shape[0]=', X.shape[0], 'X.shape[1] =', X.shape[1], 'bulk=', bulk)
    print('X.shape[1] *bulk= ' , X.shape[1] *bulk)
    print('Y.shape[0]= ' , Y.shape[0] , 'Y.shape[1]= ' , Y.shape[1])
    print('Y[:,1].shape= ' , Y[:,1].shape)
    # add one more column to X - the indcation of previos buying from the Y matrix
    
    X = np.concatenate((X, Y[:,1:]),1)
    # set the date column in the X matrix +1 to visualize the situation of not knowing the future but try to predict Y
    X[:,0] += 1
    bulk_matrix_X = np.zeros(shape=(X.shape[0], X.shape[1] ,bulk))
    # bulk_matrix_Y = np.zeros(shape=(Y.shape[0], Y.shape[1] ,bulk))
    for i in range(X.shape[0] - bulk):
        print('i = ', i)
        print('X[bulk*i:bulk,:].flatten() = ' , X[i:i+bulk,:].reshape(1, X.shape[1] ,bulk))
        print('X[bulk*i:bulk,:].flatten().shape(0) = ' , X[i:i+bulk,:].reshape(1, X.shape[1] ,bulk).shape[0])
        # print('Y[bulk*i:bulk,:].flatten().shape(0) = ' ,Y[i:i+bulk,:].flatten().shape[0])
        bulk_matrix_X[i] = X[i:i+bulk,:].reshape(1, X.shape[1] ,bulk)
        # bulk_matrix_Y[i] = Y[i:i+bulk,:].reshape(1, X.shape[1] ,bulk)
    
    return bulk_matrix_X ,Y[:,1]