import os
import warnings

from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")
import tensorflow as tf

from .config import load_config, load_models
from .routes import create_routes


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "uploads")
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    Bootstrap5(app)
    CSRFProtect(app)
    create_routes(app)
    app.models = load_models()
    app.threshold = os.getenv("THRESHOLD")
    cnn_model = app.models['cnn_model']
    app.models["feature_extractor"] = tf.keras.Model(
        inputs=cnn_model.input[0], 
        outputs=cnn_model.get_layer("global_avg").output
    )

    return app
