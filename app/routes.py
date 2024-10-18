from flask import render_template, url_for, flash, redirect, request, Blueprint,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.forms import RegistrationForm, LoginForm, RecipeForm
from app.models import User, Recipe
import os

# Create a blueprint
main = Blueprint('main', __name__)

# Home route (optional)
#@main.route('/home')
#def home():
#    return jsonify({"message": "this is home"})

@main.route('/home')
#@login_required
def home():
    recipes = Recipe.query.all()  # Fetch all recipes from the database
    return render_template('home.html', recipes=recipes)

# Registration route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegistrationForm(request.form)  # Pass request.form to the form
        
        if form.validate():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)  # Hash password using werkzeug
            
            # Handle profile image upload
            if form.profile_image.data:
                filename = secure_filename(form.profile_image.data.filename)
                form.profile_image.data.save(os.path.join('static/images', filename))
                user.profile_image = filename
            
            db.session.add(user)
            db.session.commit()
            
            return jsonify({"message": "Your account has been created! You can now log in."}), 201
        
        # Return specific validation errors
        return jsonify({"errors": form.errors}), 400
    
    return jsonify({"message": "Please submit the registration form."}), 200


# Login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):  # Check password using werkzeug
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
            # Ensure 'static/images' directory exists
            image_dir = os.path.join('static', 'images')
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            # Save the uploaded image
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(image_dir, filename))
            recipe.image = filename
        
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe has been submitted!', 'success')
        return redirect(url_for('main.home'))
    else:
        return jsonify({"error_msg":"validation error","error":form.errors})
    return render_template('submit_recipe.html', title='Submit Recipe', form=form)

@main.route('/recipe/update/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Fetch the recipe or return a 404 error
    form = RecipeForm(obj=recipe)  # Prepopulate the form with existing recipe data

    if form.validate_on_submit():  # Check if the form is submitted and valid
        form.populate_obj(recipe)  # Populate the recipe object with form data
        db.session.commit()  # Commit the changes to the database
        flash('Recipe updated successfully!', 'success')
        return jsonify({"message": "Recipe updated successfully!"}), 200  # Return a JSON response if needed
    return jsonify({"error": "Failed to update recipe"}), 400  # Handle error in updating

# Delete recipe route
@main.route('/recipes/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_recipe(id):
    # Fetch the recipe by ID
    recipe = Recipe.query.get_or_404(id)
    
    # Check if the current user is the author of the recipe
    if recipe.author != current_user:
        return jsonify({"error": "You are not authorized to delete this recipe"}), 403
    
    # Delete the recipe
    db.session.delete(recipe)
    db.session.commit()
    
    return jsonify({"message": f"Recipe '{recipe.title}' has been deleted."}), 200

# View all recipes route
@main.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()  # Fetch all recipes from the database
    recipes_data = []

    # Loop through recipes and serialize them into a list of dictionaries
    for recipe in recipes:
        recipes_data.append({
            'title': recipe.title,
            'category': recipe.category,
            'difficulty': recipe.difficulty,
            'origin': recipe.origin,
            'ingredients': recipe.ingredients,
            'image': recipe.image,
            'date_posted': recipe.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
            'author': recipe.author.username
        })

    # Return the serialized recipes as a JSON response
    return jsonify({'recipes': recipes_data}), 200

# Logout route
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('main.home'))

@main.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Hello, this is a test!"})