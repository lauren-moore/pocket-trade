"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb poke")
os.system("createdb poke")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/cards.json") as f:
    card_data = json.loads(f.read())


cards_in_db = []
all_types = []
for card in card_data:
    pokemon_name, card_name, rules, price, image_path = (
        card["pokemon_name"],
        card["card_name"],
        card["rules"],
        card["price"],
        card["image_path"]
    )

    db_card = crud.create_card(pokemon_name, card_name, rules, price, image_path)
    cards_in_db.append(db_card)
  
#     for type_name in card_data:
#         if type_name not in all_types:
#             all_types.append(type_name)
      
# types_in_db =[]

# for type_name in all_types:
#     db_typename = crud.create_type(type_name)
#     types_in_db.append(db_typename)

model.db.session.add_all(cards_in_db)
# model.db.session.add_all(types_in_db)
model.db.session.commit()

# 10 random users and cards

for n in range(10):
    name = f'Lauren {n}'
    email = f'user{n}@test.com' 
    password = 'test'

    user = crud.create_user(name, email, password)
    model.db.session.add(user)

    for n2 in range(2):
        random_card = choice(cards_in_db)

        user_card = crud.create_user_card(user, random_card)
        model.db.session.add(user_card)


model.db.session.commit()
