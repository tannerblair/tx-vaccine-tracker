from unittest import TestCase

from location import Coords, Location, Address
from maptools import coords_url, distance


class TestMapTools(TestCase):
    def test_coords_url(self):
        coords = Coords(30.274915353356107, -97.74033977282033)
        self.assertEqual(coords_url(coords),
                         "https://www.google.com/maps/search/30.274915353356107,+-97.74033977282033/"
                         "@30.274915353356107,-97.74033977282033,17z")

    def test_distance(self):
        location_a = Location("Onett", Address("111 Fake Street", "Austin", "TX", "00001"), Coords(.1, .1))
        location_b = Location("Twoson", Address("222 Fake Street", "Austin", "TX", "00002"), Coords(.2, .2))
        location_c = Location("Threed", Address("333 Fake Street", "Austin", "TX", "00003"), Coords(.3, .3))
        self.assertAlmostEqual(9.75, distance(location_a, location_b), 2)
        self.assertAlmostEqual(9.75, distance(location_b, location_c), 2)
        self.assertAlmostEqual(19.50, distance(location_a, location_c), 2)
