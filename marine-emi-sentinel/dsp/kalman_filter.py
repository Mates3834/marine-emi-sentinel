
import numpy as np
def kalman_adaptive_filter(main,reference,order=16,q=1e-5,r=.02):
    main=np.asarray(main,float); ref=np.asarray(reference,float); w=np.zeros(order)
    P=np.eye(order); Q=q*np.eye(order); y=np.zeros_like(main); e=np.zeros_like(main)
    pad=np.r_[np.zeros(order-1),ref]
    for n in range(len(main)):
        x=pad[n:n+order][::-1]; P=P+Q; K=(P@x)/(x@P@x+r)
        y[n]=w@x; e[n]=main[n]-y[n]; w=w+K*e[n]
        P=(np.eye(order)-np.outer(K,x))@P
    return e,y,w
