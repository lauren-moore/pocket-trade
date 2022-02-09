from flask import Flask, render_template, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud
from datetime import date
import requests
import os
import json

app = Flask(__name__)
app.secret_key = "dev"
API_KEY = 'c609b2a0-ca0f-4910-b3ef-a1f70a872874'

def find_cards():
    """Search for cards on Pokemon TCG"""

    url = 'https://api.pokemontcg.io/v2/cards/'


    # payload = {'apikey': API_KEY,
    #             'nationalPokedexNumbers': 1}


    response = requests.get(url, params={"q": "nationalPokedexNumbers:[1 TO 151]"}, headers={"X-Api-Key": API_KEY})

    data = response.json()

    cards = data['data']
    for card in cards:
        card.pop('set')
        card.pop('id')
        card.pop('cardmarket')
        card.pop('legalities')
        card.pop('supertype')
        card.pop('artist')
        card.pop('number')
        if 'attacks' in card:
            card.pop('attacks')
        if 'weaknesses' in card:
            card.pop('weaknesses')
        if 'retreatCost' in card:
            card.pop('retreatCost')
        if 'convertedRetreatCost' in card:
            card.pop('convertedRetreatCost')
        if 'rules' in card:
            card.pop('rules')
        if 'tcgplayer' in card:
            card.pop('tcgplayer')




    with open('poke_cards.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    
    print(data)

find_cards()