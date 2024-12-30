#!/bin/zsh

cd Akeome2025_app
pwd
rm -R build
rm -R Akeome2025.app
rm Akeome2025.pyxapp
rm Akeome2025
rm -R ../misc/Akeome2025.app

cp ../Akeome2025/Akeome2025.pyxapp .

echo "wait 5 sec."
sleep 5

uv run pyxel app2exe Akeome2025.pyxapp

cp -r Akeome2025.app ../misc

cd ..
pwd

echo "done."