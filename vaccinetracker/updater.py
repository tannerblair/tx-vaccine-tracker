from typing import Dict, Tuple

from geopy.distance import distance

from .datasource import UrlDatasource
from .site import Site, SlotDetail


class Updater:
    def __init__(self, origin: Tuple[float, float], max_dist: int, min_qty: int):
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

        self.all: Dict[str, Site] = {}
        self.matching: Dict[str, Site] = {}
        self.in_range: Dict[str, Site] = {}
        self.new: Dict[str, Site] = {}

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
            if site.name in self.in_range:
                if site.open_timeslots >= self.min_qty:
                    locations[name] = site
        self.matching = locations

    def _update_in_range(self):
        """
        Private method for finding H-E-B locations that have doses available and within a reasonable distance from
        self.home.
        """
        locations = {}
        for name, site in self.all.items():
            if distance(site.coords, self.origin).miles <= self.max_dist:
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
            elif old_locations[key].open_timeslots > self.matching[key].open_timeslots:
                new_items[key] = value

        self.new = new_items

    @staticmethod
    def parse_data(data) -> Dict[str, Site]:
        """
        Parse the data fetched from the datasource into a Dictionary of VaccinationSites
        :param data:
        :return:
        """
        locations = {}
        for loc in data:
            site = Site(
                name=loc['name'],
                store_number=loc['storeNumber'],
                loc_type=loc['type'],
                street=loc['street'],
                city=loc['city'],
                state=loc['state'],
                zip_code=loc['zip'],
                latitude=loc['latitude'],
                longitude=loc['longitude'],
                open_timeslots=loc['openTimeslots'],
                open_appointment_slots=loc['openAppointmentSlots'],
                url=loc['url'],
                slot_details=[
                    SlotDetail(
                        manufacturer=slot['manufacturer'],
                        open_timeslots=slot['openTimeslots'],
                        open_appointment_slots=slot['openAppointmentSlots'])
                    for slot in loc['slotDetails']]
            )
            locations[site.name] = site
        return locations
