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
    name = db.Column(db.String, nullable=False)
    rarity_id = db.Column(db.Integer, db.ForeignKey("rarities.rarity_id"), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    flavor_text = db.Column(db.Text, nullable=True)
    pokedex_number = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    
    rarity = db.relationship("Rarity", back_populates="cards")
    types = db.relationship("Types", secondary="card_types", backref="cards")

    def __repr__(self):
        return f'<Card card_id={self.card_id} name={self.name} price={self.price}>'


class Rarity(db.Model):
    """Types of rarity."""

    __tablename__ = "rarities"

    rarity_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True,
                    nullable=False)
    name = db.Column(db.String, unique=True)

    cards = db.relationship("Card", back_populates="rarity")

    def __repr__(self):
        return f'<Rarity id={self.rarity_id} is name={self.name}>'



class Types(db.Model):
    """Types of Pokemon."""

    tablename = "types"

    types_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        nullable=False)
    type_name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Types_id={self.types_id} type={self.type_name}>'


class CardTypes(db.Model):
    """Types belonging to specific Pokemon"""

    tablename = "card_types"

    cardtype_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,
                        nullable=False)
    types_id = db.Column(db.Integer, db.ForeignKey("types.types_id"))
    card_id = db.Column(db.Integer, db.ForeignKey("cards.card_id"))

    card = db.relationship("Card", backref="cardtypes")
    types = db.relationship("Types", backref="cardtypes")


class UserCard(db.Model):
    """A Pokemon card owned buy a user"""

    __tablename__ = "user_cards"

    user_card_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    card_id = db.Column(db.Integer, db.ForeignKey("cards.card_id"))
    sold = db.Column(db.Boolean, nullable=False)

    user = db.relationship("User", backref="user_cards")
    card = db.relationship("Card", backref="user_cards")
    

    def __repr__(self):
        return f'<Card {self.card_id} belongs to user {self.user_id}>'


class Order(db.Model):
    """A receipt of card purchase."""
 
    __tablename__ = "orders"

    order_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_card_id = db.Column(db.Integer, db.ForeignKey("user_cards.user_card_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    purchased = db.Column(db.DateTime, nullable=False)
    
    user_card = db.relationship("UserCard", backref="order")
    user = db.relationship("User", backref="orders")

    def __repr__(self):
        return f'<Order order_id={self.order_id} user_card={self.user_card_id} user={self.user_id}>'


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