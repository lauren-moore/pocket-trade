"""Models for Pocket Trade app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
 
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.name} email={self.email}>'


class Card(db.Model):
    """A Pokemon card."""
 
    __tablename__ = "cards"

    card_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    pokemon_name = db.Column(db.String, nullable=False)
    card_name = db.Column(db.String, nullable=False, unique=True)
    types = db.Column(db.String, nullable=False)
    rules = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'<Card card_id={self.card_id} pokemon_name={self.pokemon_name} card_name={self.card_name} price={self.price}>'


class UserCard(db.Model):
    """A Pokemon card owned buy a user"""

    __tablename__ = "user_cards"

    user_card_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    card_id = db.Column(db.Integer, db.ForeignKey("cards.card_id"))
    sold = db.Column(db.Boolean, nullable=False)

    card = db.relationship("Card", backref="user_cards")
    user = db.relationship("User", backref="user_cards")

    def __repr__(self):
        return f'<Card {self.card_id} belongs to user {self.user_id}>'

class Order(db.Model):
    """A receipt of card purchase."""
 
    __tablename__ = "orders"

    order_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    # card_id = db.Column(db.Integer, db.ForeignKey("cards.card_id"))
    user_card_id = db.Column(db.Integer, db.ForeignKey("user_cards.user_card_id"))
    # seller_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    listed = db.Column(db.DateTime, nullable=False)
    purchased = db.Column(db.DateTime, nullable=False)
    
    user_card = db.relationship("UserCard", backref="orders")
    buyer = db.relationship("User", backref="orders")

    def __repr__(self):
        return f'<Order order_id={self.order_id} card={self.card_id} seller={self.seller_id} buyer={self.buyer_id}>'


class ShoppingCart(db.Model):
    """A shopping cart for users to add potential purchases."""

    __tablename__ = "shopping_carts"

    shopping_cart_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user_card_id = db.Column(db.Integer, db.ForeignKey("user_cards.user_card_id"))

    user = db.relationship("User", backref="shopping_carts")
    user_card = db.relationship("UserCard", backref="shopping_carts")
    
    def __repr__(self):
        return f'<Shopping cart shopping_cart_id={self.shopping_cart_id} user_id={self.user_id} user_card_id={self.user_card_id}>'


def connect_to_db(flask_app, db_uri="postgresql:///poke", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
