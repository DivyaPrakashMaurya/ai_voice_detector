# Voice Detector – Neural Forensics for AI vs Human Speech

Voice Detector is a full‑stack hackathon project that analyzes audio samples to classify voices as **AI‑generated** or **human**.  
It combines a neon cyberpunk frontend with a FastAPI backend to deliver real‑time forensic insights.

---

## 🚀 Features
- Upload MP3 audio or record via microphone
- Language selection (Tamil, English, Hindi, Malayalam, Telugu)
- Real‑time classification with confidence meter
- Explanations for each prediction
- History sidebar to track past analyses
- Futuristic neon cyberpunk UI

---

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Models:** Wav2Vec2 + custom classifier  
- **Deployment:** Backend on Render/Railway, Frontend on Netlify/Vercel  

---

## 📂 Project Structure

---

## ⚙️ Setup Instructions

### Backend (FastAPI)
1. Navigate to backend folder:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   http://127.0.0.1:8000/api/voice-detection

   🌐 Deployment
- Backend: Deploy on Render/Railway using backend/ folder.
- Frontend: Deploy on Netlify/Vercel using frontend/ folder.
- Update frontend BACKEND_URL to point to backend’s public API URL.

🏆 Hackathon Demo Flow
- User uploads or records audio.
- Frontend sends audio + language to backend API.
- Backend runs inference → returns classification, confidence, explanation.
- Frontend displays results with neon visualization + logs history.
