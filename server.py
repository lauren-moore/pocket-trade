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





# @app.route('/login')
# def all_users():
#     """View log in page."""

#     return render_template('login.html')

# @app.route("/create-account")
# def view_register_user():
#     """Create a new user."""

#     return render_template('create_account.html')

# @app.route("/create-account", methods=["POST"])
# def register_user():
#     """Create a new user."""

#     name= request.form.get("name")
#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.get_user_by_email(email)

#     if user:
#          flash("An account has already been created with that email address. Try again.")
#     else:
#         user = crud.create_user(name, email, password)
#         db.session.add(user)
#         db.session.commit()
#         flash("Account created! Please log in.")

#         return redirect('login.html')
    

# @app.route('/users/<user_id>')
# def show_user_details(user_id):
#     """Show user details."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
