
import numpy as np
def load_profile(t,scenario="normal"):
    t=np.asarray(t); p=np.full_like(t,.50,dtype=float)
    aux=np.full_like(t,.14); hotel=np.full_like(t,.10); critical=np.full_like(t,.18)
    if scenario=="load_increase": p += .15*(t>=.45*t[-1])
    elif scenario=="load_reduction": p -= .15*(t>=.45*t[-1])
    elif scenario=="oscillatory": p += .10*np.sin(2*np.pi*.35*t)
    elif scenario=="load_shedding":
        hotel *= (t<.55*t[-1]); aux *= np.where(t<.55*t[-1],1.,.45)
    return {"propulsion":p,"auxiliary":aux,"hotel":hotel,"critical":critical,
            "total":p+aux+hotel+critical}
