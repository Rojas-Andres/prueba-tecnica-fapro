from fastapi import APIRouter, status

router = APIRouter(prefix="/web_scraping", tags=["web_scraping"])


@router.get("/sii", status_code=status.HTTP_200_OK)
def get_data_sii():
    return {"data": []}
