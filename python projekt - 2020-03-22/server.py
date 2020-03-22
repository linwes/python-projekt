import json
import random
from flask import Flask, escape, request, jsonify, render_template
import requests

with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
    jord = json.load(ord_file)

word = str(jord)


app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html')

@app.route('/', methods=['post'])
def skrivUt():
    användare = request.form.get('gissa','svar')
    
    gissa = användare.lower()
    if gissa == word:
        gissat = ("du hade rätt!")
        
    else: 
        gissat = ("Fel försök igen!")

    return render_template('index.html', gissa=gissa, gissat=gissat, ord=word)

if __name__ :
    app.debug = True
    app.run(host= '127.0.0.1', port=5080)