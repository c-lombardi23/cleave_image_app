# app/config.py
import os
import tensorflow as tf
import joblib
from dotenv import load_dotenv
import xgboost
from tensorflow.keras.models import Model

load_dotenv()

def load_models():

    return {
        "cnn_model": tf.keras.models.load_model(os.getenv("CNN_MODEL_PATH")),
        "xgb_model": joblib.load(os.getenv("XGB_MODEL")),
        "scaler": joblib.load(os.getenv("SCALER_PATH")),
        "xgb_scaler": joblib.load(os.getenv("XGB_SCALER"))
        
    }
