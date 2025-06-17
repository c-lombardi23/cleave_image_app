<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LDC Cleave Classifier & Tension Predictor</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light text-dark">

  <div class="container my-5">
    <h1 class="display-4 text-center">LDC Cleave Classifier & Tension Predictor</h1>
    <p class="lead text-center">An AI-powered web app for analyzing fiber cleaves and predicting optimal tension settings.</p>

    <hr>

    <section>
      <h2> Project Overview</h2>
      <p>
        This app allows fiber optics technicians to upload cleave images from the <strong>THORLABS LDC400</strong> system, classify them as <strong>good</strong> or <strong>bad</strong>, and—if necessary—predict the <strong>optimal tension</strong> to achieve a better cleave.
      </p>
    </section>

    <section>
      <h2> How It Works</h2>
      <ul>
        <li>Upload a cleave image</li>
        <li>Enter cleave metadata: tension, angle, misting, etc.</li>
        <li>The app classifies the cleave using a CNN model</li>
        <li>If bad, a regression model estimates a better tension</li>
        <li>Results are shown instantly on screen</li>
      </ul>
    </section>

    <section>
      <h2> Features</h2>
      <ul>
        <li><strong>Deep learning classification</strong> using MobileNetV2</li>
        <li><strong>Regression prediction</strong> of optimal tension</li>
        <li>Automatic image preprocessing</li>
        <li>Secure form input (CSRF-protected)</li>
        <li>Bootstrap-based responsive UI</li>
      </ul>
    </section>

    <section>
      <h2> What You Can Do</h2>
      <table class="table table-bordered">
        <thead>
          <tr><th>Action</th><th>Description</th></tr>
        </thead>
        <tbody>
          <tr><td>Upload an image</td><td>Submit a cleave photo directly from your FCA</td></tr>
          <tr><td>Input cleave data</td><td>Provide tension, angle, misting, etc. via form</td></tr>
          <tr><td>Get immediate feedback</td><td>Know if the cleave was good or bad</td></tr>
          <tr><td>Predict tension</td><td>Get a recommended cleave tension for retrying failed cleaves</td></tr>
        </tbody>
      </table>
    </section>

    <section>
      <h2>🛠 Tech Stack</h2>
      <ul>
        <li>Flask (Python)</li>
        <li>TensorFlow / Keras</li>
        <li>Keras Tuner</li>
        <li>Bootstrap 5</li>
        <li>WTForms</li>
        <li>Pillow + NumPy</li>
        <li>dotenv + joblib</li>
      </ul>
    </section>

    <section>
      <h2>📸 Demo Screenshot</h2>
      <p><em>(Insert a screenshot or GIF of your app in action here)</em></p>
    </section>

    <section>
      <h2> How to Launch</h2>
      <ol>
        <li>Clone the repository</li>
        <li>Create a <code>.env</code> file with your model/scaler paths</li>
        <li>Run <code>flask run</code></li>
        <li>Open <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a> in your browser</li>
      </ol>
    </section>

    <section>
      <h2> Author</h2>
      <p><strong>Chris Lombardi</strong><br>
     Machine learning researcher<br>
      Intern THORLABS</p>
    </section>

    <footer class="text-center mt-5">
      <p>&copy; 2025 Chris Lombardi — All rights reserved.</p>
    </footer>
  </div>

</body>
</html>
