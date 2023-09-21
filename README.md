# Quiz des Départements

Ce projet permet à un téléphone Android sur lequel [Termux](https://termux.dev/en/) est installé de proposer des *flashcards* sur les départements français afin d'aider à la mémorisation des numéros et des préfectures.

<p align="center">
  <img src="https://raw.githubusercontent.com/gabuz0me/images/main/quiz-departements-termux/question_nom.png" alt="Question avec nom" width="150"/>
  <img src="https://raw.githubusercontent.com/gabuz0me/images/main/quiz-departements-termux/question_num.png" alt="Question avec numéro" width="150"/>
  <img src="https://raw.githubusercontent.com/gabuz0me/images/main/quiz-departements-termux/reponse.png" alt="Affichage de la réponse" width="150"/>
  <img src="https://raw.githubusercontent.com/gabuz0me/images/main/quiz-departements-termux/trivia.png" alt="Écriture d'un trivia" width="150"/>
  <img src="https://raw.githubusercontent.com/gabuz0me/images/main/quiz-departements-termux/recherche.png" alt="Recherche d'un département" width="150"/>
</p>

---

## Installation

#### Prérequis

- Avoir un téléphone Android 🤓,
- Avoir installé [Termux](https://github.com/termux/termux-app#installation),
- Avoir installé [Termux:API](https://wiki.termux.com/wiki/Termux:API),
- Avoir installé [Termux:Widget](https://github.com/termux/termux-widget#Installation), c'est optionnel mais c'est plus pratique 😎.

#### Installation

- Cloner ce repo (ou le télécharger et le mettre) sur votre téléphone, à un endroit accessible par Termux.
- Ouvir un terminal termux et lancer `install.sh` :
  - Cela va d'abord générer un fichier `departements.json` dans le dossier `res/`,
  - Cela va ensuite créer deux scripts bash dans le répertoire `.shortcuts/` de l'utilisateurice courant⋅e, `Departement_Quiz` et `Departement_Voir`.
- Et voilà !

#### Désinstallation

- Lancer `uninstall.sh`, qui supprimera les raccourcis créés dans `~/.shortcuts/`.

## Utilisation

Que ce soit via la ligne de commande termux ou via le raccourci accessible via Termux:Widget, l'application permet deux choses :

1. Consulter un département. Pour ce faire il suffit de lancer `Departement_Voir`, de rentrer le code du département et de s'instruire. Il est possible d'éditer un trivia [^1] si l'on répond positivement à la fenêtre qui s'ouvre.
2. Jouer au quiz ! Il suffit de lancer `Departement_Quiz` et si tout marche bien (🤞), une notification s'ouvre demandant soit de trouver le nom soit le numéro d'un département. Une fois la notification cliquée ou balayée, la fenêtre affichant les informations concernant le département s'ouvre, et comme pour la consultation, il est posible d'éditer un trivia.

[^1]: Un trivia est ici une anecdote, un moyen mnémotechnique ou n'importe quel court texte qui peut aider à associer une ville à un département à un numéro.[^2]
[^2]:Par exemple, pour le Cher (18), on peut penser à la ville de Cherbourg[^3], on a donc Cher-Bourg, qui nous aide à nous souvenir de Bourges, la préfecture du Cher, donc. Voilà chacun⋅e ses méthodes hein !
[^3]: Qui n'a rien n'avoir avec le Cher, hein, c'est la Manche !

