"""
Tools and utilities for helping with geospatial tasks
"""
from typing import Tuple

from geopy.distance import geodesic


def coords_url(coords: Tuple[float, float]) -> str:
    """
    Given a set of Coords, format a url string that will open the coords in Google Maps.
    :param coords: the coordinates of interest
    :return: URL that will open the location in Google Maps when clicked
    """
    return f"https://www.google.com/maps/search/{coords[0]},+{coords[1]}/@{coords[0]},{coords[1]},17z"


def distance(coords_a: Tuple[float, float], coords_b: Tuple[float, float]) -> int:
    """
    Find the distance in miles between two coordinates
    :param coords_a: the first set of Coords
    :param coords_b: the second set of Coords
    :return: The distance in miles between coords_a and coords_b
    """
    return geodesic((coords_a[0], coords_a[1]), (coords_b[0], coords_b[1])).miles
