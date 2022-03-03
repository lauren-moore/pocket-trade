'use-strict';

console.log('JS IS WORKING')


  const homepageBtn = document.getElementById('btnrandom');
  const randomCard = document.getElementById("random-pokemon2")
  console.log(randomCard)
  const testImg = document.getElementById('test-img')
  const testCardBody = document.getElementById('test-card-body')
  const testTitle = document.getElementById('test-title')
  const testText = document.getElementById('test-text')

  homepageBtn.addEventListener('click', (evt) => {
    evt.preventDefault;
    fetch('/random')
      .then(response => response.json())
      .then(result => {
        randomCard.style.display = "block";
        testImg.innerHTML = `<img id="random" src="${result.data.image_path}" class="img-fluid rounded-start" alt="...">`
        testTitle.innerHTML = `<strong>It's ${result.data.name}!</strong>`
        testText.innerHTML = `${result.data.flavor_text}`
        testCardBody.innerHTML = `<a href="/usercards/${result.data.card_id}" class="card-link">Catch</a> `
      });
  });




