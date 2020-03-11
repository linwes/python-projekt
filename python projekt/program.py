import json
import random
import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests

app = Flask(__name__)

djur = ["apa","hund","katt","häst","hammare","sol","snö","gaffel","dörr","ägg","hamster","elefant","snickare","orm","lampa","mus","tangentbord","tallrik","spis","element","stol","bord","vatten","kran","handuk","dator","disktrasa","hörlurar","arm","ben","människa",]

ritaDjur = (random.choice(djur))
print(ritaDjur)

@app.route("/")
def start():
    return render_template('index.html')

@app.route('/', methods=['post'])
def skrivUt():
    användare = request.form.get('fNamn','svar')
    
    fNamn = användare
    ritaDjur
    if fNamn == ritaDjur:
        djuret =("du hade rätt!")
        
    else: 
        djuret =("du hade fel försök ingen")

    return render_template('index.html', fNamn=fNamn, djuret=djuret, hej=ritaDjur)

if __name__ :
    app.debug = True
    app.run(host= '127.0.0.1', port=5080)

#@app.route('/rita', methods=['post'])