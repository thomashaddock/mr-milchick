import React from "react";

const Message = ({ message }) => {
  return (
    <div
      className={`message ${
        message.role === "user" ? "user-message" : "assistant-message"
      }`}
    >
      <div className="message-content">{message.content}</div>
    </div>
  );
};

export default Message;
