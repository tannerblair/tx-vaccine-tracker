"""
The classes in this file are container classes for storing parsed data.
"""
from typing import List
from collections import namedtuple

Coords = namedtuple('Coords', ['latitude', 'longitude'])


class SlotDetail:
    def __init__(self, manufacturer: str, open_timeslots: int, open_appointment_slots: int):
        self.open_time_slots: int = open_timeslots
        self.open_appointment_slots: int = open_appointment_slots
        self.manufacturer: str = manufacturer


class Site:
    def __init__(
            self,
            name: str,
            store_number: int,
            loc_type: str,
            street: str,
            city: str,
            state: str,
            zip_code: str,
            latitude: int,
            longitude: int,
            open_timeslots: int,
            open_appointment_slots: int,
            url: str,
            slot_details: List[SlotDetail]
    ):
        self.name: str = name
        self.storeNumber: int = store_number
        self.loc_type: str = loc_type
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
        self.latitude: int = latitude
        self.longitude: int = longitude
        self.open_timeslots: int = open_timeslots
        self.open_appointment_slots: int = open_appointment_slots
        self.url: str = url
        self.slot_details: List[SlotDetail] = slot_details

    @property
    def coords(self) -> Coords:
        return Coords(self.latitude, self.longitude)

    @property
    def address(self) -> str:
        return f'{self.street}, {self.city}, {self.state} {self.zip_code})'

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str(vars(self))
