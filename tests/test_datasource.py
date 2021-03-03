from unittest import TestCase

from vaccinetracker.datasource import UrlDatasource


class TestDatasource(TestCase):
    def test_fetch(self):
        datasource = UrlDatasource("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json")
        data = datasource.fetch()
        self.assertNotEqual(0, len(data))
