from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DecimalField, DecimalRangeField, validators

class WineForm(FlaskForm):
    f_acid = DecimalRangeField("Fixed Acidity", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    v_acid = DecimalRangeField("Volatile Acidity", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    c_acid = DecimalRangeField("Citric Acidity", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    r_sugar = DecimalRangeField("Residual Sugar", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    chlorides = DecimalRangeField("Volatile Acidity", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    fs_dioxide = DecimalRangeField("Free Sulfur Dioxide", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    ts_dioxide = DecimalRangeField("Total Sulfur Dioxide", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    density = DecimalRangeField("density", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    ph = DecimalRangeField("pH", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    sulphates = DecimalRangeField("Sulphates", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    alcohol = DecimalRangeField("Alcohol", [validators.DataRequired()], render_kw={'style': 'width: 90%'})
    submit = SubmitField('Submit')
