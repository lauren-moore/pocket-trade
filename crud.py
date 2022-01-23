"""CRUD operations."""

from model import db, User, Card, UserCard, connect_to_db


# def create_user(name, email, password):
#     """Create and return a new user."""

#     user = User(name=name, email=email, password=password)

#     return user

# def create_card(name, types, rules, price, image_path):
#     """Create and return a new card."""

#     card = Card(name=name,types=types, rules=rules, price=price, image_path=image_path)

#     return card

# def create_order(listed, purchased, buyer):
#     """Create and return a new rating."""

#     order = Order(listed=listed, purchased=purchased, buyer=user)

#     return order

# def get_order_by_id(order_id):
#     '''get order by id'''

#     return Order.query.get(order_id)

# def get_cards():
#     """Return all cards."""

#     return Card.query.all()

# def get_card_by_id(card_id):
#     '''get card by id'''

#     return Card.query.get(card_id)

# def get_users():
#     '''Return all users'''

#     return User.query.all()

# def get_user_by_id(user_id):
#     '''get user by id'''

#     return User.query.get(user_id)

# def get_user_by_email(email):
#     """Return a user by email."""

#     return User.query.filter(User.email == email).first()

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)