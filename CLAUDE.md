# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands
- Run application: `python app.py` (runs on port 5001)
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`

## Architecture & Structure
- **Framework**: Flask web application.
- **Entry Point**: `app.py` contains the application instance and all route definitions.
- **Database**: Database logic is managed in the `database/` directory, specifically `database/db.py`. It is intended to use SQLite.
- **Frontend**:
    - HTML templates are located in `templates/`.
    - Static assets (CSS, JS, images) are located in `static/`.
- **Configuration**: Dependencies are listed in `requirements.txt`.
