from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField


class DataForm(FlaskForm):
    image = FileField("Upload Image", validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    submit = SubmitField("Submit")