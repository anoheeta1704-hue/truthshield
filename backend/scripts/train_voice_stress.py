import os
import sys
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Add the backend root to the Python path so we can import from app
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, backend_root)

from app.services.feature_extraction import extract_features
from dataset_loader import load_ravdess

# Configuration
DATA_DIR = os.path.join(backend_root, "data", "ravdess")
MODELS_DIR = os.path.join(backend_root, "models")
MODEL_PATH = os.path.join(MODELS_DIR, "voice_stress_xgb.json")

def train_model():
    print(f"Loading RAVDESS dataset from: {DATA_DIR}")
    print("Download the dataset from https://zenodo.org/record/1188976")
    print("Extract the 'Audio_Speech_Actors_01-24.zip' contents into the data/ravdess/ folder.")
    print("Expected structure: data/ravdess/Actor_01/03-01-01-01-01-01-01.wav\n")

    audio_files, labels = load_ravdess(DATA_DIR)

    if not audio_files:
        print("Error: No audio files found. Please ensure the RAVDESS dataset is placed in the correct directory.")
        return

    print(f"Found {len(audio_files)} valid audio files for training.")
    print("Extracting features (this may take a while)...")

    X = []
    y = []

    for idx, (filepath, label) in enumerate(zip(audio_files, labels)):
        if idx % 100 == 0:
            print(f"Processed {idx}/{len(audio_files)} files...")
        
        try:
            with open(filepath, "rb") as f:
                audio_buffer = f.read()
            features = extract_features(audio_buffer)
            X.append(features)
            y.append(label)
        except Exception as e:
            # Skip files that fail (e.g., too short, silent, or invalid)
            pass

    X = np.array(X)
    y = np.array(y)

    print(f"Feature extraction complete. Feature matrix shape: {X.shape}")

    if len(X) < 10:
        print("Error: Not enough valid samples to train a model.")
        return

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost Classifier
    print("Training XGBoost classifier...")
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric='logloss'
    )
    model.fit(X_train, y_train)

    # Evaluate
    print("\nEvaluating model on test set...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Non-Stress", "Stress"]))

    # Save model
    os.makedirs(MODELS_DIR, exist_ok=True)
    model.save_model(MODEL_PATH)
    print(f"\nModel successfully saved to {MODEL_PATH}")
    print("The Voice Stress API is now ready for use!")

if __name__ == "__main__":
    train_model()
