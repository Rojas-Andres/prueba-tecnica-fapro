import datetime

import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException


def convert_to_float(value: str):
    """
    Convierte el valor a float.
    """
    try:
        value = float(value.replace(".", "").replace(",", "."))
    except ValueError:
        raise HTTPException(status_code=500, detail=f"Error al convertir el valor {value} a float.")
    return value


def month_spanish(month: str):
    """
    Convierte el nombre del mes en español.
    """
    months = {
        "January": "enero",
        "February": "febrero",
        "March": "marzo",
        "April": "abril",
        "May": "mayo",
        "June": "junio",
        "July": "julio",
        "August": "agosto",
        "September": "septiembre",
        "October": "octubre",
        "November": "noviembre",
        "December": "diciembre",
    }
    return months.get(month, "Invalid month")


def validate_date(date: str):
    """
    Valida que la fecha ingresada sea válida.
    """
    try:
        date = datetime.datetime.strptime(date, "%d-%m-%Y")
        if date.year < 2013:
            raise ValueError("La fecha ingresada es menor al año 2013.")
    except ValueError as e:
        raise ValueError(str(e))
    return date


def get_value_day(soup: BeautifulSoup, day: int):
    """
    Obtiene el valor de la UF de un día determinado.
    """
    strong_element = soup.find("strong", text=day)
    th_parent = strong_element.find_parent("th")
    real_value = th_parent.find_next_sibling("td")
    return real_value.text


def fetch_data_get(url: str, params: dict = None, headers: dict = None):
    """
    Realiza una solicitud GET a una URL determinada y devuelve la respuesta.

    Args:
        url (str): La URL a la que se debe realizar la solicitud.
        params (dict, optional): Los parámetros que se deben enviar en la solicitud. Defaults to None.
        headers (dict, optional): Los encabezados que se deben enviar en la solicitud. Defaults to None.

    Returns:
        requests.Response: La respuesta obtenida de la URL.
    """
    response = requests.get(url, params=params, headers=headers)
    if not response.ok:
        raise HTTPException(status_code=response.status_code, detail=f"Error {response.status_code}")
    return response
