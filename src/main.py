from fastapi import FastAPI
from src.routes import auth, forecast
from src.models.database import init_db

app = FastAPI(title="Air Quality Forecast Backend")

@app.on_event("startup")
async def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "Backend is running!"}

app.include_router(auth.router)
app.include_router(forecast.router)

