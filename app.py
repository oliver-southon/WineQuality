import os
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

from models.modelling import get_model_fit, form_data_2dArray, predict_outcome

from models.forms import WineForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '571ebf8e13ca209536c29be68d435c00'
Bootstrap(app)

def predict_outcome(model, fit, test):
    test = fit.transform(test)
    pred = model.predict(test)
    return int(pred[0])

@app.route('/', methods=['POST', 'GET'])
def index():
    quality=None # placeholder
    form = WineForm()

    model, fit = get_model_fit() # Create model w/ normalised data once so it can be used every time the form is submitted

    if form.validate_on_submit():
        test = form_data_2dArray(form.data, 11) # convert parameters to normalised data
        quality = predict_outcome(model, fit, test) # Get the outcome
 
    return render_template('index.html', form=form, quality=quality)

# For viewing Jupyter Notebook work
@app.route('/modelling')
def modelling():
    return render_template('modelling.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')