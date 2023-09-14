#!/data/data/com.termux/files/usr/bin/sh

echo -n "Génération des données... "
./generator.py
echo "Fait !"

dir=$(pwd)
quiz_name="Quiz_Departement"

echo -n "Installation des raccourcis... "
shortcuts_dir=$HOME/.shortcuts/
mkdir -p $shortcuts_dir
cd $shortcuts_dir

touch $quiz_name
chmod +x $quiz_name

echo $dir/src/quiz.py > $quiz_name
echo "Fait !"