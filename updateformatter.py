from enum import Enum

from prettytable import prettytable

from updater import Updater
from geotools import coords_url, distance


class SiteTypes(Enum):
    """
    The choices for what kinds of sites to display to the user
    """
    ALL = 0
    MATCHING = 1
    NEW = 2


def updater_to_prettytable(updater: Updater, site_types: SiteTypes = SiteTypes.NEW)-> prettytable:
    """
    Create a prettytable instance from a given updater
    :param updater: the updater to render
    :param site_types: the types of sites to add to the table
    :return: prettytable containing the data from the updater
    """

    # Create new table
    table = prettytable.PrettyTable(["Name", "Url", "Distance", "Open Appointment Slots",
                                     "Open Time Slots", "Address", "Open In Maps"])

    # Choose with dataset in the updater to render in the table
    sites = {}
    if site_types == SiteTypes.ALL:
        sites = updater.all
    if site_types == SiteTypes.MATCHING:
        sites = updater.matching
    if site_types == SiteTypes.NEW:
        sites = updater.new

    # add a row to the table for each site
    for name, site in sites.items():
        table.add_row([
            name,
            site.signup_url,
            round(distance(site.location.coords, updater.home.coords)),
            site.appt_info.appt_slots,
            site.appt_info.time_slots,
            str(site.location),
            coords_url(site.location.coords)
        ])

    return table
