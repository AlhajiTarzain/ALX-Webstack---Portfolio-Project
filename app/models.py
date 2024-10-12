from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.string(15),Unique = True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(120), default='default_profile.jpg')
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
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
        return f"Recipe('{self.title}', '{self.date_posted}',{self.category})"