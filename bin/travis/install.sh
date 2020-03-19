#!/bin/bash
# pwd is the git repo.
set -e

echo "Install latestish pip"
pip install -U pip wheel

echo "Install Python dependencies"
pip install -r requirements.txt

echo "Install latest flake8"
# Perhaps this should be in some dev-requirements.txt but YOLO
pip install flake8

echo "Version of node"
node --version

echo "Version of yarn"
yarn --version

echo "Installing the node packages"
yarn

echo "Install packages for adminui"
pushd adminui
yarn
popd

echo "Install packages for pulse"
pushd pulse
yarn
popd
