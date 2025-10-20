#!/bin/zsh
# Script to install all requirements and launch the main script

python3 -m pip install --upgrade pip

# Install Python dependencies
pip3 install -r requirements.txt

# Add the project root to PYTHONPATH and launch the main script
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python3 ./src/main.py
