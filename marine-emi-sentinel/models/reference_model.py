
import numpy as np
class FeatureReferenceModel:
    def fit(self,loads,features):
        X=np.c_[np.ones(len(loads)),np.asarray(loads)]
        self.coef_,*_=np.linalg.lstsq(X,np.asarray(features),rcond=None); return self
    def predict(self,loads):
        return np.c_[np.ones(len(loads)),np.asarray(loads)]@self.coef_
