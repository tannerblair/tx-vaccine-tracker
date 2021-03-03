from unittest import TestCase

from vaccinetracker.geotools import coords_url, distance


class TestMapTools(TestCase):
    def test_coords_url(self):
        coords = (30.274915353356107, -97.74033977282033)
        self.assertEqual(coords_url(coords),
                         "https://www.google.com/maps/search/30.274915353356107,+-97.74033977282033/"
                         "@30.274915353356107,-97.74033977282033,17z")

    def test_distance(self):
        coords_a = (.1, .1)
        coords_b = (.2, .2)
        coords_c = (.3, .3)

        self.assertAlmostEqual(9.75, distance(coords_a, coords_b), 2)
        self.assertAlmostEqual(9.75, distance(coords_b, coords_c), 2)
        self.assertAlmostEqual(19.50, distance(coords_a, coords_c), 2)
