from flask import request, render_template, flash
import os
from werkzeug.utils import secure_filename
from .forms import DataForm
from .model_funcs import test_prediction, predict_tension


def create_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        form = DataForm()
        if request.method == 'POST' and not form.validate():
            flash("Please correct the errors in the form.", category="error")
        if form.validate_on_submit():
            file = form.image.data
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.image.data.save(file_path)
            fiber_type = form.fiber_type.data
            cleave_angle = form.cleave_angle.data
            cleave_tension = form.cleave_tension.data
            scribe_diameter = form.scribe_diameter.data
            misting = form.misting.data
            hackle = form.hackle.data
            tearing = form.tearing.data

            prediction = test_prediction(file, cleave_angle, cleave_tension, scribe_diameter, int(misting), int(hackle), int(tearing))
            if prediction >= 0.5:
                flash("Good Cleave", category="cleave_quality")
            else:
                tension = predict_tension(file, cleave_angle, scribe_diameter, misting, hackle, tearing)
                flash(f"Bad Cleave, Adjust Tension To: {tension:.0f}g", category = "cleave_quality")           
        print(form.errors)
        return render_template("index.html", form=form)