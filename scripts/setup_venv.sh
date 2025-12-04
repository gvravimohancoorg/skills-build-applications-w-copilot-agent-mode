#!/usr/bin/env bash
set -e

# Create virtual environment
python3 -m venv venv

# Activate (this runs in the current shell when sourced) and install requirements
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Virtual environment created and requirements installed. Activate with: source venv/bin/activate"