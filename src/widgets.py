import json
import subprocess

def montrerToast(text):
    """Affiche un popup temporaire à l'écran"""

    subprocess.run([
        "termux-toast",
        "-g", "middle",
        f"{text}",
    ])

def obtenirCodeDepartement() -> str:
    """Affiche un widget de sélection de numéro
    pour obtenir le code d'un département
    """

    data = subprocess.check_output([
        "termux-dialog", "text",
        '-t', "Numéro du département",
        '-i', "201 pour 2A et 202 pour 2B",
        '-n',
    ])
    data = json.loads(data)
    code = data.get('code')
    texte = data.get('text')
    if code != -1:
        return ""
    
    if texte == "201":
        texte = "2A"
    elif texte == "202":
        texte = "2B"
    
    return texte

def showInfoAndGetValue(titre:str, texte:str) -> bool:
    """Affiche un texte et un titre et récupère un booléen
    selon que l'utilisateurice appuie sur oui ou non
    """
    
    data = subprocess.check_output([
        "termux-dialog", "confirm",
        '-t', titre,
        '-i', texte
    ])
    data = json.loads(data)
    code = data.get('code')
    text = data.get('text')
    return code == 0 and text == 'yes'

def getTextValue(titre:str, hint:str) -> str:
    """Affiche un widget qui permet de récupérer un texte entré
    par l'utilisateurice et un booléen validant l'entrée ou non
    """
    data = subprocess.check_output([
        "termux-dialog", "text",
        '-t', titre,
        '-i', hint,
        '-m',
    ])
    data = json.loads(data)
    code = data.get('code')
    text = data.get('text')
    return code == -1, text