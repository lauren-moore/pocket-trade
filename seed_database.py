"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import re

import crud
import model
import server

os.system("dropdb poke")
os.system("createdb poke")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/poke_cards.json") as f:
    card_data = json.loads(f.read())

cards_in_db = []
all_rarities = []
rarities_in_db = []
for card in card_data["data"]:

    name = card["name"]
    price = randint(1,999)
    pokedex_number = card["nationalPokedexNumbers"][0]
    image_path = card["images"]["large"]

    if "flavorText" in card:
        flavor_text = card["flavorText"]
    
    if "rarity" in card:
        rarity = card["rarity"]
        if rarity not in all_rarities:
            all_rarities.append(rarity)
            db_rarity = crud.create_rarity(rarity)
            rarities_in_db.append(db_rarity)
    else:
        rarity = None
    
    db_card = crud.create_card(name, price, db_rarity, flavor_text, pokedex_number, image_path)

    
    cards_in_db.append(db_card)
  

model.db.session.add_all(rarities_in_db)
model.db.session.add_all(cards_in_db)

model.db.session.commit()


#     for type_name in card_data:
#         if type_name not in all_types:
#             all_types.append(type_name)
      
# types_in_db =[]

# for type_name in all_types:
#     db_typename = crud.create_type(type_name)
#     types_in_db.append(db_typename)



# 10 random users and cards

for n in range(10):
    name = f'Lauren {n}'
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(name, email, password)
    model.db.session.add(user)

    for n2 in range(100):
        random_card = choice(cards_in_db)

        user_card = crud.create_user_card(user, random_card)
        model.db.session.add(user_card)


model.db.session.commit()
