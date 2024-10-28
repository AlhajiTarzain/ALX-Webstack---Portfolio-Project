# Flavor Folio - Recipe Sharing Platform

## Project Overview
Flavor Folio is a recipe-sharing platform built using Flask, designed for users
to share their favorite recipes with others. Users can sign up, log in, and
upload their recipes, including categories, difficulty levels, ingredients, and
images. It provides functionalities for user registration, login, creating recipes,
viewing all recipes, updating, and deleting them.

## Key Features
* User Registration: Users can register, providing their username, email, password, and an optional profile image.yes.
* Login: Registered users can log in with their credentials.
* Recipe Submission: Users can submit recipes with details such as title, category, difficulty level, ingredients, and a recipe image.
* View Recipes: Anyone can view a list of recipes shared by all users.
* Update Recipes: Users can update their submitted recipes.
* Delete Recipes: Users can delete their own recipes.
* Logout: Users can log out of the platform.

## Installation and Setup
### Prerequisites
Before starting, ensure you have the following installed on your system:
* [Python 3.x](https://www.python.org/) - Programming language required for running the application.

The following packages are necessary for the application to run. You can install them using pip:

* [Flask](https://flask.palletsprojects.com/) - A lightweight web framework for building web applications.
* [Flask-WTF](https://flask-wtf.readthedocs.io/) - Flask integration with WTForms for form handling and validation.
* [Flask-Login](https://flask-login.readthedocs.io/) - User session management for Flask applications.
* [Flask-Migrate](https://flask-migrate.readthedocs.io/) - Database migrations handled through Alembic, a tool for handling schema changes.
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - SQLAlchemy integration for Flask, to manage database interactions.
* [SQLite](https://www.sqlite.org/) - Database engine; used here as a lightweight database option.

## Installation
```
# Clone the repository:
git clone https://github.com/yourusername/flavorfolio.git
cd flavorfolio

# Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required packages:
pip install -r requirements.txt

# Initialize the database:
flask db init
flask db migrate
flask db upgrade

# Run the application:
python run.py
# Access the application at http://127.0.0.1:5000/.
```

### Project Structure
```
flavorfolio/
├── app/
│   ├── __init__.py        # Application setup and configuration
│   ├── forms.py           # Forms for user registration, login, and recipe submission
│   ├── models.py          # Database models for users and recipes
│   ├── routes.py          # Application routes and views
├── static/
│   └── images/            # Directory to store uploaded images
├── templates/
│   ├── home.html          # Homepage template showing all recipes
│   ├── login.html         # Login page
│   ├── submit_recipe.html # Recipe submission form
├── run.py                 # Entry point for running the application
├── foodfolio.db           # SQLite database (auto-generated)
└── README.md              # Project documentation (this file)
```
## Configuration
Configurations for the app are set in __init__.py. Some of the key configurations include:

SECRET_KEY: A secret key used for securing sessions.
SQLALCHEMY_DATABASE_URI: The URI for the SQLite database.
UPLOAD_FOLDER: Folder where images are uploaded.

## Forms
* RegistrationForm: Handles user registration (username, email, password, profile image).
* LoginForm: Handles user login (email and password).
* RecipeForm: Allows users to submit new recipes (title, category, difficulty, ingredients, and image).
Models

* User: Stores user data including username, email, hashed password, and profile image.
* Recipe: Stores recipe data including title, category, difficulty level, ingredients, and image.

### Routes
/register: User registration route.

/login: User login route.

/submit_recipe: Recipe submission route (protected).

/recipes: View all recipes.

/recipe/update/<int:recipe_id>: Update an existing recipe.

/recipes/<int:id>/delete: Delete a recipe (protected).

/search?q=<title or origin or >



/logout: Logout route.

### Database
The platform uses SQLite as its database engine. Flask-Migrate is used for managing migrations.

## Running Tests
To ensure everything is working correctly, you can test the platform's functionalities
by registering, logging in, and performing operations like submitting, updating, and deleting recipes.

## Future Enhancements
* Add a rating system for recipes.
* Implement recipe search functionality.
* Enable comment sections for users to discuss recipes.

## AUTHORS
* ALIY ZAINUL ABIDEEN TAHIRU
*LinkedIn - Aliy Zainul Abideen Tahiru
*Email- Dredeen21@gmail.com
