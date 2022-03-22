# Pocket Trade 

Gotta catch 'em all? Pocket Trade is a full-stack web application and your one-stop shop for collecting digital first-generation Pokémon cards. With its name being an homage to the original manga, Pokémon Pocket Monsters, Pocket Trade allows users (or Pokémon Trainers as we like to call them) to search for cards by name to view the original artwork. If you see a card you like, you can add it to your shopping cart to purchase. After shopping, you can purchase the cards to add to your collection. Card ownership is constantly in flux as Pokémon Trainers purchase cards from other Trainers. Unsure of which Pokémon to catch first? There is a random card generator on the homepage to give you some ideas. Your favorite Pokémon is looking for a new trainer. Start your collection today

![image](https://user-images.githubusercontent.com/91762225/158905571-03ab001e-34f9-4baf-8a9b-38772d82f810.png)


## Tech Stack

**Backend:** Python 3, PostgreSQL, Flask, SQLAlchemy, Jinja

**Frontend:** JavaScript, jQuery, HTML 5, CSS 3, Bootstrap, React

**API:** Pokemon TCG


## Installation

**Prerequisites**

To run Pocket Trade, you will need an API key for Pokemon TCG. 
Python 3 and PostgreSQL also need to be installed on your machine.


**How to run Pocket Trade on your machine**

Clone this repository
```shell
git clone https://github.com/lauren-moore/pocket-trade.git
```
Optional: Create and activate a virtual environment using virtualenv
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```
Install dependencies from requirements.txt
```shell
pip3 install -r requirements.txt
```
Create an environmental variable to hold your API key
```shell
export POKEMONTCG_KEY='{YOUR POKEMON TCG API KEY HERE}'

```
Create your database & seed sample data
```shell
createdb poke
python3 seed_database.py
```
Run the app on localhost
```shell
python3 server.py
```

## Demo
Click [Here!](https://www.youtube.com/watch?v=pswyQinZ03U) to watch the demo

## About Me

As a Hotel Administration graduate, Laurén's background is in all things hospitality. From being a floor manager and bartender at a fine-dining restaurant to being a flight attendant, she has a passion for making others smile. She also has experience as an E-Com Proudcer and Project Manager where she works on board and card games. This appreciation for games, puzzles, problem solving, and logic lead her to tech. After taking courses in Computer Science and Python, Laurén knew it was time to transition into a life of software engineering and join Hackbright. After graduating, she will continue to expand her technical skills and knowledge in learning new coding languages and data science. She aspires to continue making a positive impact for others using her background in hospitality, passion for problem solving, and knowledge in Software Engineering. 

Let's connect on [LinkedIn!](https://www.linkedin.com/in/laurencaroleen/)

![image](/static/img/Business_card.jpg)