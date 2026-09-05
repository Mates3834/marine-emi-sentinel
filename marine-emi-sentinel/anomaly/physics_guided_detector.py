
import numpy as np
def fuse_scores(ae,physics,residual,normal_ae,normal_physics,normal_residual,weights=(.4,.3,.3)):
    norm=lambda x,ref:np.asarray(x)/(np.quantile(ref,.95)+1e-9)
    w=np.asarray(weights,float); w/=w.sum()
    return w[0]*norm(ae,normal_ae)+w[1]*norm(physics,normal_physics)+w[2]*norm(residual,normal_residual)
