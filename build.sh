#!/bin/zsh

rm index.html
rm akeome2025.pyxapp

uv run pyxel package . akeome.py 

echo "wait 5 sec."
sleep 5

uv run pyxel app2html akeome2025.pyxapp

mv akeome2025.html index.html

echo "done."