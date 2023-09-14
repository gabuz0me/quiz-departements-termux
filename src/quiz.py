#!/usr/bin/env python

import os
import json
import subprocess
from random import choice, getrandbits
from pathlib import Path

res_path = Path(os.path.dirname(__file__)) / '../res'

# 1. Lecture des données et choix d'un département au hasard
with open(res_path / 'departements.json', encoding='utf8') as file:
    departements = json.load(file)

numero = choice(list(departements.keys()))
dep = departements[numero]

# 2. Formatage du numéro si un seul chiffre, et choix d'une question à poser au hasard (nom ou numéro)
if len(numero) == 1:
    numero = '0'+numero

nom = dep['nom']
if getrandbits(1):
    question = f"Numéro {numero} ?"
else:
    question = f"{nom} ?"

# 3. Création de la réponse sous forme de texte
reponse = f"""\
{nom} ({numero}) :
- Préfecture : {dep['prefecture']}
"""
if 'region' in dep:
    reponse += f"- Ancienne région : {dep['region']}\n"
if 'region2016' in dep:
    reponse += f"- Nouvelle région : {dep['region2016']}"

# 4. Envoi de la notification
action = f"termux-dialog confirm -i '{reponse}'"
subprocess.run([
    "termux-notification",
    "-t", "Quiz Département !!",
    "-c", f"{question}",
    "--action", action,
    "--on-delete", action,
])

exit()