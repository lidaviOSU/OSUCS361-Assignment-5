from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehs.db'
db = SQLAlchemy(app)

class MSDS(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    cas = db.Column(db.String(length=50), nullable=False)
    internal = db.Column(db.Integer(), nullable=False, unique=True)
    year = db.Column(db.Integer(), nullable=False)
    user = db.Column(db.String(length=50), nullable=False)
    vendor = db.Column(db.String(length=50), nullable=False)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')


@app.route('/MSDS')
def msds():
    data = [
        {'Name': 'Methanol', 'Cas': '67-56-1', 'Internal': 1, 'Year': 2022, 'User': 'davidli', 'Vendor': 'Vendor1'},
        {'Name': 'Ethanol', 'Cas': '64 - 17 - 5', 'Internal': 8, 'Year': 2022, 'User': 'davidli',
         'Vendor': 'Vendor3'},
        {'Name': 'Ethylene Oxide', 'Cas': '75 - 21 - 8', 'Internal': 42, 'Year': 2022, 'User': 'davidli',
         'Vendor': 'Vendor15'},
        {'Name': 'Hydrochloric Acid', 'Cas': '7647 - 01 - 0', 'Internal': 103, 'Year': 2022, 'User': 'davidli',
         'Vendor': 'Vendor1'}
    ]
    return render_template('msds.html', data=data)

@app.route('/hazards')
def hazards():
    hazard = [
        {'Assessment': 'Ladder Use', 'ProductRef': 'Cell Bank', 'Year': 2022, 'User': 'davidli', 'Comments': 'Ladder usage in cell banking area'},
        {'Assessment': 'Forklift Usage', 'ProductRef': 'NA', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Forklift usage plant wide assessment'},
        {'Assessment': 'Product Milling', 'ProductRef': 'Secret X', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Ergonomic Assessment of milling activities for secret x product'},
        {'Assessment': 'Welder Usage', 'ProductRef': 'NA', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Site wide assessment of welder usage'}
    ]
    return render_template('hazards.html', hazard=hazard)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/yes')
def yes():
    return render_template('no.html')

@app.route('/no')
def no():
    return render_template('no.html')

@app.route('/search')
def search():
    return render_template('search.html')