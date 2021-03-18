import numpy as np


def clean_invalid_Values(matrix):
    # replace all nan with zeros
    cleaned_matrix = np.nan_to_num(matrix)
    idx = np.argwhere(np.all(cleaned_matrix[..., :] == 0, axis=0))
    cleaned_matrix = np.delete(cleaned_matrix, idx, axis=1)
    return cleaned_matrix