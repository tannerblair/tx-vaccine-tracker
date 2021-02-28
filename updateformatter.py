from enum import Enum

from prettytable import prettytable

from updater import Updater
from maptools import coords_url, distance


class SiteTypes(Enum):
    ALL = 0
    MATCHING = 1
    NEW = 2


def updater_to_table_str(updater: Updater, site_types: SiteTypes = SiteTypes.NEW):

    table = prettytable.PrettyTable(["Name", "Url", "Distance", "Open Appointment Slots",
                                     "Open Time Slots", "Address", "Open In Maps"])
    sites = {}
    if site_types == SiteTypes.ALL:
        sites = updater.all
    if site_types == SiteTypes.MATCHING:
        sites = updater.matching
    if site_types == SiteTypes.NEW:
        sites = updater.new

    for name, site in sites.items():
        table.add_row([
            name,
            site.signup_url,
            round(distance(site.location, updater.home)),
            site.appt_info.appt_slots,
            site.appt_info.time_slots,
            str(site.location),
            coords_url(site.location.coords)
        ])
    return table
