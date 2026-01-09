console.log('Hello its working!');

const button = <button>Button Test</button>;
const paragraph = <p>Paragraph Test</p>;

const div = (
  <div> 
    {button}
    {paragraph}
  </div>
);


const container = document.querySelector('.js-container');
const root = ReactDOM.createRoot(container);

root.render(div);

