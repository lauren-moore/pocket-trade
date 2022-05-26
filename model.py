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


    @classmethod
    def create_user(self, name, email, password):
        """Create and return a new user."""
        user = User(name=name,
                    email=email, 
                    password=password)

        return user

    @classmethod
    def get_users(self):
        '''get all users.'''

        return User.query.all()

    @classmethod
    def get_user_by_id(self, user_id):
        '''get user by id.'''

        return User.query.get(user_id)

    @classmethod
    def get_user_by_email(self, email):
        '''get user by email.'''
    
        return User.query.filter(User.email == email).first()




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

    @classmethod
    def create_card(self, name, price, rarity, flavor_text, pokedex_number, image_path):
        '''create new card.'''

        card = Card(name=name, 
                    price=price, 
                    rarity=rarity,
                    flavor_text=flavor_text, 
                    pokedex_number=pokedex_number, 
                    image_path=image_path)

        return card

    @classmethod
    def get_cards_by_rarity(self, rarity_id):
        '''get cards by rarity.'''
    
        return Card.query.get(rarity_id).all()

    @classmethod
    def get_cards(self):
        '''get all cards.'''

        return Card.query.order_by(Card.pokedex_number).all()

    @classmethod
    def get_card_by_id(self, card_id):
        '''get card by card_id.'''

        return Card.query.get(card_id)

    @classmethod
    def get_cards_by_name(self, name):
        '''get card by name.'''

        return Card.query.get(name).all()

    @classmethod
    def get_cards_by_price(self, price):
        '''get cards by price.'''

        return Card.query.get(price).all()

    @classmethod
    def get_card_by_name(self, searched):
        '''get card by searched name.'''

        searched_cards = Card.query.filter(Card.name.ilike('%' + searched + '%')).all()
        return (searched_cards)


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

    @classmethod
    def create_rarity(self, name):
        '''create new rarity.'''

        rarity = Rarity(name=name)

        return rarity

    @classmethod
    def get_rarity(self):
        '''get all rarities.'''

        return Rarity.query.all()



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

    @classmethod
    def create_user_card(self, user, card):
        '''create new user card.'''

        user_card = UserCard(user=user, card=card, sold=False)

        return user_card

    @classmethod
    def get_user_cards(self):
        '''get all user cards.'''

        return UserCard.query.join(Card).order_by(Card.pokedex_number).all()


    @classmethod
    def get_user_cards_by_user(self, user_id):
        '''get user cards by user id.'''

        return UserCard.query.get(user_id)

    @classmethod
    def get_user_cards_by_card(self, card_id):
        '''get user cards by card id.'''

        return UserCard.query.get(card_id)

    @classmethod
    def get_user_card_by_id(self, user_card_id):
        '''get user card by id.'''

        return UserCard.query.get(user_card_id)


    @classmethod
    def update_user_card(self, user_card_id):

        user_card = UserCard.query.get(user_card_id)
        user_card.sold = True

        return user_card

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


    @classmethod
    def create_order(self, user_card, user, purchased):
        """Create and return a new rating."""

        order = Order(user_card=user_card, user=user, purchased=purchased)

        return order

    @classmethod
    def get_orders(self):
        '''Return all orders.'''

        return Order.query.all()


def connect_to_db(flask_app, db_uri="postgresql:///poke", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app


    connect_to_db(app)