import numpy as np

# This file contian prediction check of the model
# The tester will recieve the prediction, with the real data inculding the price- open, close and change
# and calculate the profit of the prediction file for CAPLEVERAGE and the WANTED_YIELD



def check_predictions_independent_profit(predict_matrix, Y_matrix ,Y_real_price_change, CAPLEVERAGE=5, WANTED_YIELD=0.1):
    """
    Check predict matrix for 3 columns (for now) 
    and calc the profit/loss

    :param predict_matrix: predict matrix with shape (n,3)
    :param Y_matrix: Y matrix  with shape (1,3)
    :param Y_real_price_change: y file with the price change yield
    :param CAPLEVERAGE: CAPLEVERAGE
    :param WANTED_YIELD: WANTED_YIELD
    :return: sum of the profit/loss in US dollars
    """
    
    # append the 3 matrixes
    auxiliary_column = np.argmax(predict_matrix, axis=1)
    auxiliary_column[(auxiliary_column==2)] = -1
    appended_matrixes = np.vstack((auxiliary_column, Y_matrix))
    appended_matrixes = np.vstack((appended_matrixes, Y_real_price_change))
    # create custom field with the independent profit/loss
    yield_column = 1000*CAPLEVERAGE * auxiliary_column * Y_real_price_change

    #return  the independent profit/loss
    return np.sum(yield_column)
    
def check_predictions_cumulative_profit(predict_matrix, Y_matrix ,Y_real_price_change, CAPLEVERAGE=5, WANTED_YIELD=0.1):
    """
    Check predict matrix for 3 columns (for now) 
    and calc the profit/loss

    :param predict_matrix: predict matrix with shape (n,3)
    :param Y_matrix: Y matrix  with shape (1,3)
    :param Y_real_price_change: y file with the price change yield
    :param CAPLEVERAGE: CAPLEVERAGE
    :param WANTED_YIELD: WANTED_YIELD
    :return: sum of the profit/loss in US dollars
    """
    
    # append the 3 matrixes


    # create custom field with the cumulative profit/loss

    #return  the cumulative profit/loss

