"""
The classes in this file are container classes for storing parsed data.
"""
from typing import Tuple


class Address:
    def __init__(self, street: str, city: str, state: str, zipcode: str or int):
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.zipcode: str = str(zipcode)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"

    def __repr__(self):
        return f"Address({str(self)})"


class ApptInfo:
    def __init__(self, appt_slots: int, time_slots: int):
        self.appt_slots: int = appt_slots
        self.time_slots: int = time_slots

    def __str__(self) -> str:
        return f"open appointments: {self.appt_slots}, open timeslots: {self.time_slots}"

    def __repr__(self) -> str:
        return f"ApptInfo({str(self)})"


class Location:
    def __init__(self, name: str, address: Address, coords: Tuple[float, float]):
        self.name = name
        self.address = address
        self.coords = coords

    def __str__(self) -> str:
        return f"{self.name} | {self.address} | {self.coords}"

    def __repr__(self) -> str:
        return f"Location({str(self)})"


class HebLocation(Location):
    def __init__(self, name: str, address: Address, coords: Tuple[float, float], heb_type: str, store_number: str or int):
        super().__init__(name, address, coords)
        self.heb_type = heb_type
        self.store_number: str = str(store_number)

    def __str__(self):
        return super().__str__() + f" | {self.heb_type} #{self.store_number}"

    def __repr__(self):
        return f"HebLocation({str(self)})"


class VaccinationSite:
    def __init__(self, location: Location, appt_info: ApptInfo, signup_url: str):
        self.location: Location = location
        self.appt_info: ApptInfo = appt_info
        self.signup_url: str = signup_url

    def __str__(self):
        return f"{self.location} | {self.appt_info} | {self.signup_url}"

    def __repr__(self):
        return f"VaccinationSite({str(self)})"
