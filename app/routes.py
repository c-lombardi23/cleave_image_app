import os

from flask import flash, render_template, request, jsonify
from werkzeug.utils import secure_filename

from .forms import DataForm
from .model_funcs import test_prediction
import time


def create_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        form = DataForm()
        if request.method == "POST" and not form.validate():
            flash("Please correct the errors in the form.", category="error")
        if form.validate_on_submit():
            file = form.image.data
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            form.image.data.save(file_path)

            prediction, tension = test_prediction(file)
            print(prediction)
            threshold = app.threshold
            if prediction >= float(threshold):
                return jsonify({
                    'status': 'GOOD',
                    'message': "Good Cleave - No action needed"
                })
            else:
                print(tension)
                time.sleep(1)
                if tension > 0:
                    return jsonify({
                        'status': 'BAD',
                        'message': 'Bad Cleave - Increase in Tension Suggested'
                    })
                else:
                    return jsonify({
                        'status': 'BAD',
                        'message': "Bad Cleave - Decrease in Tension Suggested"
                    })
        print(form.errors)
        return render_template("index.html", form=form)
