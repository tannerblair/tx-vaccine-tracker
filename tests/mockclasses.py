from vaccinetracker.datasource import Datasource
from vaccinetracker.updater import Updater


onett = {
                "zip": "00001",
                "url": "www.item1.com",
                "type": "store",
                "street": "111 Fake Street",
                "storeNumber": 1,
                "state": "TX",
                "openTimeslots": 0,
                "openAppointmentSlots": 0,
                "name": "Item One H-E-B",
                "longitude": .1,
                "latitude": .1,
                "city": "Onett"
            }

twoson = {
                "zip": "00002",
                "url": "www.item2.com",
                "type": "store",
                "street": "222 Fake Street",
                "storeNumber": 2,
                "state": "TX",
                "openTimeslots": 0,
                "openAppointmentSlots": 0,
                "name": "Item Two H-E-B",
                "longitude": .2,
                "latitude": .2,
                "city": "Twoson"
            }

threed = {
                "zip": "00003",
                "url": "www.item3.com",
                "type": "store",
                "street": "333 Fake Street",
                "storeNumber": 3,
                "state": "TX",
                "openTimeslots": 0,
                "openAppointmentSlots": 0,
                "name": "Item Three H-E-B",
                "longitude": .3,
                "latitude": .3,
                "city": "Threed"
            }

foursquare = {
                "zip": "00004",
                "url": "www.item4.com",
                "type": "store",
                "street": "444 Fake Street",
                "storeNumber": 4,
                "state": "TX",
                "openTimeslots": 0,
                "openAppointmentSlots": 0,
                "name": "Item Four H-E-B",
                "longitude": .4,
                "latitude": .4,
                "city": "Foursquare"
            }
starting_data =[onett, twoson, threed, foursquare]


class MockDatasource(Datasource):
    def __init__(self):
        super().__init__()
        self.data = []

    def fetch(self):
        return self.data


class MockUpdater(Updater):
    def __init__(self, datasource):
        super().__init__((0, 0), 0, 0)
        self.datasource = datasource
