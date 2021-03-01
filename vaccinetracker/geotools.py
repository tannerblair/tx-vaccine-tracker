"""
Tools and utilities for helping with geospatial tasks
"""

from geopy.distance import geodesic

from .location import Coords, Location


def coords_url(coords: Coords) -> str:
    """
    Given a set of Coords, format a url string that will open the coords in Google Maps.
    :param coords: the coordinates of interest
    :return: URL that will open the location in Google Maps when clicked
    """
    return f"https://www.google.com/maps/search/{coords.lat},+{coords.lon}/@{coords.lat},{coords.lon},17z"


def distance(coords_a: Coords, coords_b: Coords) -> int:
    """
    Find the distance in miles between two coordinates
    :param coords_a: the first set of Coords
    :param coords_b: the second set of Coords
    :return: The distance in miles between coords_a and coords_b
    """
    return geodesic((coords_a.lat, coords_a.lon), (coords_b.lat, coords_b.lon)).miles
