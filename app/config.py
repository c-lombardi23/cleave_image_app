# app/config.py
import os

import joblib
import tensorflow as tf
import xgboost
from dotenv import load_dotenv
from tensorflow.keras.models import Model


load_dotenv()


def load_models():

    return {
        "cnn_model": tf.keras.models.load_model(os.getenv("CNN_MODEL_PATH")),
        "xgb_model": joblib.load(os.getenv("XGB_MODEL")),
        "scaler": joblib.load(os.getenv("SCALER_PATH")),
        "xgb_scaler": joblib.load(os.getenv("XGB_SCALER"))
    }


def load_config():
    return {"threshold": float(os.getenv("THRESHOLD", 0.5))}
