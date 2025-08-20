import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

# Generate sample data (3 signals)
N_SAMPLES = 4000
time = np.linspace(0, 8, N_SAMPLES)
s1 = np.sin(2 * time) + 0.3 * np.sin(7 * time)  # Signal 1 : sum of two sinusoids
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
source_signals = np.c_[s1, s2]
source_signals += 0.05 * np.random.normal(size=source_signals.shape)  # Add noise
source_signals /= source_signals.std(axis=0)  # Standardize data

# Mix data with phase shift for s1 in the first observer
phi = np.pi / 4  # phase shift (45 degrees)
A = np.array([[1, 1], [0.5, 2]])  # Mixing matrix for 2 sources and 2 observations
# For observer 0, use s1 with phase shift; for observer 1, use s1 as is
s1_phase = np.sin(2 * time + phi) + 0.3 * np.sin(7 * time + phi)
mixed_0 = A[0,0] * s1_phase + A[0,1] * source_signals[:,1]
mixed_1 = A[1,0] * source_signals[:,0] + A[1,1] * source_signals[:,1]
observed_signals = np.vstack([mixed_0, mixed_1]).T

# Compute ICA
ica = FastICA(n_components=2)
reconstructed_signal = ica.fit_transform(observed_signals)  # Reconstruct signals
A_ = ica.mixing_  # Get estimated mixing matrix

# Plot results

models = [observed_signals, source_signals, reconstructed_signal]
names = ['Mixed signals (observations)', 'True Sources', 'ICA estimated sources']
num_rows = len(models)
colors = ['C0', 'C1', 'C2']
plt.figure(figsize=(9, 2.5 * num_rows))

# Compute best match between true and estimated sources
from scipy.stats import pearsonr
true_sources = source_signals.T
estimated_sources = reconstructed_signal.T
cor_matrix = np.abs(np.corrcoef(true_sources, estimated_sources)[:len(true_sources), len(true_sources):])
matching = np.argmax(cor_matrix, axis=1)

for i, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(num_rows, 1, i)
    plt.title(name)
    if name == 'True Sources':
        for idx, sig in enumerate(model.T):
            plt.plot(sig, color=colors[idx % len(colors)])
            break
    elif name == 'ICA estimated sources':
        # Plot estimated sources in the order that best matches the true sources
        for idx, true_idx in enumerate(matching):
            plt.plot(estimated_sources[true_idx], color=colors[idx % len(colors)])
    else:
        for sig in model.T:
            plt.plot(sig)
plt.tight_layout()
plt.savefig("ica_simple_signals.png")
