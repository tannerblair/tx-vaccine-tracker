from geopy.distance import geodesic

from location import Coords, Location


def coords_url(coords: Coords):
    return f"https://www.google.com/maps/search/{coords.lat},+{coords.lon}/@{coords.lat},{coords.lon},17z"


def distance(location_a: Location, location_b: Location) -> int:
    return geodesic((location_a.coords.lat, location_a.coords.lon),
                    (location_b.coords.lat, location_b.coords.lon)).miles