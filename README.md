# SGBD Learning App

This repository contains a minimal example of a web application for studying
"Sisteme de Gestiune a Bazelor de Date". The application provides a Flask API
that reads definitions from `SGBD CURS DIACONITA COMPLET.pdf` and exposes them
as flashcards. A very small React frontend displays the flashcards.

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m flask --app app run
```

### Frontend

Open `frontend/index.html` in your browser. The page fetches flashcards from
`http://localhost:5000/flashcards`.

### Tests

```bash
pytest
```
