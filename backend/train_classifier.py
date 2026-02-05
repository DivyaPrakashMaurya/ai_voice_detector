# import os
# import numpy as np
# import librosa
# import torch
# from transformers import Wav2Vec2Processor, Wav2Vec2Model
# from sklearn.linear_model import LogisticRegression
# import joblib
# classifier = joblib.load("voice_classifier.pkl")


# # Load Wav2Vec2
# processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
# model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")

# def extract_embeddings(file_path, target_sr=16000):
#     y, sr = librosa.load(file_path, sr=target_sr)
#     inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#     embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
#     return embeddings

# X, y = [], []

# # Example dataset folders
# # human_folder = "dataset/human"
# # ai_folder = "dataset/ai"
# human_folder = "../dataset/human"
# ai_folder = "../dataset/ai"

# for f in os.listdir(human_folder):
#     emb = extract_embeddings(os.path.join(human_folder, f))
#     X.append(emb[0])
#     y.append(0)  # Human

# for f in os.listdir(ai_folder):
#     emb = extract_embeddings(os.path.join(ai_folder, f))
#     X.append(emb[0])
#     y.append(1)  # AI

# X = np.array(X)
# y = np.array(y)

# clf = LogisticRegression(max_iter=1000)
# clf.fit(X, y)

# joblib.dump(clf, "voice_classifier.pkl")
# print("✅ Classifier trained and saved as voice_classifier.pkl")

import os
import numpy as np
import librosa
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2Model
from sklearn.linear_model import LogisticRegression
import joblib

# Load Wav2Vec2
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")

def extract_embeddings(file_path, target_sr=16000):
    y, sr = librosa.load(file_path, sr=target_sr)
    inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).cpu().numpy()

X, y = [], []

human_folder = "dataset/human"
ai_folder = "dataset/ai"

for f in os.listdir(human_folder):
    emb = extract_embeddings(os.path.join(human_folder, f))
    X.append(emb[0])
    y.append(0)  # Human

for f in os.listdir(ai_folder):
    emb = extract_embeddings(os.path.join(ai_folder, f))
    X.append(emb[0])
    y.append(1)  # AI

X = np.array(X)
y = np.array(y)

classifier = LogisticRegression(max_iter=1000)
classifier.fit(X, y)

joblib.dump(classifier, "backend/voice_classifier.pkl")
print("✅ Classifier trained and saved as backend/voice_classifier.pkl")