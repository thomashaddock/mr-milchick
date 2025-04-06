import React, { useState } from "react";
import Message from "./Message";
import PropertyCard from "./PropertyCard";
import axios from "axios";

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! I'm Mr. Milchick, your Manhattan real estate assistant. How can I help you today?",
    },
  ]);
  const [input, setInput] = useState("");
  const [properties, setProperties] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading) return;

    // Add user message
    const userMessage = input;
    const newMessages = [...messages, { role: "user", content: userMessage }];
    setMessages(newMessages);
    setInput("");
    setIsLoading(true);

    try {
      // Call the backend API
      const response = await axios.post(
        "http://localhost:8000/api/conversation/chat",
        {
          message: userMessage,
        }
      );

      // Handle the response
      const assistantResponse = {
        role: "assistant",
        content: response.data.response,
      };

      setMessages([...newMessages, assistantResponse]);

      // Set properties if any were returned
      if (response.data.properties && response.data.properties.length > 0) {
        setProperties(response.data.properties);
      }
    } catch (error) {
      console.error("Error calling API:", error);
      setMessages([
        ...newMessages,
        {
          role: "assistant",
          content:
            "I'm sorry, but I encountered an error processing your request. Please try again later.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <Message key={index} message={message} />
        ))}
        {isLoading && (
          <div className="message assistant-message">
            <div className="message-content">Thinking...</div>
          </div>
        )}
      </div>

      {properties.length > 0 && (
        <div className="property-results">
          <h3>Properties</h3>
          <div className="property-grid">
            {properties.map((property) => (
              <PropertyCard key={property.id} property={property} />
            ))}
          </div>
        </div>
      )}

      <div className="message-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
          placeholder="Ask about Manhattan real estate..."
          disabled={isLoading}
        />
        <button onClick={handleSendMessage} disabled={isLoading}>
          {isLoading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;
