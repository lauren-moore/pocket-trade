"""CRUD operations."""

from model import db, User, Card, UserCard, Order, Types, ShoppingCart, connect_to_db


def create_user(name, email, password):
    """Create and return a new user."""

    user = User(name=name, email=email, password=password)

    return user

def create_card(pokemon_name, card_name, rules, price, image_path):
    """Create and return a new card."""

    card = Card(pokemon_name=pokemon_name,card_name=card_name, rules=rules, price=price, image_path=image_path)

    return card

def create_card_type(card, type_name):
    """Create the relationship between cards and types."""

    card_type = CardType(card=card, type_name=type_name)

    return card_type

def create_user_card(user, card):
    """Add a user to an existing card."""

    user_card = UserCard(user=user, card=card, sold=False)

    return user_card

def create_type(type_name):
    """Create and return a Pokemon type."""

    type_name = Types(type_name=type_name)

    return type_name

def create_order(user_card, user, listed, purchased):
    """Create and return a new rating."""

    order = Order(user_card=user_card, user=user, listed=listed, purchased=purchased)

    return order

def create_shopping_cart(user, user_card):
    """Create and return a user's shopping cart."""

    shopping_cart = ShoppingCart(user=user, user_card=user_card)

    return shopping_cart

def get_cards():
    """Return all cards."""

    return Card.query.all()

def get_card_by_id(card_id):
    '''get card by id'''

    return Card.query.get(card_id)

def get_cards_by_pokemon_name(pokemon_name):
    '''get cards by Pokemon name.'''

    return Card.query.get(pokemon_name).all()

def get_card_by_card_name(card_name):
    '''get card by card name.'''

    return Card.query.get(card_name)


def get_cards_by_price(price):
    '''get cards by price.'''

    return Card.query.get(price).all()

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    '''get user by id'''

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_cards():
    """Return all user cards."""

    return UserCard.query.all()

def get_user_cards_by_user(user_id):
    '''get user cards by user id.'''

    return UserCard.query.get(user_id)

def get_user_cards_by_card(card_id):
    '''get user cards by card id.'''

    return UserCard.query.get(card_id)

def get_user_card_by_id(user_card_id):
    '''get user card by id.'''

    return UserCard.query.get(user_card_id)

def get_orders():
    '''Return all orders.'''

    return Order.query.all()

def get_order_by_id(order_id):
    '''get order by id'''

    return Order.query.get(order_id)

def get_shopping_cart_by_user_id(user_id):
    '''get shopping cart by user id.'''

    return ShoppingCart.query.get(user_id)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)