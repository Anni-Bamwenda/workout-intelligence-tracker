# Workout Progress Intelligence API

A backend API for logging strength-training workouts and analyzing workout progress over time.

## Purpose

The Workout Progress Intelligence API allows users to record workouts and track metrics such as:

- training volume
- estimated one-rep max
- personal records
- strength progression
- potential training plateaus

The project is being built as a backend-first system using FastAPI and a relational database.

## Planned Features

- Exercise management
- Workout logging
- Set and repetition tracking
- Workout history
- Training volume analytics
- Estimated 1RM calculations
- Personal record detection
- Strength progression analysis
- Plateau detection
- Automated testing
- Logging and observability
- Optional grounded AI-generated progress summaries

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite initially
- Pytest

## Running Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the API
```bash
uvicorn app.main:app --reload
```


