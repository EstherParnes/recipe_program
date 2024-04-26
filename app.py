from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Todo {self.id}-{self.title}-{self.complete} >'
"""


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    ingredients = db.Column(db.Text)
    directions = db.Column(db.Text)

    def __repr__(self):
        return f'<Recipe {self.title}>'
# MAKE SURE TO DO create_all() in flask shell
# see https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# db.create_all()


"""
#  THIS IS ELENA'S CODE
@app.get("/")
def home():
    # todo_list = Todo.query.all()
    recipe_list = db.session.query(Recipe).all()
    #return render_template("base.html", recipe_list=recipe_list)
    return render_template("base_DO.html", recipe_list=recipe_list)

"""
# THIS IS DIGITAL OCEAN CODE
@app.route('/')
def index():
    # students = Student.query.all()
    #recipe_list = db.session.query(Recipe).all()
    recipes = Recipe.query.all()
    return render_template('index_DO.html', recipes=recipes)
# ...


@app.route('/<int:recipe_id>/')
def recipe (recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', recipe=recipe)
