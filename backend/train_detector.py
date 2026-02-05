import torch, librosa, joblib
import numpy as np
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2Model
from sklearn.linear_model import LogisticRegression

# Load Wav2Vec2 for embeddings
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("facebook/wav2vec2-large-xlsr-53")
model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-large-xlsr-53")

# Example dataset: replace with your own audio files
human_files = ["./data/human1.wav", "./data/human2.wav"]
ai_files = ["./data/ai1.wav", "./data/ai2.wav"]

X, y = [], []

def extract_embedding(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    inputs = feature_extractor(y, sampling_rate=sr, return_tensors="pt", padding=True)
    with torch.no_grad():
        return model(**inputs).last_hidden_state.mean(dim=1).numpy()

# Collect embeddings
for f in human_files:
    X.append(extract_embedding(f))
    y.append("Human")

for f in ai_files:
    X.append(extract_embedding(f))
    y.append("AI")

X = np.vstack(X)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X, y)

# Save classifier
joblib.dump(clf, "./models/voice_detector.pkl")
print("✅ voice_detector.pkl saved in ./models/")