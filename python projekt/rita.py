import json
import random
import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests

app = Flask(__name__)

djur = ["apa","hund","katt","häst","hammare","sol","snö","gaffel","dörr","ägg","hamster","elefant","snickare","orm","lampa","mus","tangentbord","tallrik","spis","element","stol","bord","vatten","kran","handuk","dator","disktrasa","hörlurar","arm","ben","människa",]

ritaDjur = (random.choice(djur))
print(ritaDjur)