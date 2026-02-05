// import React, { useState } from "react";

// function App() {
//   const [result, setResult] = useState(null);

//   const handleTest = async () => {
//     const response = await fetch("http://127.0.0.1:8000/");
//     const data = await response.json();
//     setResult(data.message || JSON.stringify(data));
//   };

//   return (
//     <div className="App">
//       <h1>Voice Detector Frontend</h1>
//       <button onClick={handleTest}>Test Backend</button>
//       {result && <p>Backend says: {result}</p>}
//     </div>
//   );
// }

// export default App;

// import React, { useState } from "react";

// function App() {
//   const [file, setFile] = useState(null);
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);

//   // Handle file selection
//   const handleFileChange = (event) => {
//     setFile(event.target.files[0]);
//     setResult(null);
//   };

//   // Convert file to Base64 and send to backend
//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select a .wav file first!");
//       return;
//     }

//     setLoading(true);

//     try {
//       // Convert file to Base64
//       const reader = new FileReader();
//       reader.readAsDataURL(file);
//       reader.onloadend = async () => {
//         const base64Audio = reader.result.split(",")[1]; // remove prefix
//         // console.log("Sending body:", JSON.stringify({ audio: base64Audio }));
//         console.log("Sending request to backend at http://127.0.0.1:8000/predict");
//         console.log("Payload:", JSON.stringify({ audio: base64Audio }));

//         // Send to backend
//         // const response = await fetch("http://127.0.0.1:8000/predict", {
//         //   method: "POST",
//         //   headers: { "Content-Type": "application/json" },
//         //   body: JSON.stringify({ audio: base64Audio }),
//         // });

//         const response = await fetch("http://127.0.0.1:8000/api/voice-detection", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//     "x-api-key": "sk_test_123456789"   // must match backend API_KEY
//   },
//   body: JSON.stringify({
//     language: "Tamil",
//     audioFormat: "mp3",
//     audioBase64: base64Audio
//   })
// });

//         if (!response.ok) {
//           throw new Error("Backend error: " + response.statusText);
//         }

//         const data = await response.json();
//         setResult(data);
//         setLoading(false);
//       };
//     } catch (error) {
//       console.error("Error:", error);
//       setResult("Error: " + error.message);
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="App" style={{ textAlign: "center", marginTop: "50px" }}>
//       <h1>🎤 Voice Detector Frontend</h1>

//       <input
//         type="file"
//         accept=".wav,.mp3,.ogg,audio/*"
//         onChange={handleFileChange}
//         style={{ margin: "20px" }}
//       />
//       {file && <p>Selected file: {file.name}</p>}


//       <button onClick={handleUpload} disabled={loading}>
//         {loading ? "Analyzing..." : "Upload & Detect"}
//       </button>

//       {result && (
//   <div style={{ marginTop: "20px" }}>
//     <h2>Result:</h2>
//     <p><strong>Classification:</strong> {result.classification}</p>
//     <p><strong>Confidence:</strong> {(result.confidence_score * 100).toFixed(2)}%</p>
//   </div>
// )}
//     </div>
//   );
// }

// export default App;



import React, { useState } from "react";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);

  // Handle file selection
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setResult(null); // reset previous result
  };

  // Handle upload and detection
  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select an MP3 file first.");
      return;
    }

    const reader = new FileReader();
    reader.onloadend = async () => {
      // Strip "data:audio/mp3;base64," prefix
      const base64Audio = reader.result.split(",")[1];

      try {
        const response = await fetch("http://127.0.0.1:8000/api/voice-detection", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "x-api-key": "sk_test_123456789" // must match backend API_KEY
          },
          body: JSON.stringify({
            language: "Tamil",        // or English/Hindi/Malayalam/Telugu
            audioFormat: "mp3",
            audioBase64: base64Audio
          })
        });

        const data = await response.json();
        setResult(data);
      } catch (error) {
        console.error("Error uploading file:", error);
        setResult({ status: "error", message: "Failed to fetch" });
      }
    };

    reader.readAsDataURL(selectedFile);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🎤 Voice Detector Frontend</h1>

      <input type="file" accept="audio/mp3" onChange={handleFileChange} />
      {selectedFile && <p>Selected file: {selectedFile.name}</p>}

      <button onClick={handleUpload} style={{ marginTop: "10px" }}>
        Upload & Detect
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          {result.status === "success" ? (
            <>
              <p>Classification: {result.classification}</p>
              <p>
                Confidence:{" "}
                {result.confidenceScore
                  ? (result.confidenceScore * 100).toFixed(2) + "%"
                  : "N/A"}
              </p>
              <p>Explanation: {result.explanation}</p>
            </>
          ) : (
            <p style={{ color: "red" }}>Error: {result.message}</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;