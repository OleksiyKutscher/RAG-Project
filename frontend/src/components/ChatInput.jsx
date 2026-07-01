import { useState } from "react";
import './ChatInput.css';

const ChatInput = ({ onSend, disabled }) => {
  const [value, setValue] = useState("");

  const handleSend = () => {
    if (!value.trim() || disabled) return;
    onSend(value.trim());
    setValue("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-input-container">
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask something about Anthropic docs..."
        disabled={disabled}
        rows={2}
      />
      <button
        onClick={handleSend}
        disabled={disabled}
        style={{
          background: disabled ? "#333" : "#2563eb",
          cursor: disabled ? "not-allowed" : "pointer",
        }}
      >
        Send
      </button>
    </div>
  );
};

export default ChatInput;