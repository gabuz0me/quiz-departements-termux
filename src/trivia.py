#!/usr/bin/env python

import os
import sys
import json
import widgets
from pathlib import Path

# On récupère la clé du département dont on veut éditer le trivia
if len(sys.argv) > 1:
    cle = sys.argv[1]
else:
    widgets.montrerToast("Appel sans argument")
    exit()

# Lecture des infos concernant ce département
res_path = Path(os.path.dirname(__file__)) / '../res'
with open(res_path / 'departements.json', encoding='utf8', mode='r') as file:
    departements = json.load(file)

if not cle in departements:
    widgets.montrerToast("Département invalide !")
    exit()

departement = departements[cle]
nom = departement['nom']
numero = cle
if len(numero) == 1:
    numero = '0' + numero
hint_trivia = departement.get('trivia', 'Écrivez ici une aide concernant ce département')

# Écriture si trivia donné
code, texte = widgets.getTextValue(f"Trivia sur {nom} ({numero})", hint_trivia)
if code:
    if len(texte) == 0:
        departement.pop('trivia', None)
    else:
        departement['trivia'] = texte
    with open(res_path / 'departements.json', encoding='utf8', mode='w') as file:
        json.dump(departements, file, indent=2)