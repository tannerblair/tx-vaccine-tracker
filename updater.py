import json
import urllib.request
from typing import Dict

from location import *
from maptools import distance


class Updater:
    def __init__(self,
                 home: Location = Location("Texas Capitol",
                                           Address("1100 Congress Ave", "Austin", "TX", 78701),
                                           Coords(30.274859759662434, -97.74032904386978)),
                 min_timeslots: int = 1,
                 max_distance: int = 50
                 ):

        self._url = "https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json"
        self.home: Location = home
        self.max_distance: int = max_distance
        self.min_timeslots: int = min_timeslots

        self.all: Dict[str, VaccinationSite] = {}
        self.matching: Dict[str, VaccinationSite] = {}
        self.new: Dict[str, VaccinationSite] = {}
        self.update()

    def _update_all(self):
        with urllib.request.urlopen(self._url) as url:
            data = json.loads(url.read().decode())
        data = data["locations"]
        locations = {}
        for loc in data:
            address = Address(loc['street'], loc['city'], loc['state'], loc['zip'])
            coords = Coords(loc['latitude'], loc['longitude'])
            location = HebLocation(loc['name'], address, coords, loc['type'], loc['storeNumber'])
            appt_info = ApptInfo(loc['openAppointmentSlots'], loc['openTimeslots'])
            signup_url = loc["url"]
            site = VaccinationSite(location, appt_info, signup_url)
            locations[site.location.name] = site
        self.all = locations

    def _update_matching(self):
        locations = {}
        for name, site in self.all.items():
            if site.appt_info.time_slots >= self.min_timeslots and \
                    distance(site.location, self.home) <= self.max_distance:
                locations[name] = site
        self.matching = locations

    def update(self):
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
