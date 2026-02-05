# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # # from inference_advanced import predict
# # from .inference_advanced import predict
# # from backend.inference_advanced import predict


# # app = FastAPI()

# # class AudioInput(BaseModel):
# #     audio: str  # Base64 string

# # @app.post("/detect-voice")
# # def detect_voice(input: AudioInput):
# #     return predict(input.audio)

# # from fastapi import FastAPI
# # from .inference_advanced import predict

# # app = FastAPI()

# # @app.get("/")
# # def read_root():
# #     return {"message": "Voice detector API is running!"}

# # @app.post("/predict")
# # def run_prediction(audio: str):
# #     return predict(audio)

# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware
# # from .inference_advanced import predict
# # from pydantic import BaseModel


# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],  # allow frontend
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # class AudioInput(BaseModel):
# #     audio: str   # Base64 string

# # # @app.get("/")
# # # def read_root():
# # #     return {"message": "Voice detector API is running!"}

# # @app.post("/predict")
# # def run_prediction(audio: str):
# #     return predict(audio)

# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware
# # from pydantic import BaseModel
# # from .inference_advanced import predict

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=[
# #         "http://localhost:3000",
# #         "http://127.0.0.1:3000"
# #     ],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# # # Define schema
# # class AudioInput(BaseModel):
# #     audio: str   # Base64 string

# # @app.post("/predict")
# # def run_prediction(input_data: AudioInput):
# #     return predict(input_data.audio)

# from fastapi import FastAPI, Header, HTTPException
# from pydantic import BaseModel
# from .inference_advanced import analyze_voice

# # Replace with your actual secret key
# API_KEY = "sk_test_123456789"

# app = FastAPI()

# class VoiceRequest(BaseModel):
#     language: str
#     audioFormat: str
#     audioBase64: str

# @app.post("/api/voice-detection")
# def voice_detection(request: VoiceRequest, x_api_key: str = Header(None)):
#     # API Key validation
#     if x_api_key != API_KEY:
#         raise HTTPException(status_code=401, detail={"status": "error", "message": "Invalid API key"})

#     # Language validation
#     supported = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
#     if request.language not in supported:
#         raise HTTPException(status_code=400, detail={"status": "error", "message": "Unsupported language"})

#     # Audio format validation
#     if request.audioFormat.lower() != "mp3":
#         raise HTTPException(status_code=400, detail={"status": "error", "message": "Only MP3 format supported"})

#     # Run inference
#     result = analyze_voice(request.audioBase64, request.language)
#     return result

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from .inference_advanced import analyze_voice
from fastapi.middleware.cors import CORSMiddleware

# Define your secret API key here
API_KEY = "sk_test_123456789"  # change this to any secret string you want

app = FastAPI()

# Allow frontend (React at localhost:3000) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

@app.post("/api/voice-detection")
def voice_detection(request: VoiceRequest, x_api_key: str = Header(None)):
    # API Key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail={"status": "error", "message": "Invalid API key"})

    # Language validation
    supported = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
    if request.language not in supported:
        raise HTTPException(status_code=400, detail={"status": "error", "message": "Unsupported language"})

    # Audio format validation
    if request.audioFormat.lower() != "mp3":
        raise HTTPException(status_code=400, detail={"status": "error", "message": "Only MP3 format supported"})

    # Run inference
    result = analyze_voice(request.audioBase64, request.language)
    return result