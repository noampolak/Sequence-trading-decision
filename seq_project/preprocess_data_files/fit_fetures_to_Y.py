import numpy as np

def adjust_dates_of_fetures_and_Y_matrix(fetures_matrix, Y_matrix, first_row_to_delete):
    # first sort the 2 matrix for easy search
    fetures_matrix = fetures_matrix[fetures_matrix[:,0].argsort()]
    Y_matrix = Y_matrix[Y_matrix[:,0].argsort()]
    # run effciently on the matrix and remove the uniqe values
    # i  = 0
    # try:
    #     while True:
    #         if fetures_matrix[i,0] != Y_matrix[i,0]:
    #             if fetures_matrix[i,0] < Y_matrix[i,0]:
    #                 fetures_matrix = np.delete(fetures_matrix,i,axis=0)
    #             else:
    #                 Y_matrix = np.delete(Y_matrix,i,axis=0)
    #         else:
    #             i = i + 1
    # except:
    #     print('end of data for one of the matrix')
    #     if fetures_matrix.shape[0] > Y_matrix.shape[0]:
    #         fetures_matrix = np.delete(fetures_matrix, slice(i , fetures_matrix.shape[0]), 0)
    #     else:
    #         Y_matrix = np.delete(Y_matrix, slice(i , Y_matrix.shape[0]), 0)
    mask = np.zeros(fetures_matrix.shape[0],dtype=bool)
    mask[np.searchsorted(fetures_matrix[:,0], Y_matrix[:,0])] = 1
    fetures_matrix = fetures_matrix[mask]
    mask = np.zeros(Y_matrix.shape[0],dtype=bool)
    mask[np.searchsorted(Y_matrix[:,0], fetures_matrix[:,0])] = 1
    Y_matrix = Y_matrix[mask]
    fetures_matrix = fetures_matrix[first_row_to_delete:,:]
    Y_matrix = Y_matrix[first_row_to_delete:,:]
    print('fetures_matrix are ready to use')
    return fetures_matrix, Y_matrix
            
    