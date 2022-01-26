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

# @app.route('/movies')
# def all_movies():
#     """View movies page."""

#     movies = crud.get_movies()

#     return render_template('all_movies.html', movies=movies)


# @app.route('/users')
# def all_users():
#     """View users page."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users)


# @app.route('/movies/<movie_id>')
# def show_movie(movie_id):
#     """Show movie detailes."""

#     movie = crud.get_movie_by_id(movie_id)

#     return render_template('movie_details.html', movie=movie)



# @app.route('/users/<user_id>')
# def show_user(user_id):
#     """Show user detailes."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

# @app.route("/users", methods=["POST"])
# def register_user():
#     """Create a new user."""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.get_user_by_email(email)

#     if user:
#          flash("Cannot create an account with that email. Try again.")
#     else:
#         user = crud.create_user(email, password)
#         db.session.add(user)
#         db.session.commit()
#         flash("Account created! Please log in.")

#     return redirect("/")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
