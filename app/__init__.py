from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SECRET_KEY'] = '4f8d7f8e1a3b4e6a8e9b34c5d4e1c72'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodfolio.db'  # Ensure this matches your DB name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to avoid overhead
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static')

    # Temporarily disable CSRF protection for testing
    app.config['WTF_CSRF_ENABLED'] = False  # Comment this line to enable CSRF protection

    # Initialize the extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Specify login route
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # Import models after db is initialized to avoid circular import
    from app.models import User

    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
