import base64, io, librosa

def decode_base64_audio(base64_str):
    audio_bytes = base64.b64decode(base64_str)
    audio_buffer = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_buffer, sr=16000)  # resample to 16kHz
    return y, sr