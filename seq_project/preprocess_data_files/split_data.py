import numpy as np

def split_to_dev_and_test(X, Y, Y_for_pred_test,val_size, test_size, start_row):
    return X[start_row:X.shape[0]-test_size-val_size, :,:], X[X.shape[0]-test_size-val_size:X.shape[0]-test_size, :,:],X[X.shape[0]-test_size:, :,:], Y[start_row:Y.shape[0]-test_size-val_size], Y[Y.shape[0]-test_size-val_size:Y.shape[0]-test_size], Y[Y.shape[0]-test_size:],Y_for_pred_test[start_row:Y.shape[0]-test_size], Y_for_pred_test[Y.shape[0]-test_size:]

# for Recurrent neural network it is needed to take all the dev data and split him to bulk of 200 for examples
def create_bulk_matrix(X, Y, bulk):
    print('X.shape[0]=', X.shape[0], 'X.shape[1] =', X.shape[1], 'bulk=', bulk)
    print('X.shape[1] *bulk= ' , X.shape[1] *bulk)
    print('Y.shape[0]= ' , Y.shape[0] , 'Y.shape[1]= ' , Y.shape[1])
    print('Y[:,1].shape= ' , Y[:,1].shape)
    
    X = np.concatenate((X, Y[:,1:]),1)
    # set the date column in the X matrix +1 to visualize the    situation of not knowing the future but try to predict Y
    X[:,0] += 1
    bulk_matrix_X = np.zeros(shape=(X.shape[0], bulk, X.shape[1] ))
    # bulk_matrix_Y = np.zeros(shape=(Y.shape[0], Y.shape[1] ,bulk))
    # create bulk from the bulk - get the bulk size before
    for i in range(bulk, X.shape[0]):
        print('i = ', i)
        # print('X[bulk*i:bulk,:].flatten() = ' , X[i:i+bulk,:].reshape(1, bulk, X.shape[1] ))
        # print('X[bulk*i:bulk,:].flatten().shape(0) = ' , X[i:i+bulk,:].reshape(1, X.shape[1] ,bulk).shape[0])
        # print('Y[bulk*i:bulk,:].flatten().shape(0) = ' ,Y[i:i+bulk,:].flatten().shape[0])
        bulk_matrix_X[i] = X[i-bulk:i,:].reshape(1,bulk, X.shape[1] )
        # bulk_matrix_Y[i] = Y[i:i+bulk,:].reshape(1, X.shape[1] ,bulk)
    
    return bulk_matrix_X ,Y[:,1]