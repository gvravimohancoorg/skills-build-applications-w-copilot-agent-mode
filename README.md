# OctoFit Tracker App - Skeleton

This branch contains a minimal skeleton for the OctoFit Tracker App and a small setup script to create a Python virtual environment and install requirements.

Project structure

- app/
  - __init__.py
  - main.py
  - models.py
- scripts/
  - setup_venv.sh
- requirements.txt
- .gitignore
- README.md

Quick local setup (Unix/macOS)

1. Fetch and switch to the branch:
   git fetch origin
   git checkout build-octofit-app

2. Create a Python virtual environment and install requirements (run from repository root):
   bash scripts/setup_venv.sh

Alternative manual commands:
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt

Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt

What's included

- Minimal Flask app factory and a single route returning a small JSON payload.
- SQLAlchemy base and a default sqlite engine pointing at instance/octofit.db.
- requirements.txt with pinned dependencies to get started.
- setup_venv.sh script to automate venv creation and pip install.

If you want, I can also open a pull request from build-octofit-app into your default branch, add CI, or expand the app with auth, endpoints, and tests. Tell me which next step you want.