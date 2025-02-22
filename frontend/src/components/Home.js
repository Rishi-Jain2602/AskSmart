import React from 'react';
import './styles/Home.css';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate()
  const handleNavigate = () =>{
    navigate("/upload")
  }
  return (
    <div className="home-container">
      <h1 className="home-title">Welcome to AskSmart</h1>
      <p className="home-description">
        AskSmart is a powerful document retrieval system that allows you to upload and process various formats such as PDF, DOCX, JSON, and TXT. 
        Our advanced AI technology retrieves relevant information and generates context-aware responses to your queries. 
      </p>
      <p className="home-supported-formats">
        <strong>Supported Formats:</strong> PDF, DOCX, JSON, TXT
      </p>
      <button className="home-button" onClick={handleNavigate}>Get Started</button>
    </div>
  );
}
