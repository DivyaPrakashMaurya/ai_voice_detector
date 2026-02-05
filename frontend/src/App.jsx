import React, { useState } from "react";
import { motion } from "framer-motion";

function App() {
  const [result, setResult] = useState(null);

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onloadend = async () => {
      const base64Audio = reader.result.split(",")[1];
      const response = await fetch("http://localhost:8000/detect-voice", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ audio: base64Audio }),
      });
      const data = await response.json();
      setResult(data);
    };
    reader.readAsDataURL(file);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-purple-500 to-indigo-600 text-white">
      <motion.h1
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl font-bold mb-6"
      >
        AI Voice Detector 🎙️
      </motion.h1>

      <input type="file" accept="audio/*" onChange={handleFileUpload} />

      {result && (
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          className="mt-6 p-6 bg-white text-black rounded-lg shadow-lg"
        >
          <h2 className="text-xl font-bold">
            {result.classification.toUpperCase()}
          </h2>
          <p>Confidence: {(result.confidence_score * 100).toFixed(2)}%</p>
          <p>{result.explanation}</p>
        </motion.div>
      )}
    </div>
  );
}

export default App;