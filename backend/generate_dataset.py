import pyttsx3
import sounddevice as sd
import soundfile as sf
import os

# Make sure data folder exists
os.makedirs("./data", exist_ok=True)

# 1. Generate AI voice samples using pyttsx3 (Text-to-Speech)
def generate_ai_voice(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ AI voice saved: {filename}")

generate_ai_voice("Hello, this is an AI generated voice sample.", "./data/ai1.wav")
generate_ai_voice("Hackathon projects are fun when AI helps.", "./data/ai2.wav")

# 2. Record Human voice samples using microphone
def record_human_voice(filename, duration=5, samplerate=16000):
    print(f"🎙️ Recording human voice for {duration} seconds... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"✅ Human voice saved: {filename}")

record_human_voice("./data/human1.wav", duration=5)
record_human_voice("./data/human2.wav", duration=5)