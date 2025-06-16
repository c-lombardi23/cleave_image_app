from flask import Flask, request, jsonify, render_template, flash
import os
import warnings
from flask_bootstrap import Bootstrap5
import secrets
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.fields import FloatField, IntegerField, RadioField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileField
from werkzeug.utils import secure_filename
import joblib as jb
from PIL import Image
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')
import tensorflow as tf

app = Flask(__name__)
cnn_model_path = "C:\\Users\\clombardi\\125pm_best_model.keras"
mlp_model_path = "C:\\Users\clombardi\\125pm_best_mlp_model_6_13.keras"
scaler_path = "C:\\Users\\clombardi\\125pm_scaler.pkl"
feature_scaler_path = "C:\\Users\\clombardi\\mlp_feature_scaler_6_13.pkl"
tension_scaler_path = "C:\\Users\\clombardi\\mlp_tension_scaler_6_13.pkl"

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

foo = secrets.token_urlsafe(16)
app.secret_key = foo

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

cnn_model = tf.keras.models.load_model(cnn_model_path)
mlp_model = tf.keras.models.load_model(mlp_model_path)
scaler = jb.load(scaler_path)
feature_scaler = jb.load(feature_scaler_path)
tension_scaler = jb.load(tension_scaler_path)

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

def preprocess_image(uploaded_file):
    # resize image and normalize
    try:
        img = Image.open(uploaded_file)  
        img = img.resize((224, 224))
        img = img.convert("RGB")  # Convert to 3 channels
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 224, 224, 3)
        return img_array
    except Exception as e:
        print(f"Image preprocessing failed: {e}")
        return None
    
def test_prediction(image, cleave_angle, cleave_tension, scribe_diamter, misting, hackle, tearing):
    '''
    Test function for generating prediction

    Parameters:
    ----------------------------------------------

    image_path: str
      - path to image to predict
    tension: int
      - tension value in grams
    cleave_angle: float
      - angle that was achieved from cleave

    Return: tf.keras.Model
      - predicition from new image of good or bad cleave
    '''
    image = preprocess_image(image)
    def process_features(cleave_angle, cleave_tension, scribe_diameter, misting, hackle, tearing):
      features = np.array([[cleave_angle, cleave_tension, scribe_diameter, misting, hackle, tearing]])
      features = scaler.transform(features)
      return features
    features = process_features(cleave_angle, cleave_tension, scribe_diamter, misting, hackle, tearing)
    prediction = cnn_model.predict([image, features])
    return prediction

def predict_tension(image, cleave_angle, scribe_diameter, misting, hackle, tearing):
        '''
        Predict tension for given image and angle

        Parameters:
        -------------------------------------
        model: tf.keras.Model
            - Model to be used for prediction
        image_path: str
            - Path to image to be used for prediction
            angle: float
            - Angle to be used for prediction

        Returns:
        float
            - Predicted tension
        '''
        # Process image and convert angle and image to tensor with dimension for single batch
        image = preprocess_image(image)
        def process_features(cleave_angle, scribe_diameter, misting, hackle, tearing):
            features = np.array([[cleave_angle, scribe_diameter, misting, hackle, tearing]])
            features = feature_scaler.transform(features)
            return features
        features = np.array(process_features(cleave_angle, scribe_diameter, misting, hackle, tearing)).reshape(1, -1)
        features = tf.convert_to_tensor(features, dtype=tf.float32)
        # Predict tension
        predicted_tension =mlp_model.predict([image, features])
        # Scale tension back to normal units
        predicted_tension = tension_scaler.inverse_transform(predicted_tension)
    
        return predicted_tension[0][0]


@app.route('/', methods=['GET', 'POST'])
def home():
    form = DataForm()
    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        form.image.data.save(file_path)
        fiber_type = form.fiber_type.data
        cleave_angle = form.cleave_angle.data
        cleave_tension = form.cleave_tension.data
        scribe_diameter = form.scribe_diameter.data
        misting = form.misting.data
        hackle = form.hackle.data
        tearing = form.tearing.data

        prediction = test_prediction(file, cleave_angle, cleave_tension, scribe_diameter, int(misting), int(hackle), int(tearing))
        if prediction >= 0.5:
            flash("Good Cleave", category="cleave_quality")
        else:
            tension = predict_tension(file, cleave_angle, scribe_diameter, misting, hackle, tearing)
            flash(f"Bad Cleave, Adjust Tension To: {tension:.0f}g", category = "cleave quality")           
    print(form.errors)
    return render_template("index.html", form=form)
