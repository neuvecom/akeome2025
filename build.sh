#!/bin/zsh

cd Akeome2025
pwd
rm index.html
rm Akeome2025.pyxapp

uv run pyxel package . akeome.py 

echo "wait 5 sec."
sleep 5

uv run pyxel app2html Akeome2025.pyxapp

mv Akeome2025.html index.html

cp inindex.html ../docs/

cd ..
pwd

echo "done."