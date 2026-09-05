import numpy as np
from dsp.nlms import nlms
from dsp.rls import rls
from dsp.kalman_filter import kalman_adaptive_filter
def test_shapes():
 x=np.random.default_rng(1).normal(size=300); r=np.random.default_rng(2).normal(size=300)
 for fn in (nlms,rls,kalman_adaptive_filter):
  e,y,w=fn(x,r,8); assert e.shape==x.shape and y.shape==x.shape and w.shape==(8,)
