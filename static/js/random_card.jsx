////// React //////

const TradingCard = (props) => {
  const url = `/usercards/${props.card_id}`

  return (
    <div className="card">
      <a href={url}><img src={props.img_path} alt="profile" /></a>
    </div>
  );
}

const RarityCardButton = (props) => {
  return (
    <button
      onClick={props.handleClick} 
      key={props.rarity} 
      className="nav-link px-0"
    > 
      <span className="d-none d-sm-inline">
        {props.rarity}
      </span>
    </button>
  )
}

const TradingCardContainer = () => {
  const [allCards, setAllCards] = React.useState([]);
  const [filteredCards, setFilteredCards] = React.useState([]);
  const [cardType, setCardType] = React.useState('');
  const [rarities, setRarities] = React.useState([]);
 
  React.useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('/get-cards')
      const jsonResult = await response.json()
      console.log(jsonResult.data)
      const cards = jsonResult.data
      cards.map((card) => {if (!rarities.includes(card.rarity)) {rarities.push(card.rarity)}})
      setRarities(rarities)
      setAllCards(cards)
      setFilteredCards(cards)
    }
    fetchData()
  }, [])

  React.useEffect(() => {
    const filteredCards = allCards.filter((card) => card.rarity === cardType)
    setFilteredCards(filteredCards)
  }, [cardType])

  const rarityButtons = rarities.map((rarity) => <RarityCardButton handleClick={() => setCardType(rarity)} rarity={rarity} key={rarity} />)
  const filteredTradingCards = filteredCards.map((card) => <TradingCard {...card} />)

  console.log(filteredCards, 'line 59 FILTERED CARDS')
  return (
    <React.Fragment>
      <td>
        <div className="browser-menu">
          <span className="fs-5"><strong>Browse by Card Rarity</strong></span>
            <ul className="nav nav-pills flex-column mb-sm-auto mb-0 align-items-sm-start" id="menu">
              {rarities.map((rarity) => (
                <RarityCardButton 
                  handleClick={() => setCardType(rarity)} 
                  rarity={rarity} 
                  key={rarity} 
                />
              ))}
            </ul>
        </div>
      </td>

      <td>
        <div className="mx-auto" style={{width: "1200px"}}>
          <div className="col py-5">  
            <div className="grid-cards" id="grid-cards-jsx">
              {filteredTradingCards}
            </div>
          </div>    
        </div>
      </td>
    </React.Fragment>
  );
}
  
ReactDOM.render(<TradingCardContainer />, document.getElementById('pokedex'));
  