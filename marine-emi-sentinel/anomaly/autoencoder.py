
import numpy as np, torch
from torch import nn
class Net(nn.Module):
    def __init__(self,d,latent=4):
        super().__init__(); h=max(8,2*latent)
        self.net=nn.Sequential(nn.Linear(d,h),nn.ReLU(),nn.Linear(h,latent),nn.ReLU(),
                               nn.Linear(latent,h),nn.ReLU(),nn.Linear(h,d))
    def forward(self,x): return self.net(x)
class AutoencoderDetector:
    def __init__(self,epochs=50,latent=4,lr=1e-3,seed=7):
        self.epochs=epochs; self.latent=latent; self.lr=lr; torch.manual_seed(seed)
    def fit(self,X):
        X=np.asarray(X,np.float32); self.mean_=X.mean(0); self.std_=X.std(0)+1e-6
        Z=(X-self.mean_)/self.std_; self.model=Net(Z.shape[1],self.latent)
        opt=torch.optim.Adam(self.model.parameters(),lr=self.lr); xt=torch.tensor(Z)
        for _ in range(self.epochs):
            opt.zero_grad(); rec=self.model(xt); loss=((rec-xt)**2).mean(); loss.backward(); opt.step()
        self.threshold_=float(np.quantile(self.score(X),.99)); return self
    def score(self,X):
        Z=(np.asarray(X,np.float32)-self.mean_)/self.std_
        with torch.no_grad(): rec=self.model(torch.tensor(Z)).numpy()
        return ((Z-rec)**2).mean(1)
    def predict(self,X): return (self.score(X)>=self.threshold_).astype(int)
