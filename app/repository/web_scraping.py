from datetime import date

from bs4 import BeautifulSoup

from app.utils import fetch_data_get, get_value_day, month_spanish


def get_data_sii(date: date):
    """
    Obtiene los datos de la página web del SII.
    """
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{date.year}.htm"
    response = fetch_data_get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    month = month_spanish(date.strftime("%B"))
    filter_month = soup.find("div", {"id": f"mes_{month}"})
    value = get_value_day(filter_month, date.day)
    return value
