function ChatInput({ chatMessages, setChatMessages }) {
  const [inputText, setInputText] = React.useState('');

  function saveInputText(event) {
    setInputText(event.target.value);
  }

  function sendMessage() {
    if (!inputText.trim()) return; // Ignore empty input

    // Add user message first
    const newChatMessages = [
      ...chatMessages,
      {
        message: inputText,
        sender: 'user',
        id: crypto.randomUUID()
      }
    ];
    setChatMessages(newChatMessages);

    // Call Python backend
    fetch('http://127.0.0.1:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: inputText })
    })
      .then(res => res.json())
      .then(data => {
        setChatMessages([
          ...newChatMessages,
          {
            message: data.reply,
            sender: 'robot',
            id: crypto.randomUUID()
          }
        ]);
      })
      .catch(err => {
        console.error(err);
        setChatMessages([
          ...newChatMessages,
          {
            message: 'Oops! Something went wrong connecting to the chatbot.',
            sender: 'robot',
            id: crypto.randomUUID()
          }
        ]);
      });

    setInputText('');
  }

  return (
    <>
      <input
        placeholder="Get to know Ian"
        size="25"
        onChange={saveInputText}
        value={inputText}
      />
      <button onClick={sendMessage}>
        Send Text
      </button>
    </>
  );
}

function ChatMessage({ message, sender }) {
  return (
    <div>
      {sender === 'robot' && (
        <img className="icon" src="CSS/Images/robot.png" />
      )}

      {message}

      {sender === 'user' && (
        <img className="icon" src="CSS/Images/user.png" />
      )}
    </div>
  );
}

function ChatMessages({ chatMessages }) {
  return (
    <>
      {chatMessages.map(chatMessage => (
        <ChatMessage
          message={chatMessage.message}
          sender={chatMessage.sender}
          key={chatMessage.id}
        />
      ))}
    </>
  );
}

function App() {
  const [chatMessages, setChatMessages] = React.useState([]);

  return (
    <>
      <ChatInput
        chatMessages={chatMessages}
        setChatMessages={setChatMessages}
      />
      <ChatMessages
        chatMessages={chatMessages}
      />
    </>
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