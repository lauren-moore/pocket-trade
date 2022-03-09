'use-strict';

console.log('JS IS WORKING')

//// random Pokemon card feature on homepage ////
const homepageBtn = document.getElementById('btnrandom');
const randomCard = document.getElementById("random-pokemon2")
console.log(randomCard)
const testImg = document.getElementById('test-img')
const randomLink = document.getElementById('random-link')
const randomTitle = document.getElementById('random-title')
const randomText = document.getElementById('random-text')

homepageBtn.addEventListener('click', (evt) => {
  evt.preventDefault;
  fetch('/random')
    .then(response => response.json())
    .then(result => {
      randomCard.style.display = "block";
      testImg.innerHTML = `<img id="random" src="${result.data.image_path}" class="img-fluid rounded-start" alt="...">`
      randomTitle.innerHTML = `<strong>It's ${result.data.name}!</strong>`
      randomText.innerHTML = `${result.data.flavor_text}`
      randomLink.innerHTML = `<a href="/usercards/${result.data.card_id}" class="card-link">Catch</a> `
    });
});



// ////// React //////
// function makeFetch() {
//   fetch('/random')
//   .then(response => response.json())
//   console.log(response)
//   .then(
//     (result) => {
//       return (
//         result,
//         console.log(result)
//       )
//     })};


// //parent component
// function TradingCardContainer(props) {
//   const [cardInfo, setCardInfo] = React.setState(makeFetch())
//   console.log(cardInfo)
//   console.log(setCardInfo)

//   //function to refreshcard
//   function refreshCard(){
//     setCardInfo(makeFetch())
//   };

//   //return should contain the button, card component
//   tradingCard.push( 
//     <PokemonCard {...cardInfo} />,
//     <button id="btnrandom" onClick={refreshCard}>Who's that Pokemon?</button>,
//   );

//   return <React.Fragment>{tradingCard}</React.Fragment>;
// }


// //child component
// const PokemonCard = (props) => {
//   const { name, img, flavor_text, card_id} = props;

//   return (
//       <div className="homepage-random-cards">
//           <img className="test-img" src={img}/>
//           <h5>{name}</h5>
//           <p id="random-text" flavor_text={flavor_text}/>
//           <a href={`/usercards/${card_id}`} class="card-link">Catch</a> 
//       </div>
//   )
// };

// ReactDOM.render(<TradingCardContainer />, document.querySelector('#homepage-random-cards'));





// outside function to make fetch (makeFetch)
// return some kind of obj
// const function {
//   fetch call
//   return cardinfo in obj
// }




//// Browse by rarity on all_cards ////
// const rarityBtn = document.getElementById('rarity-button');
// const cardRarity = document.getElementById("rarity-links")

// rarityBtn.addEventListener('click', (evt) => {
//   evt.preventDefault;
//   fetch('/rarities')
//     .then(response => response.json())
//     .then(result => {
//       console.log(result.data)
//       for (const card in result.data) {
//         cardRarity.innerHTML = `<a href="/rarity/${result.data.rarity_id}" class="card-link">${result.data.name}</a> `
//       }
//     });
// });
