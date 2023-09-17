#!/usr/bin/env python

import os
import sys
import json
import widgets
import subprocess
from pathlib import Path

# Il doit nécessairement y avoir un département en argument
if len(sys.argv) > 1:
    cle = sys.argv[1]
else:
    cle = widgets.obtenirCodeDepartement()
    if cle == '':
        exit()

# On enlève les 0 à gauche, c'est comme ça que sont les identifiants dans notre dictionnaire
cle = cle.lstrip('0')

path = Path(os.path.dirname(__file__)) / '../'
with open(path / 'res/departements.json', encoding='utf8') as file:
    departements = json.load(file)

if not cle in departements:
    widgets.montrerToast("Département invalide !")
    exit()

# Pour l'affichage on met un zéro à gauche si le département n'a qu'un seul chiffre
numero = cle
if len(numero) == 1:
    numero = '0' + numero

# On extrait toutes les informations et on crée un message de réponse qu'on affiche
dep = departements[cle]
nom = dep['nom']

titre = f"{nom} ({numero}) :"
texte = f"""\
- Préfecture : {dep['prefecture']}
"""
if 'region' in dep:
    texte += f"- Ancienne région : {dep['region']}\n"
if 'region2016' in dep:
    texte += f"- Nouvelle région : {dep['region2016']}"
if 'trivia' in dep:
    texte += '\n\n'
    texte += f"Trivia : {dep['trivia']}"

reponse = widgets.showInfoAndGetValue(titre, texte)

# Si la réponse est positive, on ouvre la fenêtre d'édition du trivia
if (reponse):
    subprocess.run(["python", f"{path / 'src/trivia.py'}", cle])