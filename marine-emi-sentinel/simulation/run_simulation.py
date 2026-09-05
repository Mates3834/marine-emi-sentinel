
import json,numpy as np
from pathlib import Path
from models.ship_power_model import load_profile
from models.emi_generator import generate_emi
from dsp.nlms import nlms
from dsp.rls import rls
from dsp.kalman_filter import kalman_adaptive_filter
from dsp.features import extract_features
def simulate(scenario="normal",seed=None):
    c=json.loads((Path(__file__).resolve().parents[1]/"config"/"default.json").read_text())
    seed=c["seed"] if seed is None else seed; fs=c["sample_rate"]
    t=np.arange(0,c["duration"],1/fs)
    ls=scenario if scenario in {"load_increase","load_reduction","oscillatory","load_shedding"} else "normal"
    loads=load_profile(t,ls)
    useful,main,ref=generate_emi(t,loads["total"],c["fundamental_hz"],c["switching_hz"],
        scenario,c["reference_correlation"],c["sensor_noise_std"],seed)
    order=c["filter_order"]; n,_,_=nlms(main,ref,order); r,_,_=rls(main,ref,order)
    k,_,_=kalman_adaptive_filter(main,ref,order)
    feat={name:extract_features(sig,fs,loads["total"].mean(),c["fundamental_hz"])
          for name,sig in {"raw":main,"nlms":n,"rls":r,"kalman":k}.items()}
    return {"t":t,"loads":loads,"useful":useful,"main":main,"reference":ref,
            "nlms":n,"rls":r,"kalman":k,"features":feat}
