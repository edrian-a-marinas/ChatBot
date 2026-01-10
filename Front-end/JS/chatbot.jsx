function ChatInput({ chatMessages, setChatMessages }) {
  const [inputText, setInputText] = React.useState('');

  function saveInputText(event) {
    setInputText(event.target.value);
  }

  function enterText(event) {
    if (event.key === 'Enter'){
      sendMessage();
    }
  }

  async function sendMessage() {
    if (!inputText.trim()) return; // Ignore empty input


    const newChatMessages = [
      ...chatMessages,
      {
        message: inputText,
        sender: 'user',
        id: crypto.randomUUID()
      }
    ];

    setChatMessages(newChatMessages);
    const typingMessage = {
      message: <span className="typing"><span></span></span>,
      sender: 'robot',
      id: crypto.randomUUID(),
      typing: true // optional flag
    };    
    setChatMessages(prev => [...prev, typingMessage]);
    
    setInputText('');

    try {
      const res = await fetch('http://127.0.0.1:8000/chat', {  // Call Python main.py backend
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: inputText })
      });

      const data = await res.json(); // wait for JSON parsing

      await new Promise(resolve => setTimeout(resolve, 500));

      // Add robot reply
      setChatMessages([
        ...newChatMessages,
        {
          message: data.reply,
          sender: 'robot',
          id: crypto.randomUUID()
        }
      ]);

    } catch (err) {
      console.error(err);
      setChatMessages([
        ...newChatMessages,
        {
          message: 'Server error. Please try again later.',
          sender: 'robot',
          id: crypto.randomUUID()
        }
      ]);
    }


  }

  return (
    <div className="chat-input-wrapper">
      <span className="tooltip-icon">?
        <span className="tooltip-text">
          Ask about Edrian's skills, hobbies, or personal details!
        </span>
      </span>

      <div className="chat-input-container">
        <input
          className="chat-input"
          placeholder="Ask me anything about Edrian…"
          size="25"
          onChange={saveInputText}
          onKeyDown={enterText}
          value={inputText}
        />
        <button 
          onClick={sendMessage}
          className="send-button"
        >
          Send
        </button>
      </div>
    </div>
  );
}

function ChatMessage({ message, sender, typing }) {
  return (
    <div className = {
      sender === 'user'
      ? 'chat-message-user'
      : 'chat-message-robot'
    } >
      {sender === 'robot' && (
        <img className="icon" src="./CSS/Images/bot.png" />
      )}

      <div className = "chat-message-text"> 
        <span className={typing ? 'typing' : ''}>
          {message}
        </span>
      </div>

      {sender === 'user' && (
        <img className="icon" src="./CSS/Images/usr.png" />
      )}
    </div>
  );
}

function ChatMessages({ chatMessages }) {
  const chatMessagesRef = React.useRef(null);

  React.useEffect(() => {
    const containerElem = chatMessagesRef.current;
    if (containerElem) {
      containerElem.scrollTop = containerElem.scrollHeight;
    }
  }, [chatMessages]);

  return (
    <div className="chat-messages-container" ref={chatMessagesRef}>
      {chatMessages.length === 0 && (
        <p className="welcome-message">
          Hi! I'm Edrian's AI. Ask me anything about Edrian's skills, hobbies, or background.
        </p>
      )}

      {chatMessages.map(chatMessage => (
        <ChatMessage
          message={chatMessage.message}
          sender={chatMessage.sender}
          key={chatMessage.id}
        />
      ))}
    </div>
  );
}

function App() {
  const [chatMessages, setChatMessages] = React.useState([]);

  return (
    <div className="app-container">
      <ChatMessages
        chatMessages={chatMessages}
      />

      <ChatInput
        chatMessages={chatMessages}
        setChatMessages={setChatMessages}
      />
    </div>
  );
}

const container = document.querySelector('.js-container');
const containerRoot = ReactDOM.createRoot(container);
containerRoot.render(<App />);




















 


/*
MAKE THIS PROJECT AS SELF QUESTION SOMETHING


This part we use the chatMessage as the new value ng chatMessage {blah: blah} 

  const chatMessageComponents = chatMessages.map((chatMessage) => {
    return (
      <ChatMessage 
        message={chatMessage.message}
        sender={chatMessage.sender}
      />
    );
  });


Special props/attributes
onClick 
key
className
...chatMessage / spread notation/ copy 
react.useSate


  */