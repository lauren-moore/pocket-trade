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
  // const tradingCards = allCards.map((card) => <TradingCard {...card} />)

  console.log(filteredCards, 'line 59 FILTERED CARDS')
  return (
    <React.Fragment>
      <td>
      <div className="container-fluid">
        <div className="row flex-nowrap">
          <div className="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-white">
            <div className="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
              <a href="/" className="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-black text-decoration-none">
                <span className="fs-5 d-none d-sm-inline">Browse by:</span>
              </a>
              <ul className="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                <li className="nav-item">
                  <a href="#" className="nav-link align-middle px-0">
                    <span className="ms-1 d-none d-sm-inline">Type</span>
                  </a>
                </li>
                  {rarities.map((rarity) => (
                    <RarityCardButton 
                      handleClick={() => setCardType(rarity)} 
                      rarity={rarity} 
                      key={rarity} 
                    />
                  ))}
              </ul>
            </div>
          </div>
        </div>
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
  