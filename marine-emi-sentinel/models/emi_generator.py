
import numpy as np
def generate_emi(t,load,fundamental_hz=50.,switching_hz=650.,scenario="normal",
                 reference_correlation=.85,sensor_noise_std=.04,seed=7):
    rng=np.random.default_rng(seed); load=np.asarray(load); ph=rng.uniform(0,2*np.pi,5)
    useful=((.25+.20*load)*np.sin(2*np.pi*fundamental_hz*t+ph[0])+
            (.07+.05*load)*np.sin(2*np.pi*2*fundamental_hz*t+ph[1])+
            (.04+.04*load)*np.sin(2*np.pi*3*fundamental_hz*t+ph[2])+
            (.05+.08*load)*np.sin(2*np.pi*switching_hz*t+ph[3]))
    if scenario=="converter_harmonic":
        useful += .18*np.sin(2*np.pi*2*switching_hz*t+ph[4])
    elif scenario=="generator_transient":
        c=.55*t[-1]; env=np.exp(-((t-c)/(.05*t[-1]))**2)
        useful += .35*env*np.sin(2*np.pi*fundamental_hz*t)
    elif scenario=="sensor_contamination":
        useful += .12*rng.standard_normal(len(t))
    common=.16*rng.standard_normal(len(t)); ind=.16*rng.standard_normal(len(t))
    rho=float(np.clip(reference_correlation,0,.999))
    ref=rho*common+np.sqrt(1-rho**2)*ind+sensor_noise_std*rng.standard_normal(len(t))
    main=useful+common+sensor_noise_std*rng.standard_normal(len(t))
    return useful,main,ref
