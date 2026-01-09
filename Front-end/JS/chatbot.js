function ChatInput({chatMessages, setChatMessages}) {
  const [inputText, setInputText] = React.useState('');

  function saveInputText(event){
    setInputText(event.target.value);
    
  }
  
  function sendMessage() {
    const newChatMessages = [
      ...chatMessages,
      {
        message: inputText,
        sender: 'user',
        id: crypto.randomUUID()
      }
    ]

    setChatMessages(newChatMessages);

    const response = Chatbot.getResponse(inputText);
    
    setChatMessages([
      ...newChatMessages,
      {
        message: response,
        sender: 'robot',
        id: crypto.randomUUID()
      }
    ]);

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
      <button 
        onClick={sendMessage}>
          Send Text
      </button>
    </>
  );
}

function ChatMessage({ message, sender }){
  return (
    <div>
      {sender === 'robot' && (
        <img className="icon" 
        src="../CSS/Images/robot.png" />
      )}

      {message}
  
      {sender === 'user' && (
        <img className="icon" 
        src="../CSS/Images/user.png" />
        )}
      
    </div>
  );
}


function ChatMessages({chatMessages}) {
  return (
    <> 
      {chatMessages.map((chatMessage) => {
        return (
          <ChatMessage 
          
            message={chatMessage.message}
            sender={chatMessage.sender}
            key={chatMessage.id}
          />
        );   
      })}
    </>
  );
}


function App() {
  const [chatMessages, setChatMessages] = React.useState([{
    message: 'hello chatbot',
    sender: 'user',
    id: 1
  }, {
    message: 'Hello! How can I help you?',
    sender: 'robot',
    id: 2 
  }, {
    message: 'When is your birthday?',
    sender: 'user',
    id: 3
  }, {
    message: 'January 27',
    sender: 'robot',
    id: 4
  }]);

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