import numpy as np
from dsp.features import extract_features
def test_features():
 fs=2000;t=np.arange(0,2,1/fs);z=extract_features(np.sin(2*np.pi*50*t),fs,.8);assert np.all(np.isfinite(z))
