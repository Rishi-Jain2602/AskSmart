import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import './styles/Upload.css'

export default function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadResponse, setUploadResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setUploadResponse(null); // Reset previous response when new file is selected
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile) return;

    setIsLoading(true); // Start loading
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch("http://127.0.0.1:8000/Rag/upload", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setUploadResponse(data);

      if (data.doct_id) {
        localStorage.setItem('doct_id', data.doct_id);
        setTimeout(() => {
          navigate("/chat");
        }, 3000);
      }else{
        alert("Error in uploading document")
      }

    } catch (error) {
      console.error("Error uploading file:", error);
    } finally {
      setIsLoading(false); // Stop loading in all cases
    }
  };

  return (
    <div className='container'>
      <form className='upload-form' onSubmit={handleSubmit}>
        <label htmlFor="formFileLg" className="form-label">
          Upload Your Document Here
        </label>
        <input
          className="form-control form-control-lg"
          id="formFileLg"
          type="file"
          onChange={handleFileChange}
        />
        <button type="submit" className="btn btn-primary mt-3">Upload</button>
      </form>

      <div className="status-section">
        {isLoading && (
          <div className="mt-3 spinner-text">
            <FontAwesomeIcon icon={faSpinner} spin /> Uploading... Please wait.
          </div>
        )}
        {uploadResponse && (
          <div className="mt-3">
            <p>Filename: {uploadResponse.filename}</p>
            <p>{uploadResponse.message}</p>
            <p className="text-success">Upload successful! Redirecting to chat Page...</p>
          </div>
        )}
      </div>
    </div>
  );
}