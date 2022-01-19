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
    """A Pokemon trading card."""
 
    __tablename__ = "cards"

    card_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)
    types = db.Column(db.String, nullable=False)
    rules = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String, nullable=False)\
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f'<Card card_id={self.card_id} name={self.name} types={self.types} price={self.price}>'

class Order(db.Model):
    """An order to purchase a card."""
 
    __tablename__ = "orders"

    order_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    listed_at = db.Column(db.DateTime, nullable=False)
    purchased_at = db.Column(db.DateTime, nullable=False)
    sold_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    purchaed_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f'<Order order_id={self.order_id} 
                listed at={self.listed_at} 
                purchased at="{self.purchasd_at} 
                sold by={self.sold_by} 
                purchased by={self.purcased_by}>'



def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
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
