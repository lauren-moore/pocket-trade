'use-strict';

// const randomBtn = document.querySelector('#btnrandom');
// const randomPokemon = document.querySelector('.homepage-random-cards')

// randomBtn.addEventListener('click', () => {
//     if (randomPokemon.style.display === 'none') {
//         randomPokemon.style.display = 'block';
//     } else {
//         randomPokemon.style.display = 'none'
//          }
// });

// function replaceCard(results) {
//     document.querySelector('#fortune-text').innerHTML = results;
//   }
  
//   function showCard(evt) {
//     fetch('/')
//       .then(response => response.text())
//       .then(replaceFortune);
//   }
  
//   document.querySelector('#get-fortune-button').addEventListener('click', showFortune);


  const testDiv = document.querySelector('#test')

  document.querySelector('#btnrandom').addEventListener('click', () => {
    fetch('/random')
      .then(response => response.text())
      .then(result => {
        console.log("hello");
        console.log(result);
        // testDiv.innerText = result;
        // const randomCard = result.random_card;
        // document
        //   .querySelector('#homepage-random-cards')
        //   .innertHTML = `<div><src="${randomCard}"></div>`;
      });
  });







// const randomBtn = document.querySelector('#btnrandom');
// const randomPokemon = document.querySelector('.homepage-random-cards')

// randomBtn.addEventListener('click', () => {
//     fetch('/')
//         .then(response => response.text())
//         .then(randomCardResponse => {
//             if (randomPokemon.style.display === 'none') {
//                 randomPokemon.style.display = 'block';
//             } else {
//                 randomPokemon.style.display = 'none'
//                 }
//         });


// fetch('https://pokeapi.co/api/v2/berry/')
//     .then(response => response.json())
//     .then(berriesResponse => {
//         let berryList = [];
//         for (const berry in berriesResponse.results) {
//             berryList.push(berriesResponse.results[berry]['name']);
//                 document.querySelector('#berries').innerHTML = berryList.join(', ');
//     }
// });

// const randomBtn = document.querySelector('#btnrandom');
// const randomPokemon = document.querySelector('.homepage-random-cards')

// randomBtn.addEventListener('click', () => {
//   const url = "/data/cards.json";

//   fetch(url)
//     .then(response => response.json())
//     .then(randomResponse => {

//         // # card_id = randint(1, 200)
//         // # random_card = crud.get_card_by_id(card_id)

//         let pokemonCards = [];

//         for (const card in randomResponse.results) {
//             pokemonCards.push(randomResponse.results['name']);
//                 document.querySelector('#berries').innerHTML = berryList.join(', ');
//     }

//         if (randomPokemon.style.display === 'none') {
//             randomPokemon.style.display = 'block';
//         } else {
//             randomPokemon.style.display = 'none'
//              }
//     });
// });





// const button = document.querySelector('#update-status');

// button.addEventListener('click', () => {
//   const queryString = new URLSearchParams({order: 123}).toString();
//   // you could also hard code url to '/status?order=123'
//   const url = `/status?${queryString}`;

//   fetch("/random")
//     .then(response => response.text())
//     .then(status => {
//       document.querySelector('#order-status').innerHTML = status;
//     });
// });