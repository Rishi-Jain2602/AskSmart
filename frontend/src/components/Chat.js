import React, { useState,useEffect } from 'react';
import './styles/Chat.css';

function generateSessionId() {
  // Generate a simple random session ID.
  return Math.random().toString(36).substring(2, 10);
}

export default function Chat() {
  const [userMessages, setUserMessages] = useState([]);
  const [responseMessages, setResponseMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [sessionId, setSessionId] = useState('');

  useEffect(() => {
    let storedSessionId = sessionStorage.getItem('sessionId');
    if (!storedSessionId) {
      storedSessionId = generateSessionId();
      sessionStorage.setItem('sessionId', storedSessionId);
    }
    setSessionId(storedSessionId);
  }, []);

  // Combine messages from both arrays
  const combinedMessages = userMessages.map((message, index) => ({
    type: 'user',
    text: message.text,
    timestamp: message.timestamp,
    id: `user-${index}`,
  })).concat(responseMessages.map((message, index) => ({
    type: 'ai',
    text: message.text,
    timestamp: message.timestamp,
    id: `ai-${index}`,
  })));

  // Sort messages chronologically
  const sortedMessages = combinedMessages.sort(
    (a, b) => new Date(a.timestamp) - new Date(b.timestamp)
  );

  // Format text to support **bold** formatting
  const formatImprovementText = (text) => {
    return text.split('\n').map((line, index) => {
      const formattedLine = line.split('**').map((part, partIndex) => 
        partIndex % 2 === 1 ? <strong key={partIndex}>{part}</strong> : part
      );
      return <div key={index}>{formattedLine}</div>;
    });
  };

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return;
    const timestamp = new Date().toISOString();

    // Update state with user's message
    setUserMessages(prev => [...prev, { text: inputMessage, timestamp }]);

    // Clear the input field
    const currentInput = inputMessage;
    setInputMessage('');

    // Call the API endpoint
    const storedDocID = localStorage.getItem('doct_id') || "default_doct_id";
    try {
      const response = await fetch("http://127.0.0.1:8000/Rag/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ "user_id":sessionId,
            "query":currentInput,
            "doctID":storedDocID })
      });
      const data = await response.json();
      // Assuming the API returns a JSON object with a key "response"
      const aiText = data.response || "No response from server.";
      setResponseMessages(prev => [...prev, { text: aiText, timestamp: new Date().toISOString() }]);
    } catch (error) {
      console.error("Error calling chat API:", error);
      setResponseMessages(prev => [...prev, { text: "Error: Unable to fetch response", timestamp: new Date().toISOString() }]);
    }
  };

  // Send the message on Enter key press
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="chat-container">
      <header className="header">
        <h3>Chat with your Doc!</h3>
      </header>
      <div className="chat-box">
        {sortedMessages.map(message => (
          <div 
            key={message.id} 
            className={`message ${message.type === 'user' ? 'user-message' : 'ai-message'}`}
          >
            <div className="message-text">
              {formatImprovementText(message.text)}
              <span className="message-timestamp">
                {new Date(message.timestamp).toLocaleTimeString()}
              </span>
            </div>
          </div>
        ))}
      </div>
      <div className="input-area">
        <input 
          type="text"
          placeholder="Enter Your Query Here"
          value={inputMessage}
          onChange={e => setInputMessage(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}
