
from scipy.signal import welch,stft
import numpy as np
def psd(x,fs): return welch(x,fs=fs,nperseg=min(1024,len(x)))
def spectrogram(x,fs):
    f,t,Z=stft(x,fs=fs,nperseg=min(256,len(x))); return f,t,np.abs(Z)**2
