
from sklearn.ensemble import IsolationForest
class IsolationForestDetector:
    def __init__(self,random_state=7): self.model=IsolationForest(random_state=random_state)
    def fit(self,X): self.model.fit(X); return self
    def score(self,X): return -self.model.score_samples(X)
    def predict(self,X): return (self.model.predict(X)==-1).astype(int)
