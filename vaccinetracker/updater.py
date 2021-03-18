from enum import Enum
from typing import Dict, Tuple

from geopy.distance import distance

from .datasource import UrlDatasource
from .location import VaccinationSite, Address, HebLocation, ApptInfo


class VaxType(Enum):
    all = "all"
    moderna = "Moderna"
    pfizer = "Pfizer"
    jandj = "J&J/Janssen"


class Updater:
    def __init__(self, origin: Tuple[float, float], max_dist: int, min_qty: int, vax_type: VaxType):
        """
        Create a new instance of Updater
        :param origin: The location for calculating the distance to each H-E-B
        :param max_dist: The maximum distance from self.home that is acceptable
        :param min_qty: The minimum number of timeslots to include in the results
        """
        self.datasource = UrlDatasource("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json")
        self.origin: Tuple[float, float] = origin
        self.max_dist: int = max_dist
        self.min_qty: int = min_qty
        self.vax_type = vax_type

        self.all: Dict[str, VaccinationSite] = {}
        self.matching: Dict[str, VaccinationSite] = {}
        self.in_range: Dict[str, VaccinationSite] = {}
        self.new: Dict[str, VaccinationSite] = {}

    def _update_all(self):
        """
        Private method for fetching all data from the datasource, parse it, and save it to self.all
        """
        data = self.datasource.fetch()
        self.all = self.parse_data(data)

    def _update_matching(self):
        """
        Private method for finding H-E-B locations that have doses available and within a reasonable distance from
        self.home.
        """
        locations = {}
        for name, site in self.all.items():
            if site.location.name in self.in_range:
                if site.appt_info.time_slots >= self.min_qty:
                    if self.vax_type != VaxType.all:
                        if self.vax_type.value in site.doses.keys():
                            locations[name] = site
                    else:
                        locations[name] = site
        self.matching = locations

    def _update_in_range(self):
        """
        Private method for finding H-E-B locations that have doses available and within a reasonable distance from
        self.home.
        """
        locations = {}
        for name, site in self.all.items():
            if distance(site.location.coords, self.origin).miles <= self.max_dist:
                locations[name] = site
        self.in_range = locations

    def update(self):
        """
        Fetch data from datasource and update self.all, self.matching, and self.new
        """
        old_locations = self.matching
        self._update_all()
        self._update_in_range()
        self._update_matching()

        new_items = {}
        for key, value in self.matching.items():
            if key not in old_locations:
                new_items[key] = value
            elif old_locations[key].appt_info.time_slots > self.matching[key].appt_info.time_slots:
                new_items[key] = value

        self.new = new_items

    @staticmethod
    def parse_slot_info(data) -> Dict[str, Dict]:
        vax_dict = {}
        for vaccine in data:
            vax_dict[vaccine['manufacturer']] = vaccine

        return vax_dict

    @staticmethod
    def parse_data(data) -> Dict[str, VaccinationSite]:
        """
        Parse the data fetched from the datasource into a Dictionary of VaccinationSites
        :param data:
        :return:
        """
        locations = {}
        for loc in data:
            address = Address(loc['street'], loc['city'], loc['state'], loc['zip'])
            coords = (loc['latitude'], loc['longitude'])
            location = HebLocation(loc['name'], address, coords, loc['type'], loc['storeNumber'])
            appt_info = ApptInfo(loc['openAppointmentSlots'], loc['openTimeslots'])
            signup_url = loc["url"]
            doses = Updater.parse_slot_info(loc['slotDetails'])
            site = VaccinationSite(location, appt_info, signup_url, doses)
            locations[site.location.name] = site
        return locations

