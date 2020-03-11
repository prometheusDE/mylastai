#!/bin/bash

# Generate a virtual environment with notebooks name
python3 -m venv $1
# Activate environment
source $1/bin/activate
# Install iPython
pip install wheel
pip install ipykernel
pip install jupyter
# create kernel
ipython kernel install --user --name=$1
# start jupyter notebook - you have to choose kernel by hand so far!
jupyter notebook

