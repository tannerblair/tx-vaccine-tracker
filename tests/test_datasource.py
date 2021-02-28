from unittest import TestCase

from datasource import Datasource


class TestDatasource(TestCase):
    def test_fetch(self):
        datasource = Datasource("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json")
        data = datasource.fetch()
        self.assertEqual(len(data), 296)
