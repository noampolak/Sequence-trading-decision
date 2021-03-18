# This file contian prediction check of the model
# The tester will recieve the prediction, with the real data inculding the price- open, close and change
# and calculate the profit of the prediction file for CAPLEVERAGE and the WANTED_YIELD



def check_predictions_profit(predict_matrix, Y_matrix ,CAPLEVERAGE=5, WANTED_YIELD=0.1):
    """
    Check predict matrix for 3 columns (for now) 
    and calc the profit/loss

    :param predict_matrix: predict matrix with shape (n,3)
    :param Y_matrix: Y matrix  with shape (n,3)
    :param log_file: The log file
    :return: The engine to the ran games.
    """