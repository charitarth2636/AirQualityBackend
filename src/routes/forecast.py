from fastapi import APIRouter, HTTPException, Query
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/")
async def get_forecast(lat: float = Query(..., description="Latitude"), lon: float = Query(..., description="Longitude")):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching AQI data: {e}")

    forecast_list = []
    for item in data.get("list", []):
        forecast_list.append({
            "datetime": item["dt"],
            "AQI": item["main"]["aqi"],
            "components": item["components"]
        })

    return {"location": {"lat": lat, "lon": lon}, "forecast": forecast_list}
