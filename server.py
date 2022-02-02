"""Server for Pokemon Card app."""
from flask import Flask, render_template, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud
from datetime import date

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/login')
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


# @app.route('/login')
# def log_in():
#     """Log in page."""

#     return render_template('login.html')


@app.route("/create-account")
def view_register_user():
    """Create a new user."""

    return render_template('create_account.html')


@app.route('/cards')
def all_cards():
    """View cards page."""

    cards = crud.get_cards()

    return render_template('all_cards.html', cards=cards)


@app.route('/usercards/<card_id>')
def all_usercards(card_id):
    """View all available usercards."""

    usercards = crud.get_user_cards()
    card = crud.get_card_by_id(card_id)

    return render_template('all_usercards.html', 
                            usercards=usercards,
                            card=card)


@app.route('/cards/<user_card_id>')
def show_card(user_card_id):
    """Show card details."""

    usercard = crud.get_user_card_by_id(user_card_id)

    return render_template('card_details.html', usercard=usercard)


@app.route('/users')
def all_users():
    """View users page."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users/<user_id>')
@app.route('/collection/<user_id>')
def show_user(user_id):
    """Show user details."""

    user = crud.get_user_by_id(user_id)
    usercards = crud.get_user_cards()
    card = crud.get_cards()
    
    count_of_cards =0

    for usercard in usercards:
        if usercard.user_id == session['user_id']:
            count_of_cards += 1

    return render_template('user_details.html', user=user,
                                                usercards=usercards,
                                                card=card,
                                                count_of_cards=count_of_cards)


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""

    order_total = 0
    shopping_cart = []

    cart = session.get("cart", {})

    for user_card_id, quantity in cart.items():
        usercard = crud.get_user_card_by_id(user_card_id)
        
        order_total += usercard.card.price
        shopping_cart.append(usercard)

    return render_template("cart.html",
                           cart=cart,
                           order_total=order_total,
                           shopping_cart=shopping_cart)


@app.route("/add_to_cart/<user_card_id>")
def add_to_cart(user_card_id):
    """Add a usercard to cart and redirect to shopping cart page."""

    if 'cart' in session:
        cart = session['cart']
    else:
        cart = session['cart'] = {}

    cart[user_card_id] = cart.get(user_card_id, 0) + 1

    flash("Card successfully added to cart.")

    return redirect("/cart")



@app.route("/checkout")
def checkout():
    """Checkout customer and process payment."""

    return render_template('checkout.html')


@app.route("/checkout", methods=["POST"])
def create_order():
    """Create an order from items in cart."""

    shopping_cart = session.get('cart')

    user_logged_in = session.get("user_id")
    user = crud.get_user_by_id(user_logged_in)

    if user_logged_in is None:
        flash("Please log in to trade cards.")
        return redirect("/login")
        
    else:
        for user_card_id, _quantity in shopping_cart.items():
            usercard = crud.get_user_card_by_id(user_card_id)
            order = crud.create_order(usercard, user, date.today(), date.today())
            db.session.add(order)
        db.session.commit()

    flash("Your order has been processed!")

    return redirect("/checkout")


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

    return redirect('/login')
    
    
@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")

        return redirect(request.referrer)

    else:
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.name.title()}!")


        return redirect("/")



@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["user_id"] 
    flash("Logged out.")
    return redirect("/")





if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
