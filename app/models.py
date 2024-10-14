from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # Import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db  # Ensure you're importing db from your app package
from sqlalchemy import Column, Integer, String


class User(UserMixin, db.Model):  # Inherit from UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Store hashed password
    profile_image = db.Column(db.String(120), default='profile.jpeg')
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    # Use werkzeug to hash the password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Use werkzeug to check if the provided password matches the stored hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    origin = db.Column(db.String(100))
    ingredients = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(120), default='default.jpg')  # Default image
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.date_posted}', '{self.category}')"
