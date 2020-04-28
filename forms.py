from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    cuisine = StringField('Cuisine type')
    location = StringField('City')
    price = StringField('Price')
    submit = SubmitField('Find meals')
    # can add price range and eta later
