import random
import json
def SkapaOrd():

    djur = ["apa","hund","katt","häst","hammare","sol","snö","gaffel","dörr","ägg","hamster","elefant","snickare","orm","lampa","mus","tangentbord","tallrik","spis","element","stol","bord","vatten","kran","handuk","dator","disktrasa","hörlurar","arm","ben","människa",]
    ritaDjur = (random.choice(djur))

    with open('Ritat_ord.json', 'w', encoding='utf-8') as fpoint:
        json.dump(ritaDjur, fpoint, ensure_ascii=False)
SkapaOrd()