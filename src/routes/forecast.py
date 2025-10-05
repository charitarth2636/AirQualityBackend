from fastapi import APIRouter

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/")
def get_forecast():
    return {"message": "AQI forecast endpoint placeholder"}
