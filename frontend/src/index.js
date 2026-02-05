import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

const BACKEND_URL = "http://127.0.0.1:8000/api/voice-detection";
let selectedLang = 'Tamil';
let mediaRecorder;
let audioChunks = [];
let isRecording = false;
let history = JSON.parse(localStorage.getItem('forensic_history')) || [];

// // --- NEURAL BACKGROUND ANIMATION ---
// const canvas = document.getElementById('neuralCanvas');
// const ctx = canvas.getContext('2d');
// let particles = [];

// function initCanvas() {
//     canvas.width = window.innerWidth;
//     canvas.height = window.innerHeight;
//     particles = Array.from({length: 70}, () => ({
//         x: Math.random() * canvas.width,
//         y: Math.random() * canvas.height,
//         vx: (Math.random() - 0.5) * 0.4,
//         vy: (Math.random() - 0.5) * 0.4
//     }));
// }
// function animate() {
//     ctx.clearRect(0,0, canvas.width, canvas.height);
//     ctx.strokeStyle = 'rgba(0, 242, 255, 0.1)';
//     ctx.fillStyle = '#00f2ff';
//     particles.forEach((p, i) => {
//         p.x += p.vx; p.y += p.vy;
//         if(p.x<0 || p.x>canvas.width) p.vx*=-1;
//         if(p.y<0 || p.y>canvas.height) p.vy*=-1;
//         ctx.fillRect(p.x, p.y, 2, 2);
//         for(let j=i+1; j<particles.length; j++){
//             let d = Math.hypot(p.x-particles[j].x, p.y-particles[j].y);
//             if(d<150) { ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(particles[j].x, particles[j].y); ctx.stroke(); }
//         }
//     });
//     requestAnimationFrame(animate);
// }
// initCanvas(); animate();

// // --- LANGUAGE SELECTION ---
// document.querySelectorAll('.lang-btn').forEach(btn => {
//     btn.onclick = () => {
//         document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
//         btn.classList.add('active');
//         selectedLang = btn.dataset.lang;
//     };
// });

// // --- RECORDING ---
// async function toggleRecording() {
//     const btn = document.getElementById('recordBtn');
//     if (!isRecording) {
//         try {
//             const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
//             mediaRecorder = new MediaRecorder(stream);
//             audioChunks = [];
//             mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
//             mediaRecorder.onstop = async () => {
//                 const blob = new Blob(audioChunks, { type: "audio/mp3" });
//                 const base64 = await convertBlobToBase64(blob);
//                 sessionStorage.setItem("recordedAudio", base64);
//             };
//             mediaRecorder.start();
//             btn.innerText = "CEASE_INTERCEPT";
//             btn.classList.add('recording-active');
//             isRecording = true;
//         } catch (err) {
//             alert("MIC_ACCESS_DENIED: Check hardware permissions.");
//         }
//     } else {
//         mediaRecorder.stop();
//         btn.innerText = "MIC_INTERCEPT";
//         btn.classList.remove('recording-active');
//         isRecording = false;
//     }
// }

// // --- UTILS ---
// const convertBlobToBase64 = blob => new Promise((resolve) => {
//     const reader = new FileReader();
//     reader.onloadend = () => resolve(reader.result.split(',')[1]);
//     reader.readAsDataURL(blob);
// });

// // --- MAIN ANALYSIS ---
// async function analyzeVoice() {
//     const fileInput = document.getElementById('audioFile');
//     const display = document.getElementById('resultDisplay');
//     const classLabel = document.getElementById('classification');

//     let base64Audio;
//     if (fileInput.files[0]) {
//         base64Audio = await convertBlobToBase64(fileInput.files[0]);
//     } else if (sessionStorage.getItem("recordedAudio")) {
//         base64Audio = sessionStorage.getItem("recordedAudio");
//     } else {
//         return alert("ACCESS DENIED: NO AUDIO SIGNAL DETECTED");
//     }

//     display.style.display = 'block';
//     classLabel.innerText = "COMPUTING...";
//     classLabel.style.color = "var(--neon-blue)";

//     try {
//         const response = await fetch(BACKEND_URL, {
//             method: "POST",
//             headers: { 
//                 "Content-Type": "application/json",
//                 "x-api-key": "sk_test_123456789" // must match backend
//             },
//             body: JSON.stringify({ 
//                 language: selectedLang,
//                 audioFormat: "mp3",
//                 audioBase64: base64Audio
//             })
//         });

//         const data = await response.json();
//         updateUI(data);
//         saveToHistory(data);
//     } catch (err) {
//         classLabel.innerText = "LINK_FAILURE";
//         console.error(err);
//     }
// }

// // --- UPDATE UI ---
// function updateUI(data) {
//     const classBox = document.getElementById('classification');
//     classBox.innerText = data.classification.toUpperCase();
//     classBox.style.color = data.classification.toLowerCase().includes('ai') ? '#ff003c' : '#00ff41';

//     if (data.confidenceScore !== undefined) {
//         document.getElementById('confidenceText').innerText = (data.confidenceScore * 100).toFixed(2) + "%";
//         document.getElementById('confidenceFill').style.width = (data.confidenceScore * 100) + "%";
//     } else {
//         document.getElementById('confidenceText').innerText = "N/A";
//         document.getElementById('confidenceFill').style.width = "0%";
//     }
//     document.getElementById('explanation').innerText = data.explanation || "No explanation provided.";
// }

// // --- HISTORY ---
// function saveToHistory(data) {
//     const entry = { ...data, timestamp: new Date().toLocaleTimeString(), lang: selectedLang };
//     history.unshift(entry);
//     localStorage.setItem('forensic_history', JSON.stringify(history.slice(0, 15)));
//     renderHistory();
// }

// function renderHistory() {
//     const list = document.getElementById('historyList');
//     list.innerHTML = history.map(item => `
//         <div class="history-item">
//             <div style="color: ${item.classification.toLowerCase().includes('ai') ? '#ff003c' : '#00ff41'}">
//                 ${item.classification.split('-')[0]} // ${(item.confidenceScore*100).toFixed(2)}%
//             </div>
//             <div style="font-size: 0.6rem; opacity: 0.5;">
//                 ${item.lang.toUpperCase()} | ${item.timestamp}
//             </div>
//         </div>
//     `).join('');
// }

// renderHistory();
