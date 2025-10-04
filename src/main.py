from fastapi import FastAPI

app = FastAPI(title="Air Quality Forecast Backend")

@app.get("/")
async def root():
    return {"message": "Backend is running!"}
