#!/usr/bin/env python

import os
import csv
import json
from pathlib import Path

res_path = Path(os.path.dirname(__file__)) / '../res'

departements = {}

# Prefectures.csv est un copié-collé du tableau de la page
# https://fr.wikipedia.org/wiki/Liste_des_pr%C3%A9fectures_de_France
with open(res_path/"prefectures.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        info = {
            "nom":row['Département'].strip(),
            "prefecture":row['Préfecture'].strip(),
        }
        departements[row['NoInsee'].strip()] = info

# Les fichiers JSON des régions ont été écrits à la main.
with open(res_path/"regions.json", encoding="utf8") as file:
    regions = json.load(file)
    for reg, deps in regions.items():
        for dep in deps:
            departements[str(dep)]['region'] = reg

with open(res_path/"regions2016.json", encoding="utf8") as file:
    regions = json.load(file)
    for reg, deps in regions.items():
        for dep in deps:
            departements[str(dep)]['region2016'] = reg

with open(res_path/"departements.json", encoding="utf8", mode='w') as file:
    json.dump(departements, file, indent=2, ensure_ascii=False)