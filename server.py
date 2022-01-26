"""Server for Pokemon Card app."""
from flask import Flask, render_template, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/login')
def log_in():
    """Log in page."""

    email = request.form.get("email")
    password = request.form.get("password")

    return render_template('login.html')


@app.route("/create-account")
def view_register_user():
    """Create a new user."""

    return render_template('create_account.html')


@app.route('/cards')
def all_cards():
    """View cards page."""

    cards = crud.get_cards()

    return render_template('all_cards.html', cards=cards)


@app.route('/users')
def all_users():
    """View users page."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/cards/<card_id>')
def show_card(card_id):
    """Show card details."""

    card = crud.get_card_by_id(card_id)

    return render_template('card_details.html', card=card)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user details."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/cart/<shopping_cart_id>')
def sho_shopping_cart(user_id):
    """Get shopping cart by user id."""

    shopping_cart = crud.get_shopping_cart_by_user_id(user_id)

    return render_template('shopping_cart.html', shopping_cart=shopping_cart)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    name= request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("An account has already been created with that email address. Try again.")
    else:
        user = crud.create_user(name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

        return redirect('login.html')
    
    
@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
