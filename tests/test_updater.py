from unittest import TestCase

from tests.mockclasses import MockUpdater, MockDatasource, starting_data, onett, twoson, threed, foursquare


class TestUpdater(TestCase):
    def test_update_all(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        self.assertEqual(str({}), str(updater.all))
        datasource.data = starting_data
        updater.update()
        self.assertEqual(str(updater.parse_data(starting_data)), str(updater.all))

    def test_update_matching(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)

        # empty on create
        self.assertEqual(str({}), str(updater.all))

        datasource.data = starting_data

        updated_data = starting_data
        updated_data[0]['openAppointmentSlots'] = 1
        updated_data[0]['openTimeslots'] = 1
        updated_data[1]['openAppointmentSlots'] = 2
        updated_data[1]['openTimeslots'] = 2
        updated_data[2]['openAppointmentSlots'] = 3
        updated_data[2]['openTimeslots'] = 3
        updated_data[3]['openAppointmentSlots'] = 4
        updated_data[3]['openTimeslots'] = 4

        # set max distance to 10, then check that only onett is passed
        updater.max_distance = 10
        updater.min_timeslots = 1
        updater.update()
        self.assertEqual(str(updater.parse_data([onett])), str(updater.matching))

        # set max distance to 20, then check that onett and twoson are passed
        updater.max_distance = 20
        updater.min_timeslots = 1
        updater.update()
        self.assertEqual(str(updater.parse_data([onett, twoson])), str(updater.matching))

        # set max distance to 20, then check that onett, twoson, and threed are passed
        updater.max_distance = 30
        updater.min_timeslots = 1
        updater.update()
        self.assertEqual(str(updater.parse_data([onett, twoson, threed])), str(updater.matching))

        # set max distance to 20, then check that onett, twoson, threed, and foursquare are passed
        updater.max_distance = 40
        updater.min_timeslots = 1
        updater.update()
        self.assertEqual(str(updater.parse_data([onett, twoson, threed, foursquare])), str(updater.matching))

        updater.max_distance = 40
        updater.min_timeslots = 2
        updater.update()
        self.assertEqual(str(updater.parse_data([twoson, threed, foursquare])), str(updater.matching))

        updater.max_distance = 40
        updater.min_timeslots = 3
        updater.update()
        self.assertEqual(str(updater.parse_data([threed, foursquare])), str(updater.matching))

        updater.max_distance = 40
        updater.min_timeslots = 4
        updater.update()
        self.assertEqual(str(updater.parse_data([foursquare])), str(updater.matching))

        updater.max_distance = 40
        updater.min_timeslots = 5
        updater.update()
        self.assertEqual(str({}), str(updater.matching))

    def test_update(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        datasource.data = starting_data
        # empty on create
        self.assertEqual(str({}), str(updater.all))
        updater.update()
        self.assertEqual(str(updater.parse_data(starting_data)), str(updater.all))
