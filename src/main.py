from fastapi import FastAPI
from src.models.database import Base, engine
from src.routes import auth, forecast

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Air Quality Forecast Backend")

@app.get("/")
async def root():
    return {"message": "Backend is running!"}

app.include_router(auth.router)
app.include_router(forecast.router)

