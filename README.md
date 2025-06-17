# 🧪 LDC Cleave Classifier & Tension Predictor

An AI-powered web app for analyzing fiber cleaves and predicting optimal tension settings to improve cleave quality.

---

## 🌐 Project Overview

This web application allows fiber optics technicians to upload cleave images from the **THORLABS LDC400** system. It performs two main tasks:

1. ✅ **Classifies** the cleave as either **good** or **bad** using a CNN model.
2. 🔧 If the cleave is bad, it uses a **regression model** to predict the optimal **tension value** to improve the result.

The app is designed to be intuitive, fast, and useful in real lab settings.

---

## 🧠 How It Works

- Upload a cleave image through the browser.
- Fill in metadata: cleave angle, tension, misting, hackle, tearing, etc.
- The app uses a pre-trained image+feature model to classify the cleave.
- If the cleave is bad, the regression model recommends a better tension value.
- Feedback is shown on-screen immediately — no downloads or retraining required.

---

## 💡 Features

- ✅ Deep learning classification using **MobileNetV2** (transfer learning).
- 🔁 Dual-branch architecture: one for images, one for numerical parameters.
- 🔧 Tension prediction using a custom **regression model**.
- 🖼️ Automatic image preprocessing (resizing, normalization).
- 🔐 Secure form input via **Flask-WTF** with CSRF protection.
- 🎨 Clean UI built with **Bootstrap 5**.

---

## 📋 What You Can Do

| Action               | Description |
|----------------------|-------------|
| Upload an image      | Submit a cleave photo from the THORLABS FCA system |
| Enter cleave data    | Provide angle, tension, and binary labels for misting, hackle, and tearing |
| Get a quality result | The model tells you whether the cleave is good or bad |
| Predict new tension  | If bad, the app suggests a better tension value for retrying |

---

## 🛠 Tech Stack

- Flask (Python)
- TensorFlow / Keras
- Keras Tuner
- Bootstrap 5
- WTForms
- Pillow + NumPy
- dotenv + joblib

---

## 🚀 How to Launch

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ldc-cleave-classifier.git
   cd ldc-cleave-classifier
