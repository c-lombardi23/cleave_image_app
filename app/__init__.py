from flask import Flask
import os
import warnings
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')
import tensorflow as tf
from .routes import create_routes
from .config import load_models

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    Bootstrap5(app)
    CSRFProtect(app)
    create_routes(app)
    app.models = load_models()

    return app

