from datetime import date

from bs4 import BeautifulSoup

from app.utils import fetch_data_get, get_value_day, month_spanish


def get_data_sii(day: date):
    """
    Obtiene los datos de la página web del SII.
    """
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{day.year}.htm"
    response = fetch_data_get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    month = month_spanish(day.strftime("%B"))
    filter_month = soup.find("div", {"id": f"mes_{month}"})
    if not filter_month:
        raise ValueError("No se encontró el mes ingresado.")
    value = get_value_day(filter_month, day.day)
    return value
