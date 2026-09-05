import numpy as np
from simulation.run_simulation import simulate
from anomaly.threshold_detector import StandardizedThresholdDetector
X=np.array([simulate("normal",s)["features"]["kalman"] for s in range(20,35)])
d=StandardizedThresholdDetector().fit(X)
d.score(simulate("converter_harmonic",99)["features"]["kalman"][None,:])
print("Anomaly pipeline executed; score intentionally not published.")
