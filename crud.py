"""CRUD operations."""

from model import db, User, Card, UserCard, Order, ShoppingCart, connect_to_db


def create_user(name, email, password):
    """Create and return a new user."""

    user = User(name=name, email=email, password=password)

    return user

def create_card(name, types, rules, price, image_path):
    """Create and return a new card."""

    card = Card(name=name,types=types, rules=rules, price=price, image_path=image_path)

    return card

def create_user_card(user, card):
    """Add a user to an existing card."""

    user_card = UserCard(user=user, card=card, sold=False)

    return user_card

def create_order(listed, purchased, buyer):
    """Create and return a new rating."""

    order = Order(listed=listed, purchased=purchased, buyer=user)

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

def get_cards_by_types(types):
    '''get cards by types.'''

    return Card.query.get(types).all()

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

    return UserCard.query.get(user_id).all()

def get_orders():
    '''Return all orders.'''

    return Orders.query.all()

def get_order_by_id(order_id):
    '''get order by id'''

    return Order.query.get(order_id)

def get_shopping_carts():
    """Return all shopping carts."""

    return ShoppingCart.query.all()

def get_shopping_cart_by_user_id(user_id):
    '''get shopping cart by user id.'''

    return ShoppingCart.query.get(user_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)