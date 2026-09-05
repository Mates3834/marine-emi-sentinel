
import numpy as np
class StandardizedThresholdDetector:
    def __init__(self,threshold=3.): self.threshold=threshold
    def fit(self,X):
        X=np.asarray(X); self.mean_=X.mean(0); self.std_=X.std(0)+1e-8; return self
    def score(self,X): return np.abs((np.asarray(X)-self.mean_)/self.std_).max(1)
    def predict(self,X): return (self.score(X)>=self.threshold).astype(int)
