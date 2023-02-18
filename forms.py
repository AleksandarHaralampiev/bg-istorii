from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import Length ,EqualTo, Email, DataRequired
from datetime import datetime



class MessageForm(FlaskForm):
    title = StringField(label = "Title: ", validators = [Length(min = 5, max = 20), DataRequired()])
    message = StringField(label = "Message: ", validators = [Length(min = 10, max = 1500), DataRequired()])
    author = StringField(label = "Author: ", validators = [Length(min = 1, max = 20)], default='User')
    submit = SubmitField(label = "Submit")
    
