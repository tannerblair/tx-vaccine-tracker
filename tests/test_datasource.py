from unittest import TestCase

from datasource import UrlDatasource


class TestDatasource(TestCase):
    def test_fetch(self):
        datasource = UrlDatasource("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json")
        data = datasource.fetch()
        self.assertEqual(len(data), 296)
