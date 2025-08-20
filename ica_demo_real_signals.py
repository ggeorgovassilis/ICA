import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
from scipy.io import wavfile

CLIP1="./audio/clips/receiver1.wav"
CLIP2="./audio/clips/receiver2.wav"
CLIP3="./audio/clips/receiver3.wav"
# Load signals from WAV files in audio/clips/
rate1, s1 = wavfile.read(CLIP1)
rate2, s2 = wavfile.read(CLIP2)
rate3, s3 = wavfile.read(CLIP3)

# Ensure signals have the same length
min_len = min(len(s1), len(s2), len(s3))
s1 = s1[:min_len].astype(float)
s2 = s2[:min_len].astype(float)
s3 = s3[:min_len].astype(float)

# Use the loaded signals directly as observed signals (no further mixing)
observed_signals = np.c_[s1, s2, s3]

observed_signals /= observed_signals.std(axis=0)

# Compute ICA
ica = FastICA(n_components=3)
reconstructed_signal = ica.fit_transform(observed_signals)  # Reconstruct signals
A_ = ica.mixing_  # Get estimated mixing matrix

# Plot results

models = [observed_signals, reconstructed_signal]
names = ['Observed signals', 'ICA estimated sources']
num_rows = len(models)
colors = ['C0', 'C1', 'C2']
plt.figure(figsize=(9, 2.5 * num_rows))

# Compute best match between estimated sources (no true sources available)
estimated_sources = reconstructed_signal.T
for i, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(num_rows, 1, i)
    plt.title(name)
    for idx, sig in enumerate(model.T):
        plt.plot(sig, color=colors[idx % len(colors)])
plt.tight_layout()
plt.savefig("ica_demo_real_signals.png")

# Save estimated sources as WAV files
from scipy.io.wavfile import write

# Normalize each estimated source to int16 range
est_sources = reconstructed_signal  # shape: (n_samples, n_components)
max_vals = np.max(np.abs(est_sources), axis=0)
normalized_est = (est_sources / max_vals) * 32767
normalized_est = normalized_est.astype(np.int16)

# Use the sample rate from the first loaded file (assumed same for all clips)
for i in range(normalized_est.shape[1]):
    filename = f"audio/reconstructed/reconstructed_source_{i+1}.wav"
    print(f"Saving {filename}")
    write(filename, rate1, normalized_est[:, i])
