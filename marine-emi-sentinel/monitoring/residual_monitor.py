
import numpy as np
def residual_score(measured,expected,weights=None):
    r=np.asarray(measured)-np.asarray(expected)
    if weights is None:return np.sum(r*r,axis=-1)
    return np.einsum("...i,ij,...j->...",r,np.asarray(weights),r)
