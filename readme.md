# Eval Python B2 — API Stations de vélos

API REST de gestion de stations de vélos construite avec FastAPI, SQLAlchemy et SQLite.

## Prérequis

- Python 3.12
- Git Bash ou terminal compatible

## Installation

### 1. Créer et activer le virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Lancement de l'API

```bash
uvicorn app.main:app --reload
```

- API : http://127.0.0.1:8000  
- Docs interactives : http://127.0.0.1:8000/docs

## Lancer les tests

```bash
python -m pytest -v
```

## Endpoints

| Méthode | Route               | Description                        | Code retour |
|---------|---------------------|------------------------------------|-------------|
| GET     | /health             | Santé de l'API                     | 200         |
| GET     | /stations           | Liste toutes les stations          | 200         |
| GET     | /stations?status=open | Filtre par statut               | 200         |
| GET     | /stations/{id}      | Détail d'une station               | 200 / 404   |
| POST    | /stations           | Créer une station                  | 201 / 409 / 422 |
| PATCH   | /stations/{id}      | Modifier name ou status            | 200 / 404 / 422 |

EXO4 I M P O S S I B L E# eval-rio-killian-pythin-b2
# eval-rio-killian-pythin-b2
# eval-rio-killian-pythin-b2
