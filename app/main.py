from fastapi import FastAPI

app = FastAPI(
    title="Workout Progress Intelligence API",
    description="Backend service for logging workouts and analyzing strength progress.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}