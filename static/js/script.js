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


//// Browse by rarity on all_cards ////
const rarityBtn = document.getElementById('rarity-button');
const cardRarity = document.getElementById("rarity-links")

rarityBtn.addEventListener('click', (evt) => {
  evt.preventDefault;
  fetch('/rarities')
    .then(response => response.json())
    .then(result => {
      console.log(result.data)
      for (const card in result.data) {
        cardRarity.innerHTML = `<a href="/rarity/${result.data.rarity_id}" class="card-link">${result.data.name}</a> `
      }
    });
});
