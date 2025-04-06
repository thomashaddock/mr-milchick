import React from "react";
import ChatInterface from "./components/ChatInterface";

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Mr. Milchick</h1>
        <p>Manhattan Real Estate Assistant</p>
      </header>
      <main>
        <ChatInterface />
      </main>
    </div>
  );
}

export default App;
