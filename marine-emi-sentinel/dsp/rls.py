
import numpy as np
def rls(main,reference,order=16,forgetting=.995,delta=10.):
    main=np.asarray(main,float); ref=np.asarray(reference,float); w=np.zeros(order)
    P=delta*np.eye(order); y=np.zeros_like(main); e=np.zeros_like(main)
    pad=np.r_[np.zeros(order-1),ref]
    for n in range(len(main)):
        x=pad[n:n+order][::-1]; Px=P@x; g=Px/(forgetting+x@Px)
        y[n]=w@x; e[n]=main[n]-y[n]; w+=g*e[n]
        P=(P-np.outer(g,x)@P)/forgetting
    return e,y,w
