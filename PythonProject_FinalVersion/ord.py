import random
import json
def SkapaOrd():

    words = ["apa","hund","katt","häst","hammare","sol","snö","gaffel","dörr","ägg","hamster","elefant","snickare","orm","lampa","mus","tangentbord","tallrik", "dator",
    "disktrasa","hörlurar","arm","ben","människa", "bulle", "pizza","öl","kebbab", "skidor", "tomte","socker","bänkpress","gym","klippa","stereo","maskin", "spis","element","stol","bord","vatten","kran",
    "regn","vatten","zoo","polis","brandman","stege","fläkt","flygplan","rumpa","bowling","bajs","bil","lastbil","plånbok","jorden","bläckfisk","ledsen","arg","finland",
    "japan","usa","choklad","spruta","prutt","glass","båt","kyckling","höna","tupp","gris","mohawk","skägg","gitarr","giraffe","zebra","konduktör", "snus", "handuk"]
    rita_word = (random.choice(words))

    with open('Ritat_ord.json', 'w', encoding='utf-8') as fpoint:
        json.dump(rita_word, fpoint, ensure_ascii=False)
SkapaOrd()