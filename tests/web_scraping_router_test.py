from unittest import TestCase

from fastapi.testclient import TestClient

from main import app


class TestWebScraping(TestCase):
    def setUp(self):
        with TestClient(app) as client:
            self.client = client

    def test_validate_bad_day_1(self):
        response = self.client.get("/web_scraping/sii?date=2021-09-31")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "day is out of range for month")

    def test_validate_bad_day_2(self):
        response = self.client.get("/web_scraping/sii?date=2021-09-40")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "unconverted data remains: 0")

    def test_validate_bad_day_3(self):
        response = self.client.get("/web_scraping/sii?date=asdasdasdadsasd")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "time data 'asdasdasdadsasd' does not match format '%Y-%m-%d'")

    def test_validate_bad_day_4(self):
        response = self.client.get("/web_scraping/sii?date=2012-12-31")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "La fecha ingresada es menor al año 2013.")

    def test_validate_good_day_1(self):
        response = self.client.get("/web_scraping/sii?date=2013-01-01")
        self.assertEqual(response.status_code, 200)

    def test_validate_good_day_2(self):
        """
        Pagina web del SII no tiene datos para el año 2050.
        """
        response = self.client.get("/web_scraping/sii?date=2050-01-01")
        self.assertEqual(response.status_code, 404)

    def test_validate_scraping_2013_01_01(self):
        response = self.client.get("/web_scraping/sii?date=2013-01-01")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "22.837,06")
        self.assertEqual(response.json()["value_format"], 22837.06)

    def test_validate_scraping_2015_07_11(self):
        response = self.client.get("/web_scraping/sii?date=2015-07-11")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "25.005,99")
        self.assertEqual(response.json()["value_format"], 25005.99)

    def test_validate_scraping_2015_07_31(self):
        response = self.client.get("/web_scraping/sii?date=2015-07-31")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "25.086,58")
        self.assertEqual(response.json()["value_format"], 25086.58)

    def test_validate_scraping_2018_01_01(self):
        response = self.client.get("/web_scraping/sii?date=2018-01-01")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "26.799,01")
        self.assertEqual(response.json()["value_format"], 26799.01)

    def test_validate_scraping_2016_12_15(self):
        response = self.client.get("/web_scraping/sii?date=2016-12-15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "26.334,39")
        self.assertEqual(response.json()["value_format"], 26334.39)

    def test_validate_scraping_2016_12_22(self):
        response = self.client.get("/web_scraping/sii?date=2016-12-22")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "26.340,34")
        self.assertEqual(response.json()["value_format"], 26340.34)

    def test_validate_scraping_2014_10_06(self):
        response = self.client.get("/web_scraping/sii?date=2014-10-06")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "24.182,51")
        self.assertEqual(response.json()["value_format"], 24182.51)

    def test_validate_scraping_2014_10_03(self):
        response = self.client.get("/web_scraping/sii?date=2014-10-03")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["value"], "24.175,26")
        self.assertEqual(response.json()["value_format"], 24175.26)
