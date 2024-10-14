from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Configurations
    app.config['SECRET_KEY'] = '4f8d7f8e1a3b4e6a8e9b34c5d4e1c72'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flavorfolio.db'  # Database configuration
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static')

    # Initialize the extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    # Specify login route
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'
    
    # Import blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Create database models (optional if not using migrations)
    with app.app_context():
        db.create_all()

    return app
