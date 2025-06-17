# app/config.py
import os
import tensorflow as tf
import joblib
from dotenv import load_dotenv

load_dotenv()

def load_models():
    return {
        "cnn_model": tf.keras.models.load_model(os.getenv("CNN_MODEL_PATH")),
        "mlp_model": tf.keras.models.load_model(os.getenv("MLP_MODEL_PATH")),
        "scaler": joblib.load(os.getenv("SCALER_PATH")),
        "feature_scaler": joblib.load(os.getenv("FEATURE_SCALER_PATH")),
        "tension_scaler": joblib.load(os.getenv("TENSION_SCALER_PATH")),
    }
