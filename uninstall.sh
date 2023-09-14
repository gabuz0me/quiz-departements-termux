#!/data/data/com.termux/files/usr/bin/sh

echo -n "Désinstallation des raccourcis... "
shortcuts_dir=$HOME/.shortcuts/
mkdir -p $shortcuts_dir
cd $shortcuts_dir
rm -f Quiz_Departement
echo "Fait !"