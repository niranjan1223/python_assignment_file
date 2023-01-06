import numpy as np


def floor_arr(array):
    array = np.array(array)
    np.set_printoptions(legacy='1.13')
    return np.floor(array)
def ceil_arr(array):
    array = np.array(array)
    return np.ceil(array)
def rint_arr(array):
    array = np.array(array)
    return np.rint(array)