from unittest import TestCase


from location import Coords
from maptools import coords_url


class TestMapTools(TestCase):
    def test_coords_url(self):
        coords = Coords(30.274915353356107, -97.74033977282033)
        self.assertEqual(coords_url(coords),"https://www.google.com/maps/search/30.274915353356107,+-97.74033977282033/"
                                            "@30.274915353356107,-97.74033977282033,17z")
