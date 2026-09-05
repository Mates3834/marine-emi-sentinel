# MarineEMI Sentinel

**Physics-Guided Adaptive EMI Monitoring and Anomaly Detection for Shipboard Power Systems**

Research-oriented, generic simulation framework combining a simplified shipboard
load model, synthetic EMI generation, dual-channel sensing, adaptive filtering,
spectral features, anomaly detection and residual monitoring.

## Pipeline

```text
Shipboard Load Model
        ↓
Synthetic EMI Generator
        ↓
Main + Reference Sensors
        ↓
NLMS / RLS / Kalman Adaptive Filtering
        ↓
STFT / PSD + Physics-Motivated Features
        ↓
Threshold / Isolation Forest / Autoencoder
        ↓
Physics-Guided Score Fusion
        ↓
Physics-Based Reference Model + Residual Monitoring
        ↓
Anomaly Decision
```

## Implemented components

- Generic shipboard load profiles
- Load-dependent synthetic EMI signatures
- Main/reference measurement channels
- NLMS adaptive cancellation
- RLS adaptive cancellation
- Kalman-based adaptive coefficient estimation
- PSD and STFT utilities
- RMS, harmonic ratios, THD-like ratio, band power, peak frequency,
  spectral centroid, entropy and kurtosis
- Statistical threshold detector
- Isolation Forest wrapper
- Autoencoder anomaly detector
- Physics-guided score fusion
- Load-aware feature reference model
- Residual monitoring
- Eight configurable synthetic scenarios
- Monte Carlo experiment utility

## Research question

> Can adaptive signal processing and physics-guided anomaly detection identify
> abnormal operating conditions in an isolated shipboard power system from
> electromagnetic-noise signatures under varying electrical loads?

## Scenarios

`S0` normal operation; `S1` propulsion-load increase; `S2` load reduction;
`S3` oscillatory demand; `S4` converter harmonic anomaly; `S5` generator
transient; `S6` load shedding; `S7` sensor contamination / unknown anomaly.

## Evaluation framework

The repository defines evaluation targets rather than publishing performance
claims. Adaptive-filter studies can evaluate noise attenuation, signal
distortion, SNR improvement, convergence and computation time. Anomaly studies
can evaluate precision, recall, F1, false-alarm rate, detection delay and AUROC.
Robustness studies can vary load, noise, reference-channel quality and model
mismatch.

## Run

```bash
pip install -r requirements.txt
python examples/full_pipeline_demo.py
pytest
```

## Important scope

All signals, loads, parameters and abnormal conditions are synthetic and generic.
The repository contains no real vessel measurements, real converter/generator
signatures, operational ship parameters, reactor physics, reactor protection
logic, plant procedures, HIL validation or claimed diagnostic performance.

The model-residual layer is intentionally described as a **physics-based
reference model**, not a validated digital twin. A stronger digital-twin claim
would require synchronization and validation against a physical system.

## Results

No performance results are published in the repository at this stage.
`results/` is intentionally empty and reserved for future controlled experiments.

## Future work

Potential extensions include real public datasets, synchronized electrical/EMI
measurements, contrastive self-supervised learning, domain adaptation,
uncertainty-aware anomaly detection, explainability, multi-sensor fusion and
real-time edge benchmarking.
