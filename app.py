import os
from itertools import islice
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

from modelling.modelling import get_model_fit

from form import WineForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '571ebf8e13ca209536c29be68d435c00'
Bootstrap(app)

def predict_outcome(model, fit, test):
    test = fit.transform(test)
    pred = model.predict(test)
    return int(pred[0])

@app.route('/', methods=['POST', 'GET'])
def index():
    quality=1
    form = WineForm()

    model, fit = get_model_fit()

    if form.validate_on_submit():
        print('yes')

        test = []
        insert_test = []
        for fieldname, value in islice(form.data.items(), 11):
            test.append(float(value))
        print(insert_test)
        insert_test.append(test)
        quality = predict_outcome(model, fit, insert_test)

    return render_template('index.html', form=form, quality=quality)

if __name__ == "__main__":
    app.run(debug=True)