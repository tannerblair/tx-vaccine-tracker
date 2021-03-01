from typing import List

from prettytable import prettytable

from .location import VaccinationSite, Coords
from .geotools import coords_url, distance


def to_horizontal_table(sites: List[VaccinationSite], home_coords: Coords) -> prettytable:
    """
    Create a prettytable of VaccinationSites
    :param sites: the list of sites to add to the table
    :param home_coords: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable(["Name", "Url", "Distance", "Open Appointment Slots",
                                     "Open Time Slots", "Address", "Open In Maps"])

    # add a row to the table for each site
    for site in sites:
        table.add_row(convert_site(site, home_coords))

    return table


def to_vertical_table(sites: List[VaccinationSite], home_coords: Coords) -> prettytable:
    """
    Create a prettytable of VaccinationSites
    :param sites: the list of sites to add to the table
    :param home_coords: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable()

    table.add_column("Store", ["Url", "Distance", "Open Appointment Slots",
                               "Open Time Slots", "Address", "Open In Maps"])
    # add a row to the table for each site
    for site in sites:
        entry = convert_site(site, home_coords)
        table.add_column(entry[0], entry[1:], 'l')

    return table


def convert_site(site: VaccinationSite, home_coords: Coords):
    return [
        site.location.name,
        site.signup_url,
        round(distance(site.location.coords, home_coords)),
        site.appt_info.appt_slots,
        site.appt_info.time_slots,
        str(site.location.address),
        coords_url(site.location.coords)
    ]


def to_address_table(sites: List[VaccinationSite], home_coords: Coords) -> prettytable:
    """
    Create a prettytable of VaccinationSites with only location information
    :param sites: the list of sites to add to the table
    :param home_coords: the coordinates of the home location to calculate distances
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable(["Name", "Address", "Distance", "Open in Maps"])

    entries = []
    for site in sites:
        entries.append([site.location.name, site.location.address,
                       round(distance(site.location.coords, home_coords)), coords_url(site.location.coords)])
        entries.sort(key=lambda x: x[2])

    table.add_rows(entries)

    return table
