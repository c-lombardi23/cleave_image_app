import os
import warnings

import numpy as np
import tensorflow as tf
from flask import current_app, flash, render_template
from PIL import Image

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")
import tensorflow as tf
from tensorflow.keras.models import Model

from .forms import *


def preprocess_image(uploaded_file):
    # resize image and normalize
    try:
        img = Image.open(uploaded_file)
        if img is None:
            flash("Invalid image uploaded.", category="error")
            return render_template("index.html", form=DataForm())
        img = img.resize((224, 224))  # size of images trained on efficientnet
        img = img.convert("RGB")  # Convert to 3 channels
        img_array = np.array(img)
        img_array = np.expand_dims(
            img_array, axis=0
        )  # Shape: (1, 224, 224, 3)
        return img_array

    except Exception as e:
        print(f"Image preprocessing failed: {e}")
        return None


def extract_features(cnn_model):
    feature_extractor = Model(
        inputs=cnn_model.input[0],
        outputs=cnn_model.get_layer("global_avg").output,
    )
    return feature_extractor


def test_prediction(image):
    """
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
    """
    image = preprocess_image(image)
    features = np.zeros(shape=(5,))
    features = np.expand_dims(features, axis=0)
    prediction = current_app.models["cnn_model"].predict([image, features])
    feature_extractor = extract_features(current_app.models["cnn_model"])
    img_features = feature_extractor(image).numpy()
    tensions_prediction = current_app.models["xgb_model"].predict(img_features)
    delta = current_app.models["xgb_scaler"].inverse_transform(
        tensions_prediction.reshape(1, -1)
    )

    return prediction, delta
