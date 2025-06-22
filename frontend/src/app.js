function Flashcards() {
  const [cards, setCards] = React.useState([]);
  React.useEffect(() => {
    fetch('http://localhost:5000/flashcards')
      .then(res => res.json())
      .then(setCards);
  }, []);
  return (
    <div>
      <h1>Flashcards</h1>
      <ul>
        {cards.map(card => (
          <li key={card.term}>
            <strong>{card.term}</strong>: {card.definition}
          </li>
        ))}
      </ul>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<Flashcards />);
