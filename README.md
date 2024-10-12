# FlavorFolio: Recipe Sharing Platform

FlavorFolio is a backend-powered platform where users can share, view, and manage their favorite recipes. It is built using Flask and provides functionality for user authentication, recipe posting, and management.

## Features

- **User Registration and Login**: Users can sign up and log in to their accounts to access the platform.
- **Recipe Management**: Users can create, update, and delete their own recipes.
- **Recipe Viewing**: All users, regardless of authentication, can browse through the available recipes.
- **RESTful API**: The platform supports RESTful endpoints for easy interaction with the backend.
- **Authentication**: Secure user authentication with password hashing.
  
## Technologies Used

- **Flask**: A lightweight Python web framework for building the backend.
- **SQLAlchemy**: For database modeling and ORM functionality.
- **Flask-Migrate**: For handling database migrations.
- **Flask-WTF**: For form validation and handling.
- **Flask-Bcrypt**: For password hashing.

## API Endpoints

| Method | Endpoint         | Description                    |
|--------|------------------|--------------------------------|
| POST   | `/signup`         | Register a new user            |
| POST   | `/login`          | Log in a user                  |
| POST   | `/recipes`        | Create a new recipe            |
| GET    | `/recipes`        | Get all recipes                |
| GET    | `/recipes/<id>`   | Get a specific recipe by ID     |
| PUT    | `/recipes/<id>`   | Update a recipe (auth required)|
| DELETE | `/recipes/<id>`   | Delete a recipe (auth required)|

## Setup and Installation

### Prerequisites
- Python 3.x
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flavorfolio.git
   cd flavorfolio
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the environment variables:

Create a .env file in the root directory and add the following:
bash
Copy code
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///recipes.db
Initialize the database:

bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the Flask application:

bash
Copy code
flask run
Visit the app in your browser at http://127.0.0.1:5000/.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Contact
For any inquiries or feedback, please reach out to me at your-email@example.com.