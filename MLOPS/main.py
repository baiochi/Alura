# imports
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import os
import pandas as pd
import pickle

# instance Flask object
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'baiochi'
app.config['BASIC_AUTH_PASSWORD'] = 'batata'

basic_auth = BasicAuth(app)

# Load House Price Dataset
df = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv')
df.columns = ['size', 'year', 'garage', 'price']
# Load House Price Model
print(f'\033[36m{os.getcwd()}\033[39m')
with open('reg_lin_model','rb') as file:
    reg_lin = pickle.load(file)

# define API routes
@app.route('/')
def home():
    return 'Batata'

@app.route('/sentiment/<word>')
@basic_auth.required
def sentiment(word):
    tb = TextBlob(word)
    return f'Polatiry: {tb.sentiment.polarity}'

@app.route('/price_predict/', methods=['POST'])
@basic_auth.required
def price_predict():
    data = request.get_json()
    data_input = [data[col] for col in df.drop('price', axis=1).columns]
    price = reg_lin.predict([data_input])
    return jsonify(price = price[0])

# run app
app.run(debug=True)
