import os
import librosa

def load_ravdess(data_dir: str):
    """
    Loads the RAVDESS dataset from the given directory.
    RAVDESS files follow the naming convention:
    Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
    Vocal channel (01 = speech, 02 = song).
    Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
    Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
    Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
    Repetition (01 = 1st repetition, 02 = 2nd repetition).
    Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

    For TruthShield, we map emotions to binary "stress":
    Stress (1): angry (05), fearful (06)
    Non-Stress (0): neutral (01), calm (02), happy (03), sad (04)
    (ignoring disgust/surprise for simplicity, or we could include them)
    """
    stress_emotions = ["05", "06"]
    non_stress_emotions = ["01", "02", "03", "04"]

    audio_files = []
    labels = []

    if not os.path.exists(data_dir):
        print(f"Warning: Dataset directory {data_dir} does not exist.")
        return audio_files, labels

    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".wav"):
                parts = file.split("-")
                if len(parts) == 7:
                    emotion = parts[2]
                    
                    if emotion in stress_emotions:
                        label = 1
                    elif emotion in non_stress_emotions:
                        label = 0
                    else:
                        continue # Skip unmapped emotions

                    audio_files.append(os.path.join(root, file))
                    labels.append(label)

    return audio_files, labels
