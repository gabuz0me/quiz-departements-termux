#!/usr/bin/env bash

echo -n "Désinstallation des raccourcis... "
shortcuts_dir=$HOME/.shortcuts/
mkdir -p $shortcuts_dir
cd $shortcuts_dir
rm -f Quiz_Departement
echo "Fait !"