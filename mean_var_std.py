import numpy as np

def calculate(list):
    # check if list contains exact nine numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # create a 3x3 matrix from the list
    matrix = np.array(list).reshape(3, 3)

    calculations = dict()
    calculations["mean"] = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        np.mean(matrix),
    ]
    calculations["variance"] = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        np.var(matrix),
    ]
    calculations["standard deviation"] = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        np.std(matrix),
    ]
    calculations["max"] = [
        np.max(matrix, axis=0).tolist(),
        np.max(matrix, axis=1).tolist(),
        np.max(matrix),
    ]
    calculations["min"] = [
        np.min(matrix, axis=0).tolist(),
        np.min(matrix, axis=1).tolist(),
        np.min(matrix),
    ]
    calculations["sum"] = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        np.sum(matrix),
    ]

    return calculations
