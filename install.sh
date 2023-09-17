#!/usr/bin/env bash

echo -n "Génération des données... "
./src/generator.py
echo "Fait !"

dir=$(pwd)
quiz_name="Departement_Quiz"
show_name="Departement_Voir"

echo -n "Installation des raccourcis... "
shortcuts_dir=$HOME/.shortcuts/
mkdir -p $shortcuts_dir
cd $shortcuts_dir

touch $quiz_name
chmod +x $quiz_name
echo python $dir/src/quiz.py > $quiz_name

touch $show_name
chmod +x $show_name
echo python $dir/src/departement_show.py > $show_name

echo "Fait !"