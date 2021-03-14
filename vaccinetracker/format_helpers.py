from typing import List, Tuple

from geopy.distance import distance
from prettytable import prettytable

from .site import Site


def to_horizontal_table(sites: List[Site], origin: Tuple[float, float]) -> prettytable:
    """
    Create a prettytable of VaccinationSites
    :param sites: the list of sites to add to the table
    :param origin: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable(["Name", "Url", "Distance", "Open Appointment Slots",
                                     "Open Time Slots", "Address", "Open In Maps"])

    # add a row to the table for each site
    for site in sites:
        table.add_row(convert_site(site, origin))

    return table


def to_vertical_table(sites: List[Site], origin: Tuple[float, float]) -> prettytable:
    """
    Create a prettytable of VaccinationSites
    :param sites: the list of sites to add to the table
    :param origin: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable()

    table.add_column("Store", ["Url", "Distance", "Open Appointment Slots",
                               "Open Time Slots", "Address", "Open In Maps"])
    # add a row to the table for each site
    for site in sites:
        entry = convert_site(site, origin)
        table.add_column(entry[0], entry[1:], 'l')

    return table


def convert_site(site: Site, origin: Tuple[float, float]):
    return [
        site.location.name,
        site.signup_url,
        round(distance(site.location.coords, origin).miles),
        site.appt_info.appt_slots,
        site.appt_info.time_slots,
        str(site.location.address),
        coords_url(site.location.coords)
    ]


def to_address_table(sites: List[Site], origin: Tuple[float, float]) -> prettytable:
    """
    Create a prettytable of VaccinationSites with only location information
    :param sites: the list of sites to add to the table
    :param origin: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable(["Name", "Address", "Distance", "Open in Maps"])

    entries = []
    for site in sites:
        entries.append([site.name, site.address,
                        round(distance(site.coords, origin).miles), coords_url(site.coords)])
        entries.sort(key=lambda x: x[2])

    table.add_rows(entries)

    return table


def coords_url(coords: Tuple[float, float]) -> str:
    """
    Given a set of Coords, format a url string that will open the coords in Google Maps.
    :param coords: the coordinates of interest
    :return: URL that will open the location in Google Maps when clicked
    """
    return f"https://www.google.com/maps/search/{coords[0]},+{coords[1]}/@{coords[0]},{coords[1]},17z"
