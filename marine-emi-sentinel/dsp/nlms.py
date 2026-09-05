
import numpy as np
def nlms(main,reference,order=16,mu=.35,eps=1e-8):
    main=np.asarray(main,float); ref=np.asarray(reference,float); w=np.zeros(order)
    y=np.zeros_like(main); e=np.zeros_like(main); pad=np.r_[np.zeros(order-1),ref]
    for n in range(len(main)):
        x=pad[n:n+order][::-1]; y[n]=w@x; e[n]=main[n]-y[n]
        w += mu*e[n]*x/(eps+x@x)
    return e,y,w
