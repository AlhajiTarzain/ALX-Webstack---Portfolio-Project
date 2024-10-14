from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileAllowed  # Import to validate file uploads

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])  # Added password length validation
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    profile_image = FileField('Profile Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])  # Validate image file type
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    category = SelectField('Category', 
                           choices=[('appetizer', 'Appetizer'), 
                                    ('main_course', 'Main Course'), 
                                    ('dessert', 'Dessert')],
                           validators=[DataRequired()])
    difficulty = SelectField('Difficulty Level',
                             choices=[('easy', 'Easy'),
                                      ('medium', 'Medium'),
                                      ('hard', 'Hard')],
                             validators=[DataRequired()])
    origin = StringField('Country of Origin')
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    image = FileField('Recipe Image', validators=[FileAllowed(['jpg', 'png'], 'Pictures Images only!')])  # Validate image file type
    submit = SubmitField('Submit Recipe')