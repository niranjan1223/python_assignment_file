
# axis=0--> columns
# axis=1-->rows

import numpy as np
def min_max(Ans):
    l=sorted(np.min(Ans, axis = 1))
    return l[-1]