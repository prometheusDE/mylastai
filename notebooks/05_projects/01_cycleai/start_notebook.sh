#!/bin/bash

# Generate a virtual environment with notebooks name
python3.7 -m venv $1
# Activate environment
source $1/bin/activate
# Install iPython
pip3 install --upgrade pip
pip3 install wheel
pip3 install ipykernel
pip3 install jupyter
# create kernel
ipython kernel install --user --name=$1
# start jupyter notebook - you have to choose kernel by hand so far!
jupyter notebook

