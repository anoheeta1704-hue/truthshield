import librosa
import numpy as np

def extract_features(audio_buffer: bytes) -> np.ndarray:
    """
    Extracts acoustic features from an audio buffer using Librosa.
    Features: MFCC (13), Pitch (F0 mean), Jitter, Shimmer, ZCR (mean)
    """
    import io
    import soundfile as sf
    import warnings
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Load audio from memory
        y, sr = sf.read(io.BytesIO(audio_buffer))

    # Convert stereo to mono if necessary
    if len(y.shape) > 1:
        y = np.mean(y, axis=1)
        
    # Ensure audio is sufficiently long (at least 1 second)
    if len(y) < sr:
        raise ValueError("Audio is too short for meaningful feature extraction.")

    # Check for silence-only audio
    rms = librosa.feature.rms(y=y)
    if np.mean(rms) < 1e-4:
        raise ValueError("Audio contains only silence.")

    features = []

    # 1. MFCC (13 coefficients)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfccs.T, axis=0)
    features.extend(mfcc_mean)

    # 2. Pitch (Fundamental Frequency F0) using librosa.yin
    f0 = librosa.yin(y, fmin=50, fmax=500)
    f0_valid = f0[f0 > 0]
    pitch_mean = np.mean(f0_valid) if len(f0_valid) > 0 else 0
    features.append(pitch_mean)

    # 3. Zero Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = np.mean(zcr)
    features.append(zcr_mean)

    # Placeholder logic for Jitter and Shimmer (using basic perturbations)
    # Proper jitter/shimmer requires precise peak picking, estimating with diffs
    if len(f0_valid) > 1:
        jitter = np.mean(np.abs(np.diff(f0_valid)))
    else:
        jitter = 0
    features.append(jitter)

    if len(rms[0]) > 1:
        shimmer = np.mean(np.abs(np.diff(rms[0])))
    else:
        shimmer = 0
    features.append(shimmer)

    # Total 13 (MFCC) + 1 (Pitch) + 1 (ZCR) + 1 (Jitter) + 1 (Shimmer) = 17 features
    return np.array(features, dtype=np.float32)
