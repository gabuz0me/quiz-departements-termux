#!/usr/bin/env python

import os
import json
import subprocess
from random import choice, getrandbits
from pathlib import Path

path = Path(os.path.dirname(__file__)) / '../'

# Lecture des données et choix d'un département au hasard
with open(path / 'res/departements.json', encoding='utf8') as file:
    departements = json.load(file)

cle = choice(list(departements.keys()))
departement = departements[cle]

# Formatage du numéro si un seul chiffre, et choix d'une question à poser au hasard (nom ou numéro)
numero = cle
if len(numero) == 1:
    numero = '0'+numero

nom = departement['nom']
if getrandbits(1):
    question = f"Numéro {numero} ?"
else:
    question = f"{nom} ?"

# Envoi de la notification
action = f"python {path / 'src/departement_show.py'} '{cle}'"
subprocess.run([
    "termux-notification",
    "-t", f"Quiz Département !!",
    "-c", f"{question}",
    "--action", action,
    "--on-delete", action,
])