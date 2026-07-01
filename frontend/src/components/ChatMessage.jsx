import './ChatMessage.css'


const ChatMessage = ({ message }) => {
  const isUser = message.role === "user";

  return (
    <div 
      className="message-container" 
      style={{
        justifyContent: isUser ? "flex-end" : "flex-start",
      }}
    >
      <div 
        className="message-bubble"
        style={{
        background: isUser ? "#2563eb" : "#1e1e1e",
      }}>
        {message.content}
      </div>
    </div>
  );
};

export default ChatMessage;