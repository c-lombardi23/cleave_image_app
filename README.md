# LDC Cleave Classifier & Tension Predictor

An AI-powered web app for analyzing fiber cleaves and predicting optimal tension settings to improve cleave quality.

---

## Project Overview

This web application allows engineers to upload cleave images from the **THORLABS LDC400** system. It performs two main tasks:

1.  **Classifies** the cleave as either **good** or **bad** using a CNN model.
2.  If the cleave is bad, it uses a **regression model** to predict the change in **tension value** needed to improve the result.

The app is designed to be quick and easy for use in real lab settings.

---

## How It Works

- Upload a cleave image through the browser.
- The app uses a pre-trained image and feature model to classify the cleave.
- If the cleave is bad, the regression model recommends a better tension value direction.
- Feedback is shown on-screen immediately

---

## Features

-  Deep learning classification using **EfficientNetB0** for transfer learning.
-  Dual-branch architecture: one for images, one for numerical parameters.
-  Tension prediction using a custom **regression model**.
-  Automatic image preprocessing including resizing and normalization.
-  Secure form input via **Flask-WTF** with CSRF protection.
-  Clean UI built with **Bootstrap 5**.

---

## What You Can Do

| Action               | Description |
|----------------------|-------------|
| Upload an image      | Submit a cleave photo from the THORLABS FCA system |
| Get a quality result | The model tells you whether the cleave is good or bad |
| Predict new tension  | If bad, the app suggests a direction to change tension for performing cleave |

---

## 🛠 Tech Stack

- Python
- Flask
- TensorFlow / Keras
- Keras Tuner
- Bootstrap 5
- WTForms
- Pillow + NumPy
- dotenv + joblib

---

##  How to Launch Locally

1. Create virtual enviornment:
   ```bash

   # Create virtual enviornment
   python -m venv myenv
   # On Windows
   source myenv/Scripts/activate
   # On mac/linux
   source myenv/bin/activate
   ```

2. Clone the repository
```bash

   git clone https://github.com/c-lombardi23/cleave_image_app.git
   cd cleave_image_app
   pip install -r requirements.txt
   ```

3. Create .env file
```bash

   #I provided a .env.exmaple file for you to use
   #add
   CNN_MODEL_PATH=models/Unified_classifier.keras
   SCALER_PATH=models/Unified_classifier_feature_scaler.pkl
   XGB_MODEL=models/Unified_regressor.pkl
   XGB_SCALER=models/Unified_regressor_scaler.pkl
   THRESHOLD=0.5
   ```

4. Run app
```bash

   flask --app app.py run
   ```
