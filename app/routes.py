from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from app import db
from app.forms import RegistrationForm, LoginForm, RecipeForm
from app.models import User, Recipe

# Create a blueprint
main = Blueprint('main', __name__)

# Home route (optional)
@main.route('/')
def home():
    return render_template('home.html', title='Home')

# Registration route
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        # Handle profile image upload
        if form.profile_image.data:
            filename = secure_filename(form.profile_image.data.filename)
            form.profile_image.data.save(os.path.join('static/profile_images', filename))
            user.profile_image = filename
        
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

# Login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))  # Redirect to home or profile page
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Recipe submission route
@main.route('/submit_recipe', methods=['GET', 'POST'])
@login_required  # Protect this route
def submit_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            category=form.category.data,
            difficulty=form.difficulty.data,
            origin=form.origin.data,
            ingredients=form.ingredients.data,
            user_id=current_user.id
        )
        
        # Handle recipe image upload
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join('static/recipe_images', filename))
            recipe.image = filename
        
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('submit_recipe.html', title='Submit Recipe', form=form)

# Logout route
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('main.home'))

# Register the blueprint in the create_app function of __init__.py
# Make sure to include this line in your __init__.py
# from app.routes import main
# app.register_blueprint(main)
