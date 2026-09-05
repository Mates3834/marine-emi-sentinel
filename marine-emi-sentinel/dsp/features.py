
import numpy as np
from scipy.signal import welch
from scipy.stats import kurtosis
FEATURE_NAMES=["rms","fundamental","h2_h1","h3_h1","thd","band_power",
"peak_frequency","spectral_centroid","spectral_entropy","spectral_kurtosis","load"]
def extract_features(x,fs,load,fundamental_hz=50.,band=(500,1600)):
    f,P=welch(np.asarray(x,float),fs=fs,nperseg=min(1024,len(x))); P=np.maximum(P,1e-15)
    near=lambda hz:int(np.argmin(np.abs(f-hz)))
    a1=np.sqrt(P[near(fundamental_hz)]); a2=np.sqrt(P[near(2*fundamental_hz)])
    a3=np.sqrt(P[near(3*fundamental_hz)]); den=max(a1,1e-12)
    mask=(f>=band[0])&(f<=min(band[1],fs/2))
    bp=np.trapezoid(P[mask],f[mask]) if mask.any() else 0.
    pn=P/P.sum()
    return np.array([np.sqrt(np.mean(np.asarray(x)**2)),a1,a2/den,a3/den,
    np.sqrt(a2*a2+a3*a3)/den,bp,f[np.argmax(P)],np.sum(f*P)/P.sum(),
    -np.sum(pn*np.log(pn))/np.log(len(pn)),kurtosis(P,fisher=False,bias=False),float(load)])
