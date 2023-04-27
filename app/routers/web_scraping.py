from fastapi import APIRouter, HTTPException, status

from app.repository import web_scraping
from app.utils import convert_to_float, validate_date

router = APIRouter(prefix="/web_scraping", tags=["web_scraping"])


@router.get("/sii", status_code=status.HTTP_200_OK)
def get_data_sii_filter(
    date: str,
):
    try:
        date = validate_date(date)
        value = web_scraping.get_data_sii(date.date())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"value": value, "value_format": convert_to_float(value)}
