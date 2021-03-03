from unittest import TestCase

from geopy.distance import distance


class TestGeoPy(TestCase):

    def test_distance(self):
        coords_a = (.1, .1)
        coords_b = (.2, .2)
        coords_c = (.3, .3)

        self.assertAlmostEqual(9.75, distance(coords_a, coords_b).miles, 2)
        self.assertAlmostEqual(9.75, distance(coords_b, coords_c).miles, 2)
        self.assertAlmostEqual(19.50, distance(coords_a, coords_c).miles, 2)
