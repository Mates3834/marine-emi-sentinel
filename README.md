# MarineEMI Sentinel

## Physics-Guided Adaptive EMI Monitoring and Anomaly Detection for Shipboard Power Systems

MarineEMI Sentinel is a research-oriented simulation framework for investigating **adaptive electromagnetic interference (EMI) monitoring and anomaly detection in isolated shipboard electrical power systems**.

The project combines adaptive signal processing, spectral analysis, physics-motivated feature extraction, machine-learning-based anomaly detection, and model-residual monitoring within a unified condition-monitoring architecture.

The framework includes:

- Generic shipboard electrical load modelling
- Load-dependent synthetic EMI generation
- Dual-channel main/reference sensing
- NLMS adaptive interference cancellation
- RLS adaptive interference cancellation
- Kalman-based adaptive coefficient estimation
- Power Spectral Density (PSD) analysis
- Short-Time Fourier Transform (STFT)
- Physics-motivated spectral feature extraction
- Statistical threshold-based anomaly detection
- Isolation Forest
- Autoencoder-based anomaly detection
- Physics-guided anomaly-score fusion
- Load-aware physics-based reference modelling
- Residual-based condition monitoring
- Configurable operating and anomaly scenarios
- Monte Carlo experiment support

All signals, operating conditions, and system parameters used in the public implementation are **synthetic and generic**.

---

# 1. Research Question

The central research question is:

> **Can adaptive signal processing and physics-guided anomaly detection identify abnormal operating conditions in an isolated shipboard power system from electromagnetic-noise signatures under varying electrical loads?**

The project investigates whether EMI characteristics can provide an additional source of information for condition monitoring without relying exclusively on conventional electrical measurements.

---

# 2. Motivation

Modern shipboard electrical systems may contain multiple interacting electrical subsystems, including:

- Electrical generation
- Power conversion
- Propulsion loads
- Auxiliary loads
- Critical electrical loads
- Hotel loads

Changes in electrical operating conditions can influence electromagnetic-noise characteristics.

Rather than treating EMI exclusively as unwanted interference, this project investigates whether spectral characteristics of electromagnetic signals can also be used as **condition-monitoring information**.

The main concept is:

```text
Electrical Operating State
          ↓
   EMI Characteristics
          ↓
Adaptive Signal Processing
          ↓
Spectral Representation
          ↓
Condition Features
          ↓
Anomaly Detection
```

---

# 3. System Architecture

The complete research framework is organized as:

```text
                 Shipboard Load Model
                         │
                         ▼
                Synthetic EMI Model
                         │
               ┌─────────┴─────────┐
               │                   │
               ▼                   ▼
         Main EM Channel     Reference Channel
               │                   │
               └─────────┬─────────┘
                         ▼
              Adaptive EMI Cancellation
                 ┌───────┼───────┐
                 ▼       ▼       ▼
                NLMS    RLS    Kalman
                 └───────┼───────┘
                         ▼
                   Cleaned Signal
                         │
                         ▼
                    STFT / PSD
                         │
                         ▼
              Spectral Feature Layer
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
        Threshold    Isolation     Autoencoder
        Detector      Forest
            │            │            │
            └────────────┼────────────┘
                         ▼
              Physics-Guided Fusion
                         │
                         ▼
               Reference Model
                         │
                         ▼
                Residual Monitor
                         │
                         ▼
               Anomaly Assessment
```

The framework therefore combines both **signal-driven** and **model-driven** condition-monitoring approaches.

---

# 4. Shipboard Electrical Load Model

A simplified shipboard electrical demand model is used to generate operating conditions.

The total electrical load is represented as:

\[
P_{\mathrm{load}}(t)
=
P_{\mathrm{prop}}(t)
+
P_{\mathrm{aux}}(t)
+
P_{\mathrm{hotel}}(t)
+
P_{\mathrm{critical}}(t)
\]

where:

- \(P_{\mathrm{prop}}\) represents propulsion-related demand
- \(P_{\mathrm{aux}}\) represents auxiliary loads
- \(P_{\mathrm{hotel}}\) represents hotel/service loads
- \(P_{\mathrm{critical}}\) represents critical electrical loads

The load model is intentionally generic.

It is not intended to reproduce the electrical architecture of a specific vessel.

---

# 5. Load-Dependent EMI Generation

The synthetic EMI model represents electromagnetic signatures using combinations of:

- Fundamental-frequency components
- Harmonic components
- Converter-like switching components
- Broadband noise
- Load-dependent amplitude variations
- Transient spectral components
- Synthetic abnormal spectral behaviour

A generic signal can be represented as:

\[
s(t)
=
\sum_{k=1}^{N_h}
A_k(t)
\sin(2\pi kf_0t+\phi_k)
+
\sum_{j=1}^{N_s}
B_j(t)
\sin(2\pi f_{sw,j}t+\theta_j)
+
n(t)
\]

where:

- \(f_0\) is the fundamental frequency
- \(f_{sw}\) represents switching-frequency components
- \(A_k\) represents harmonic amplitudes
- \(B_j\) represents switching-component amplitudes
- \(n(t)\) represents broadband noise

The amplitudes can vary according to electrical load.

Conceptually:

```text
Ship Load
    │
    ▼
Operating Condition
    │
    ▼
Harmonic / Switching Characteristics
    │
    ▼
Synthetic EMI Signature
```

---

# 6. Dual-Channel Measurement Architecture

The monitoring architecture uses two channels.

## Main Channel

The main sensor contains the desired EMI signature together with correlated interference:

\[
x[n]
=
s[n]
+
v[n]
\]

where:

- \(s[n]\) represents the signal component associated with the electrical system
- \(v[n]\) represents unwanted correlated interference

## Reference Channel

The reference sensor provides an observation correlated with the interference:

\[
r[n]
\approx
v[n]
\]

The reference signal is used by the adaptive filter to estimate the unwanted component.

---

# 7. Adaptive EMI Cancellation

The adaptive filter produces an estimate:

\[
\hat v[n]
\]

and the cleaned signal becomes:

\[
e[n]
=
x[n]
-
\hat v[n]
\]

Three adaptive filtering approaches are included:

```text
NLMS
RLS
Kalman-Based Adaptive Filtering
```

The purpose is to provide multiple adaptive signal-processing approaches under the same synthetic monitoring conditions.

---

# 8. NLMS Adaptive Filtering

Normalized Least Mean Squares provides a computationally lightweight adaptive-filtering baseline.

The filter output is:

\[
\hat v[n]
=
\mathbf{w}^{T}[n]\mathbf{r}[n]
\]

and:

\[
e[n]
=
x[n]
-
\hat v[n]
\]

The coefficient update is:

\[
\mathbf{w}[n+1]
=
\mathbf{w}[n]
+
\frac{
\mu e[n]\mathbf{r}[n]
}{
\epsilon+\|\mathbf{r}[n]\|^2
}
\]

where:

- \(\mu\) is the adaptation rate
- \(\epsilon\) prevents numerical instability

---

# 9. RLS Adaptive Filtering

Recursive Least Squares is included as a second adaptive-filtering method.

RLS minimizes an exponentially weighted error criterion:

\[
J[n]
=
\sum_{k=0}^{n}
\lambda^{n-k}e^2[k]
\]

where:

\[
0<\lambda\leq1
\]

is the forgetting factor.

Compared with NLMS, RLS provides a different trade-off between:

```text
Adaptation Speed
        ↕
Computational Complexity
```

The repository provides both approaches so that they can later be evaluated under identical scenarios.

---

# 10. Kalman-Based Adaptive Filtering

The project also formulates adaptive filter coefficients as a dynamic state.

The coefficient model is:

\[
\mathbf{w}_{k+1}
=
\mathbf{w}_{k}
+
\mathbf{q}_{k}
\]

and the measurement relationship can be represented as:

\[
x_k
=
\mathbf{r}_{k}^{T}\mathbf{w}_{k}
+
v_k
\]

The Kalman estimator recursively updates the adaptive coefficients.

This implementation should be interpreted as:

> **Kalman-based adaptive coefficient estimation**

rather than a high-fidelity physical electromagnetic state estimator.

---

# 11. Signal Processing Pipeline

After adaptive cancellation, the signal is analysed in both time and frequency domains.

```text
Adaptive Filter Output
          │
          ├─────────────► PSD
          │
          └─────────────► STFT
                              │
                              ▼
                         Spectrogram
```

---

# 12. Power Spectral Density

Power Spectral Density provides information about the distribution of signal energy across frequency.

\[
S_{xx}(f)
\]

can reveal:

- Fundamental components
- Harmonic components
- Switching-frequency activity
- Broadband spectral changes
- Abnormal spectral peaks

---

# 13. Short-Time Fourier Transform

For non-stationary behaviour, the framework includes STFT analysis:

\[
X(\tau,f)
=
\sum_n
x[n]w[n-\tau]
e^{-j2\pi fn}
\]

This provides a time-frequency representation:

```text
Time
  ↓
Spectral Evolution
  ↓
Transient / Anomaly Observation
```

---

# 14. Physics-Motivated Feature Extraction

The framework extracts interpretable spectral features.

The current feature vector includes:

```text
RMS energy
Fundamental amplitude
H2/H1
H3/H1
THD-like harmonic ratio
Band power
Peak frequency
Spectral centroid
Spectral entropy
Spectral kurtosis
Electrical load level
```

---

# 15. Harmonic Features

The relative second harmonic is:

\[
R_2
=
\frac{H_2}{H_1}
\]

and the third-harmonic ratio is:

\[
R_3
=
\frac{H_3}{H_1}
\]

A THD-like quantity is represented as:

\[
THD
=
\frac{
\sqrt{H_2^2+H_3^2+\cdots+H_N^2}
}{
H_1
}
\]

These features provide interpretable information about spectral changes.

---

# 16. Band Power

Frequency-band energy can be represented as:

\[
P_{\mathrm{band}}
=
\int_{f_1}^{f_2}
S_{xx}(f)\,df
\]

This is useful for monitoring activity in selected spectral regions.

---

# 17. Spectral Centroid

The spectral centroid is:

\[
f_c
=
\frac{
\sum_f fS_{xx}(f)
}{
\sum_f S_{xx}(f)
}
\]

It represents the approximate centre of spectral energy.

---

# 18. Spectral Entropy

Normalized spectral energy is defined as:

\[
p_i
=
\frac{P_i}{\sum_jP_j}
\]

and spectral entropy is:

\[
H_s
=
-
\sum_i
p_i\log(p_i)
\]

This provides information about spectral complexity and energy distribution.

---

# 19. Feature Vector

The resulting physics-motivated feature representation can be written as:

\[
\mathbf{z}_{phys}
=
[
E_{RMS},
H_1,
H_2/H_1,
H_3/H_1,
THD,
P_{band},
f_{peak},
f_c,
H_s,
K_s,
P_{load}
]^T
\]

This vector forms the primary input to several anomaly-monitoring components.

---

# 20. Statistical Threshold Detector

The first anomaly-detection baseline uses deviations from normal feature statistics.

For feature \(i\):

\[
z_i
=
\frac{x_i-\mu_i}{\sigma_i}
\]

A generic anomaly score is:

\[
A_{stat}
=
\max_i |z_i|
\]

and an anomaly can be indicated when:

\[
A_{stat}
\geq
T
\]

This provides an interpretable baseline.

---

# 21. Isolation Forest

The project includes an Isolation Forest detector operating on extracted feature vectors.

```text
Physics Features
       │
       ▼
Isolation Forest
       │
       ▼
Anomaly Score
```

The method does not require labelled examples for every possible abnormal operating condition.

---

# 22. Autoencoder-Based Anomaly Detection

An autoencoder is included for learned anomaly detection.

The model follows:

```text
Feature Vector
      │
      ▼
   Encoder
      │
      ▼
Latent Representation
      │
      ▼
   Decoder
      │
      ▼
Reconstructed Features
```

The reconstruction error is:

\[
A_{AE}
=
\|
\mathbf{x}
-
\hat{\mathbf{x}}
\|_2^2
\]

The model can be trained using normal operating data.

Large reconstruction errors may indicate behaviour that differs from the learned normal distribution.

The current implementation is therefore described as **unsupervised/semi-supervised anomaly detection**, rather than claiming a general self-supervised learning framework.

---

# 23. Physics-Guided Anomaly Fusion

A central feature of the project is the combination of learned and physically interpretable information.

The fused score can be represented as:

\[
A_{PG}
=
\alpha A_{AE}
+
\beta A_{physics}
+
\gamma A_{residual}
\]

where:

- \(A_{AE}\) represents autoencoder reconstruction behaviour
- \(A_{physics}\) represents statistical/physics-feature deviation
- \(A_{residual}\) represents model-residual behaviour

and:

\[
\alpha+\beta+\gamma=1
\]

The fusion weights are configurable.

No claim is made that a particular weighting is universally optimal.

---

# 24. Physics-Based Reference Model

A load-aware reference model is included to estimate expected feature behaviour.

Conceptually:

\[
\hat{\mathbf{z}}
=
f(P_{load})
\]

where:

\[
\hat{\mathbf{z}}
\]

represents expected features for a given operating load.

The current implementation uses a lightweight load-to-feature relationship learned from nominal synthetic data.

---

# 25. Residual Monitoring

The residual between measured and expected features is:

\[
\mathbf{r}
=
\mathbf{z}_{measured}
-
\mathbf{z}_{expected}
\]

A residual score can be calculated as:

\[
J_r
=
\mathbf{r}^{T}
W
\mathbf{r}
\]

where:

\[
W
\]

is a configurable weighting matrix.

This creates a model-driven monitoring layer complementary to the data-driven anomaly detectors.

---

# 26. Why This Is Not Yet Called a Validated Digital Twin

The reference-model layer is intentionally described as:

> **Physics-Based Reference Model and Residual Monitoring**

rather than a validated digital twin.

A stronger digital-twin interpretation would require elements such as:

```text
Physical System
       │
       ▼
Synchronized Measurements
       │
       ▼
Validated Dynamic Model
       │
       ▼
Online State / Parameter Updating
       │
       ▼
Measured vs Predicted Behaviour
```

The current public project does not claim this level of physical validation.

---

# 27. Operating Scenarios

The simulation framework defines eight generic operating conditions.

| Scenario | Description |
|---|---|
| S0 | Normal steady operation |
| S1 | Propulsion load increase |
| S2 | Propulsion load reduction |
| S3 | Oscillatory propulsion demand |
| S4 | Converter harmonic anomaly |
| S5 | Generator transient |
| S6 | Load shedding |
| S7 | Sensor contamination / unknown anomaly |

These scenarios are synthetic and configurable.

---

# 28. Normal Operation

The normal scenario provides baseline EMI behaviour under nominal electrical loading.

This scenario can be used to generate normal data for:

- Statistical feature estimation
- Reference-model fitting
- Isolation Forest training
- Autoencoder training

---

# 29. Propulsion Load Changes

Step changes in propulsion-related electrical demand can be generated.

Conceptually:

\[
P_{prop}(t)
=
P_0+\Delta P
\]

or:

\[
P_{prop}(t)
=
P_0-\Delta P
\]

This allows the monitoring framework to distinguish operating-state changes from explicitly abnormal spectral behaviour.

---

# 30. Oscillatory Demand

A time-varying propulsion demand can be represented as:

\[
P_{prop}(t)
=
P_0
+
A\sin(2\pi f_pt)
\]

This introduces a non-stationary operating condition.

---

# 31. Converter Harmonic Anomaly

A synthetic additional switching-related component is introduced into the EMI signal.

This allows investigation of whether the spectral-monitoring pipeline can recognize changes that are not explained solely by load variation.

---

# 32. Generator Transient

A temporary fundamental-frequency disturbance can be introduced using a localized transient envelope.

Conceptually:

\[
s_{transient}(t)
=
A
e^{-\left(
\frac{t-t_0}{\sigma}
\right)^2}
\sin(2\pi f_0t)
\]

This creates a temporary non-stationary spectral event.

---

# 33. Load Shedding

Selected lower-priority load components can be reduced during the simulation.

This creates a rapid change in total electrical demand and therefore provides another operating-state transition for the monitoring framework.

---

# 34. Sensor Contamination / Unknown Anomaly

Additional broadband contamination can be introduced at the measurement level.

This scenario is useful for investigating the distinction between:

```text
Electrical-System Behaviour
```

and:

```text
Measurement / Sensor Contamination
```

It also provides a generic anomaly condition that is not represented simply as a load step.

---

# 35. Monte Carlo Framework

The project includes infrastructure for repeated simulations.

Parameters that can be varied in future studies include:

```text
Electrical load
Harmonic amplitudes
Switching components
Sensor noise
Reference correlation
Transient timing
Random phase
Model mismatch
```

The number of Monte Carlo runs is configurable.

The framework does **not** claim that a specific number of trials has already been used to establish statistical performance.

---

# 36. Evaluation Framework

The repository defines an evaluation methodology without publishing performance claims.

## Adaptive Filtering Metrics

Potential metrics include:

```text
Noise attenuation
Signal distortion
SNR improvement
Convergence behaviour
Computational time
```

An important distinction is maintained between:

```text
Removing Interference
```

and:

```text
Preserving the Desired Signal
```

A filter should therefore not be evaluated solely by output-energy reduction.

---

# 37. Anomaly Detection Metrics

Future controlled experiments can evaluate:

```text
Precision
Recall
F1-score
False-alarm rate
Detection delay
AUROC
```

These metrics are intentionally listed as evaluation targets rather than reported project results.

---

# 38. Robustness Evaluation

Potential robustness studies include:

```text
Sensor-noise sensitivity
Load uncertainty
Reference-channel quality
Model mismatch
Harmonic variability
Switching-frequency variation
Monte Carlo statistics
```

---

# 39. Repository Structure

```text
marine-emi-sentinel/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── config/
│   └── default.json
│
├── models/
│   ├── ship_power_model.py
│   ├── emi_generator.py
│   └── reference_model.py
│
├── dsp/
│   ├── nlms.py
│   ├── rls.py
│   ├── kalman_filter.py
│   ├── spectral_analysis.py
│   └── features.py
│
├── anomaly/
│   ├── threshold_detector.py
│   ├── isolation_forest.py
│   ├── autoencoder.py
│   └── physics_guided_detector.py
│
├── monitoring/
│   └── residual_monitor.py
│
├── simulation/
│   ├── scenarios.py
│   ├── run_simulation.py
│   └── monte_carlo.py
│
├── examples/
│   ├── adaptive_filter_demo.py
│   ├── anomaly_detection_demo.py
│   └── full_pipeline_demo.py
│
├── tests/
│   ├── test_filters.py
│   ├── test_features.py
│   └── test_scenarios.py
│
└── results/
    └── .gitkeep
```

---

# 40. Module Overview

| Module | Purpose |
|---|---|
| `ship_power_model.py` | Generic shipboard electrical-load profiles |
| `emi_generator.py` | Synthetic load-dependent EMI generation |
| `reference_model.py` | Load-aware expected-feature model |
| `nlms.py` | NLMS adaptive cancellation |
| `rls.py` | RLS adaptive cancellation |
| `kalman_filter.py` | Kalman-based adaptive coefficient estimation |
| `spectral_analysis.py` | PSD and STFT utilities |
| `features.py` | Physics-motivated spectral features |
| `threshold_detector.py` | Statistical anomaly baseline |
| `isolation_forest.py` | Isolation Forest detector |
| `autoencoder.py` | Autoencoder anomaly detector |
| `physics_guided_detector.py` | Multi-source anomaly-score fusion |
| `residual_monitor.py` | Model-residual calculation |
| `scenarios.py` | Scenario definitions |
| `run_simulation.py` | Integrated simulation pipeline |
| `monte_carlo.py` | Repeated simulation utility |

---

# 41. Installation

Clone the repository:

```bash
git clone <repository-url>
cd marine-emi-sentinel
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Main dependencies include:

```text
NumPy
SciPy
scikit-learn
PyTorch
Matplotlib
pytest
```

---

# 42. Running the Framework

Run the full pipeline demonstration:

```bash
python examples/full_pipeline_demo.py
```

Adaptive-filter demonstration:

```bash
python examples/adaptive_filter_demo.py
```

Anomaly-detection demonstration:

```bash
python examples/anomaly_detection_demo.py
```

Run tests:

```bash
pytest
```

---

# 43. Configuration

Generic simulation parameters are stored in:

```text
config/default.json
```

The configuration includes quantities such as:

```text
Sampling frequency
Simulation duration
Fundamental frequency
Synthetic switching frequency
Reference correlation
Sensor-noise level
Adaptive-filter order
Random seed
```

All default values are synthetic and are not associated with a real shipboard electrical system.

---

# 44. Current Scope

The current public implementation contains:

```text
Generic Shipboard Load Model
          ↓
Synthetic EMI Generation
          ↓
Dual-Channel Measurement
          ↓
Adaptive Filtering
          ↓
Spectral Analysis
          ↓
Physics-Motivated Features
          ↓
Machine-Learning Detectors
          ↓
Physics-Guided Fusion
          ↓
Reference-Model Residual
          ↓
Condition Monitoring
```

---

# 45. Current Limitations

The current framework does not contain:

- Real shipboard EMI measurements
- Real vessel electrical parameters
- Real converter signatures
- Real generator signatures
- Real propulsion-motor signatures
- Detailed electrical-network transient simulation
- Detailed electromagnetic field modelling
- Validated EMC/EMI models
- Real sensor calibration
- Hardware-in-the-loop validation
- Real-time embedded implementation
- Sea-trial validation
- Physical fault-injection experiments
- Validated digital-twin synchronization
- Reactor physics
- Neutron kinetics
- Reactor protection systems
- Nuclear safety logic
- Plant operating procedures

The project should therefore be interpreted as a **generic algorithm-development and research simulation framework for EMI-based condition monitoring**.

---

# 46. Future Extensions

Potential extensions include:

## Real Data

```text
Public EMI Dataset
        ↓
Signal Conditioning
        ↓
Feature Extraction
        ↓
Model Validation
```

## Multi-Sensor Monitoring

```text
EMI
+
Voltage
+
Current
+
Vibration
+
Temperature
        ↓
Sensor Fusion
        ↓
Condition Assessment
```

## Self-Supervised Representation Learning

Future versions could investigate contrastive or pretext-task learning rather than relying exclusively on autoencoder reconstruction.

## Uncertainty-Aware Monitoring

Potential methods include:

- Bayesian models
- Ensemble uncertainty
- Monte Carlo dropout
- Confidence calibration

## Explainable Anomaly Detection

Future detectors could estimate which physical features contributed most strongly to an anomaly decision.

## Online Adaptation

The reference model could be updated as operating conditions change.

---

# 47. Relationship Between Signal Processing and Condition Monitoring

The central research architecture can be summarized as:

```text
        Adaptive Signal Processing
                  │
                  ▼
            Cleaner Signal
                  │
                  ▼
           Spectral Features
                  │
         ┌────────┴────────┐
         ▼                 ▼
Physical Knowledge    Learned Model
         │                 │
         └────────┬────────┘
                  ▼
           Residual Analysis
                  │
                  ▼
          Anomaly Assessment
```

This allows classical signal-processing methods and modern data-driven monitoring methods to be investigated within the same framework.

---

# 48. Research Areas

The project relates to:

- Adaptive Signal Processing
- Electromagnetic Interference Monitoring
- Condition Monitoring
- Fault Detection and Diagnostics
- Marine Electrical Systems
- Shipboard Power Systems
- Kalman Filtering
- Machine Learning
- Anomaly Detection
- Physics-Guided Machine Learning
- Residual-Based Monitoring
- Digital-Twin-Oriented Modelling

---

# 49. Technologies

```text
Python
NumPy
SciPy
scikit-learn
PyTorch
Matplotlib
pytest
```

Methods represented in the framework include:

```text
NLMS
RLS
Kalman Filtering
PSD
STFT
Spectral Feature Extraction
Isolation Forest
Autoencoder
Residual Monitoring
Monte Carlo Simulation
```

---

# 50. Results Policy

This repository currently makes **no numerical performance claim**.

No values are reported for:

```text
SNR improvement
Noise attenuation
Precision
Recall
F1-score
AUROC
False-alarm rate
Detection delay
```

until a controlled evaluation is performed.

The:

```text
results/
```

directory is intentionally reserved for future validated experimental outputs.

This distinction is important because software functionality alone does not establish scientific performance.

---

# 51. Public Implementation Notice

This repository contains a **generic and sanitized research implementation**.

All:

- Electrical loads
- EMI signatures
- Harmonic amplitudes
- Switching frequencies
- Sensor-noise levels
- Operating scenarios
- Fault/anomaly conditions
- Monitoring thresholds
- Model parameters

are synthetic and intended for algorithm development.

System-specific, operational, proprietary, or restricted information is intentionally excluded.

---

# 52. Project Status

**Research-oriented simulation framework — active development**

Current pipeline:

```text
Shipboard Power State
        ↓
Synthetic EMI
        ↓
Adaptive Cancellation
        ↓
Spectral Analysis
        ↓
Physics Features
        ↓
Data-Driven Detection
        ↓
Model Residual
        ↓
Physics-Guided Monitoring
```

The next scientific stage is controlled comparative evaluation of the implemented methods under repeatable synthetic scenarios and, where appropriate, future validation using suitable physical or public measurement data.

---

# Author

**Mehmet Ateş**

Research interests:

- Autonomous Systems
- Guidance, Navigation and Control
- Marine Robotics
- Shipboard Power and Energy Systems
- State Estimation
- Adaptive Signal Processing
- Condition Monitoring
- Model Predictive Control
- Reinforcement Learning
- Physics-Guided Machine Learning
