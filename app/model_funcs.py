from flask import render_template, flash, current_app
import warnings
from PIL import Image
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')
import tensorflow as tf

from .forms import *

def preprocess_image(uploaded_file):
    # resize image and normalize
    try:
        img = Image.open(uploaded_file)
        if img is None:
            flash("Invalid image uploaded.", category="error")
            return render_template("index.html", form=DataForm())
        img = img.resize((224, 224))
        img = img.convert("RGB")  # Convert to 3 channels
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 224, 224, 3)
        return img_array
    except Exception as e:
        print(f"Image preprocessing failed: {e}")
        return None
    
def test_prediction(image, cleave_angle, cleave_tension, scribe_diameter, misting, hackle, tearing):
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
      features = current_app.models["scaler"].transform(features)
      return features
    features = process_features(cleave_angle, cleave_tension, scribe_diameter, misting, hackle, tearing)
    prediction = current_app.models['cnn_model'].predict([image, features])
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
            features = current_app.models['feature_scaler'].transform(features)
            return features
        features = np.array(process_features(cleave_angle, scribe_diameter, misting, hackle, tearing)).reshape(1, -1)
        features = tf.convert_to_tensor(features, dtype=tf.float32)
        # Predict tension
        predicted_tension = current_app.models['mlp_model'].predict([image, features])
        # Scale tension back to normal units
        predicted_tension = current_app.models['tension_scaler'].inverse_transform(predicted_tension)
    
        return predicted_tension[0][0]

