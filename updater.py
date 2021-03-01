from typing import Dict

from datasource import UrlDatasource
from location import *
from geotools import distance


class Updater:
    def __init__(self, home_coords: Coords, min_timeslots: int, max_distance: int):
        """
        Create a new instance of Updater
        :param home_coords: The location for calculating the distance to each H-E-B
        :param min_timeslots: The minimum number of timeslots to include in the results
        :param max_distance: The maximum distance from self.home that is acceptable
        """
        self.datasource = UrlDatasource("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json")
        self.home_coords: Coords = home_coords
        self.max_distance: int = max_distance
        self.min_timeslots: int = min_timeslots

        self.all: Dict[str, VaccinationSite] = {}
        self.matching: Dict[str, VaccinationSite] = {}
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
            if site.appt_info.time_slots >= self.min_timeslots and \
                    distance(site.location.coords, self.home_coords) <= self.max_distance:
                locations[name] = site
        self.matching = locations

    def update(self):
        """
        Fetch data from datasource and update self.all, self.matching, and self.new
        """
        old_locations = self.matching
        self._update_all()
        self._update_matching()

        new_items = {}
        for key, value in self.matching.items():
            if key not in old_locations:
                new_items[key] = value
            elif old_locations[key].appt_info.time_slots > self.matching[key].appt_info.time_slots:
                new_items[key] = value

        self.new = new_items

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
            coords = Coords(loc['latitude'], loc['longitude'])
            location = HebLocation(loc['name'], address, coords, loc['type'], loc['storeNumber'])
            appt_info = ApptInfo(loc['openAppointmentSlots'], loc['openTimeslots'])
            signup_url = loc["url"]
            site = VaccinationSite(location, appt_info, signup_url)
            locations[site.location.name] = site
        return locations
