# import torch, base64, io, librosa, joblib
# import numpy as np
# from transformers import Wav2Vec2Processor, Wav2Vec2Model

# processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53")
# model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-large-xlsr-53")
# clf = joblib.load("voice_detector.pkl")

# def predict(base64_audio):
#     y, sr = librosa.load(io.BytesIO(base64.b64decode(base64_audio)), sr=16000)
#     inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)
#     with torch.no_grad():
#         embeddings = model(**inputs).last_hidden_state.mean(dim=1).numpy()
#     prediction = clf.predict(embeddings)[0]
#     confidence = max(clf.predict_proba(embeddings)[0])
#     explanation = "Synthetic harmonics detected" if prediction == "AI" else "Natural human prosody"
#     return {
#         "classification": prediction,
#         "confidence_score": float(confidence),
#         "explanation": explanation
#     }

# import torch, base64, io, librosa, joblib, os
# import numpy as np
# from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2Model

# # Path to local model cache
# LOCAL_MODEL_PATH = "./models/wav2vec2-large-xlsr-53"
# MODEL_NAME = "facebook/wav2vec2-large-xlsr-53"

# # Try local first, else fallback to HuggingFace Hub
# if os.path.isdir(LOCAL_MODEL_PATH):
#     print(f"Loading model from local path: {LOCAL_MODEL_PATH}")
#     feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(LOCAL_MODEL_PATH)
#     model = Wav2Vec2Model.from_pretrained(LOCAL_MODEL_PATH)
# else:
#     print(f"Local model not found, downloading from HuggingFace Hub: {MODEL_NAME}")
#     feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(MODEL_NAME)
#     model = Wav2Vec2Model.from_pretrained(MODEL_NAME)

# # Load your trained classifier
# # clf = joblib.load("voice_detector.pkl")
# clf = joblib.load("./models/voice_detector.pkl")
# def predict(base64_audio):
#     # Decode and load audio
#     y, sr = librosa.load(io.BytesIO(base64.b64decode(base64_audio)), sr=16000)

#     # Extract features
#     inputs = feature_extractor(y, sampling_rate=sr, return_tensors="pt", padding=True)

#     # Get embeddings
#     with torch.no_grad():
#         embeddings = model(**inputs).last_hidden_state.mean(dim=1).numpy()

#     # Classify
#     prediction = clf.predict(embeddings)[0]
#     confidence = max(clf.predict_proba(embeddings)[0])
#     explanation = "Synthetic harmonics detected" if prediction == "AI" else "Natural human prosody"

#     return {
#         "classification": prediction,
#         "confidence_score": float(confidence),
#         "explanation": explanation
#     }

# import base64
# import io
# import librosa
# import numpy as np
# import torch
# from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2Model
# import joblib

# # Load feature extractor + model
# feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("./models/wav2vec2-large-xlsr-53")
# model = Wav2Vec2Model.from_pretrained("./models/wav2vec2-large-xlsr-53")

# # Load classifier
# clf = joblib.load("./models/voice_detector.pkl")

# def predict(audio: str):
#     try:
#         # Decode Base64 string into raw audio bytes
#         audio_bytes = base64.b64decode(audio)
#         audio_buffer = io.BytesIO(audio_bytes)

#         # Librosa can handle both WAV and MP3 if audioread/ffmpeg are installed
#         y, sr = librosa.load(audio_buffer, sr=16000)

#         # Extract embeddings
#         inputs = feature_extractor(y, sampling_rate=sr, return_tensors="pt", padding=True)
#         with torch.no_grad():
#             embeddings = model(**inputs).last_hidden_state.mean(dim=1).numpy()

#         # Predict with classifier
#         prediction = clf.predict(embeddings)[0]
#         confidence = np.max(clf.predict_proba(embeddings))

#         return {
#             "classification": prediction,
#             "confidence_score": float(confidence)
#         }

#     except Exception as e:
#         return {"error": str(e)}

# import base64
# import io
# import numpy as np
# import librosa
# from sklearn.linear_model import LogisticRegression
# from transformers import Wav2Vec2Processor, Wav2Vec2Model
# import torch



# # Load pretrained Wav2Vec2 model + processor
# processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
# model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")

# # Example classifier (replace with your trained one)
# # classifier = LogisticRegression()

# import joblib
# classifier = joblib.load("voice_classifier.pkl")

# # ⚠️ In real use, load your trained classifier weights here
# # e.g., joblib.load("voice_classifier.pkl")

# def decode_audio(base64_audio: str, target_sr: int = 16000):
#     """Decode Base64 audio string into waveform array."""
#     audio_bytes = base64.b64decode(base64_audio)
#     audio_buffer = io.BytesIO(audio_bytes)
#     y, sr = librosa.load(audio_buffer, sr=target_sr)
#     return y, sr

# def extract_embeddings(y: np.ndarray, sr: int):
#     """Extract Wav2Vec2 embeddings from waveform."""
#     inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#     # Mean pooling over time dimension
#     embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
#     return embeddings

# def classify_voice(score: float) -> str:
#     """Multi-case classification based on probability score."""
#     if score >= 0.7:
#         return "AI"
#     elif score >= 0.6:
#         return "Likely AI"
#     elif score >= 0.4:
#         return "Uncertain"
#     elif score >= 0.3:
#         return "Likely Human"
#     else:
#         return "Human"

# def predict(base64_audio: str):
#     """Main prediction pipeline."""
#     # Decode audio
#     y, sr = decode_audio(base64_audio)

#     # Extract embeddings
#     embeddings = extract_embeddings(y, sr)

#     # Get probability of AI (assuming classifier outputs [Human, AI])
#     score = classifier.predict_proba(embeddings)[0][1]

#     # Classify with multi-case thresholds
#     label = classify_voice(score)

#     return {
#         "classification": label,
#         "confidence_score": float(score)
#     }

import base64, io, librosa, torch
import numpy as np
from transformers import Wav2Vec2Processor, Wav2Vec2Model
import joblib

# Load Wav2Vec2 + trained classifier
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")
classifier = joblib.load("backend/voice_classifier.pkl")

def decode_audio(base64_audio, target_sr=16000):
    audio_bytes = base64.b64decode(base64_audio)
    audio_buffer = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_buffer, sr=target_sr)
    return y, sr

def extract_embeddings(y, sr):
    inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).cpu().numpy()

def analyze_voice(base64_audio, language):
    try:
        y, sr = decode_audio(base64_audio)
        embeddings = extract_embeddings(y, sr)
        # score = classifier.predict_proba(embeddings)[0][1]
        score = float(classifier.predict_proba(embeddings)[0][1])
        label = "AI_GENERATED" if score >= 0.5 else "HUMAN"
        explanation = (
            "Unnatural pitch consistency and robotic speech patterns detected"
            if label == "AI_GENERATED"
            else "Natural variations in tone and rhythm detected"
        )

        return {
            "status": "success",
            "language": language,
            "classification": label,
            "confidenceScore": round(score, 2),
            "explanation": explanation,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}