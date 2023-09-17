#!/usr/bin/env bash

echo -n "Désinstallation des raccourcis... "
shortcuts_dir=$HOME/.shortcuts/
mkdir -p $shortcuts_dir
cd $shortcuts_dir
rm -f Departement_Quiz
rm -f Departement_Voir
echo "Fait !"