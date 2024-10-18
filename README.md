**Flavor Folio**

Flavor Folio is a recipe-sharing platform where users can create an account, log in, and submit recipes with images. Users can view, update, and delete their own recipes while browsing other users' creations.

**Features**

User Authentication: Users can register, log in, and log out.
Recipe Management: Users can submit, update, view, and delete recipes.
Image Uploads: Profile and recipe images can be uploaded.
Category and Difficulty Selection: Users can categorize recipes by type (e.g., appetizer, main course, dessert) and difficulty (easy, medium, hard).
Technologies Used
Flask: Web framework
Flask-WTF: Form handling with validation
Flask-SQLAlchemy: ORM for database interactions
Flask-Login: User session management
Flask-Migrate: Database migrations
SQLite: Database (can be changed as needed)
HTML/CSS: For rendering templates and styling

**Setup Instructions**
**1. Clone the repository**
bash
Copy code
git clone https://github.com/AlhajiTarzain/ALX-Webstack---Portfolio-Project.git
cd your-repo-name
**2. Create and activate a virtual environment**
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/Mac
# OR
venv\Scripts\activate  # For Windows
**3. Install dependencies**
bash
Copy code
pip install -r requirements.txt
**4. Set up the database**
bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
**5. Run the application**
bash
Copy code
python run.py
The app will now be running at http://127.0.0.1:5000/.

**6. Register a User**
Navigate to the /register route and create a user account to start using the platform.

Routes
/register: Register a new user.
/login: Log in with an existing account.
/submit_recipe: Submit a new recipe (requires login).
/recipes: View all recipes.
/recipe/update/<int:recipe_id>: Update a recipe (requires login and recipe ownership).
/recipes/<int:id>/delete: Delete a recipe (requires login and recipe ownership).
/logout: Log out from the application.
File Structure
bash
Copy code
.
├── app/
│   ├── __init__.py          # App factory and configuration
│   ├── forms.py             # WTForms for user registration, login, and recipe submission
│   ├── models.py            # SQLAlchemy models for User and Recipe
│   ├── routes.py            # Flask routes for handling logic
├── run.py                   # Run the Flask app
├── requirements.txt         # Python dependencies
├── migrations/              # Flask-Migrate files for DB migrations
└── README.md                # Project documentation (this file)
Database
This project uses SQLite by default. The database file is named foodfolio.db and is created automatically in the project folder. To switch to another database like PostgreSQL or MySQL, update the SQLALCHEMY_DATABASE_URI in __init__.py.

To Do
Improve UI with a frontend framework.
Add pagination for recipes.
Add recipe search and filter functionality.
License
This project is licensed under the MIT License.
