from flask_wtf import FlaskForm
from wtforms.fields import FloatField, IntegerField, RadioField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileField


class DataForm(FlaskForm):
    image = FileField("Upload Image", validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    fiber_type = StringField("Enter Fiber Type", validators=[DataRequired(), Length(0,50)])
    cleave_angle = FloatField("Cleave Angle", validators=[DataRequired()])
    cleave_tension = IntegerField("Cleave Tension", validators=[DataRequired()])
    scribe_diameter = FloatField("Scribe Diameter", validators=[DataRequired()])
    misting = RadioField("Misting", choices=[('1', 'Yes'), ('0', 'No')])
    hackle = RadioField("Hackle  ", choices=[('1', 'Yes'), ('0', 'No')])
    tearing = RadioField("Tearing", choices=[('1', 'Yes'), ('0', 'No')])
    submit = SubmitField("Submit")