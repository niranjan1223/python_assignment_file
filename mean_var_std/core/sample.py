
# axis=0--> columns
# axis=1-->rows

import numpy as np


def arr_mean(array):
    return np.mean(array, axis=1)  # return arithmetic mean


def arr_var(array):
    return np.var(array, axis=0)  # return variance


def arr_std(array):
    k = np.std(array, axis=None)
    return k.round(11)  # return standard deviation