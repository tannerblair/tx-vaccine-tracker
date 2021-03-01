from unittest import TestCase

from vaccinetracker.location import Address, Coords, ApptInfo, Location, HebLocation, VaccinationSite


class TestAddress(TestCase):
    def test_init(self):
        my_address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        self.assertEqual("1100 Congress Ave", my_address.street)
        self.assertEqual("Austin", my_address.city)
        self.assertEqual("TX", my_address.state)
        self.assertEqual("78701", my_address.zipcode)

    def test_str(self):
        my_address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        self.assertEqual("1100 Congress Ave, Austin, TX 78701", str(my_address))

    def test_repr(self):
        my_address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        self.assertEqual("Address(1100 Congress Ave, Austin, TX 78701)", repr(my_address))


class TestCoords(TestCase):
    def test_init(self):
        my_coords = Coords(30.274859759662434, -97.74032904386978)
        self.assertEqual(my_coords.lat, 30.274859759662434)
        self.assertEqual(my_coords.lon, -97.74032904386978)

    def test_str(self):
        my_coords = Coords(30.274859759662434, -97.74032904386978)
        self.assertEqual("(30.274859759662434, -97.74032904386978)", str(my_coords))

    def test_repr(self):
        my_coords = Coords(30.274859759662434, -97.74032904386978)
        self.assertEqual("Coords((30.274859759662434, -97.74032904386978))", repr(my_coords))


class TestApptInfo(TestCase):
    def test_init(self):
        info = ApptInfo(23, 45)
        self.assertEqual(info.appt_slots, 23)
        self.assertEqual(info.time_slots, 45)

    def test_str(self):
        info = ApptInfo(23, 45)
        self.assertEqual("open appointments: 23, open timeslots: 45", str(info))

    def test_repr(self):
        info = ApptInfo(23, 45)
        self.assertEqual("ApptInfo(open appointments: 23, open timeslots: 45)", repr(info))


class TestLocation(TestCase):
    def test_init(self):
        address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        coords = Coords(30.274859759662434, -97.74032904386978)
        location = Location("Texas Capitol", address, coords)
        self.assertEqual("Texas Capitol", location.name)
        self.assertEqual(address, location.address)
        self.assertEqual(coords, location.coords)

    def test_str(self):
        address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        coords = Coords(30.274859759662434, -97.74032904386978)
        location = Location("Texas Capitol", address, coords)
        self.assertEqual("Texas Capitol | 1100 Congress Ave, Austin, TX 78701 | "
                         "(30.274859759662434, -97.74032904386978)"
                         "",
                         str(location))

    def test_repr(self):
        address = Address("1100 Congress Ave", "Austin", "TX", 78701)
        coords = Coords(30.274859759662434, -97.74032904386978)
        location = Location("Texas Capitol", address, coords)
        self.assertEqual("Location(Texas Capitol | 1100 Congress Ave, Austin, TX 78701 | "
                         "(30.274859759662434, -97.74032904386978))",
                         repr(location))


class TestHebLocation(TestCase):
    def test_init(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        self.assertEqual("Spring Green Market H-E-B", location.name)
        self.assertEqual(address, location.address)
        self.assertEqual(coords, location.coords)
        self.assertEqual("store", location.heb_type)
        self.assertEqual("749", location.store_number)

    def test_str(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        self.assertEqual("Spring Green Market H-E-B | 9211 FM 723 RD, RICHMOND, TX 77406-0 | "
                         "(29.69558, -95.81427) | store #749",
                         str(location))

    def test_repr(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        self.assertEqual("HebLocation(Spring Green Market H-E-B | 9211 FM 723 RD, RICHMOND, TX 77406-0 | "
                         "(29.69558, -95.81427) | store #749)",
                         repr(location))


class TestVaccinationSite(TestCase):
    def test_init(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        info = ApptInfo(23, 45)
        site = VaccinationSite(location, info, "www.google.com")
        self.assertEqual(location, site.location)
        self.assertEqual(info, site.appt_info)
        self.assertEqual("www.google.com", site.signup_url)

    def test_str(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        info = ApptInfo(23, 45)
        site = VaccinationSite(location, info, "www.google.com")
        self.assertEqual("Spring Green Market H-E-B | 9211 FM 723 RD, RICHMOND, TX 77406-0 | (29.69558, -95.81427) | "
                         "store #749 | open appointments: 23, open timeslots: 45 | www.google.com", str(site))

    def test_repr(self):
        address = Address("9211 FM 723 RD", "RICHMOND", "TX", "77406-0")
        coords = Coords(29.69558, -95.81427)
        location = HebLocation("Spring Green Market H-E-B", address, coords, "store", 749)
        info = ApptInfo(23, 45)
        site = VaccinationSite(location, info, "www.google.com")
        self.assertEqual("VaccinationSite(Spring Green Market H-E-B | 9211 FM 723 RD, RICHMOND, TX 77406-0 | "
                         "(29.69558, -95.81427) | store #749 | open appointments: 23, open timeslots: 45 | "
                         "www.google.com)", repr(site))
