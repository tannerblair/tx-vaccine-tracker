from unittest import TestCase

from tests.mockclasses import MockDatasource, MockUpdater, starting_data
from updateformatter import updater_to_prettytable, SiteTypes

empty_table = "+------+-----+----------+------------------------+-----------------+---------+--------------+\n" \
              "| Name | Url | Distance | Open Appointment Slots | Open Time Slots | Address | Open In Maps |\n" \
              "+------+-----+----------+------------------------+-----------------+---------+--------------+\n" \
              "+------+-----+----------+------------------------+-----------------+---------+--------------+"

all_table = "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+\n" \
            "|       Name       |      Url      | Distance | Open Appointment Slots | Open Time Slots |                                     Address                                     |                       Open In Maps                       |\n" \
            "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+\n" \
            "|  Item One H-E-B  | www.item1.com |    10    |           0            |        0        |    Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1    | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z |\n" \
            "|  Item Two H-E-B  | www.item2.com |    19    |           0            |        0        |    Item Two H-E-B | 222 Fake Street, Twoson, TX 00002 | (0.2, 0.2) | store #2   | https://www.google.com/maps/search/0.2,+0.2/@0.2,0.2,17z |\n" \
            "| Item Three H-E-B | www.item3.com |    29    |           0            |        0        |   Item Three H-E-B | 333 Fake Street, Threed, TX 00003 | (0.3, 0.3) | store #3  | https://www.google.com/maps/search/0.3,+0.3/@0.3,0.3,17z |\n" \
            "| Item Four H-E-B  | www.item4.com |    39    |           0            |        0        | Item Four H-E-B | 444 Fake Street, Foursquare, TX 00004 | (0.4, 0.4) | store #4 | https://www.google.com/maps/search/0.4,+0.4/@0.4,0.4,17z |\n" \
            "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+"

onett_table = "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+\n" \
              "|      Name      |      Url      | Distance | Open Appointment Slots | Open Time Slots |                                  Address                                  |                       Open In Maps                       |\n" \
              "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+\n" \
              "| Item One H-E-B | www.item1.com |    10    |           0            |        0        | Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1 | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z |\n" \
              "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+"


class Test(TestCase):
    def test_updater_to_prettytable(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        datasource.data = starting_data
        # empty on create
        self.assertEqual(empty_table, str(updater_to_prettytable(updater, SiteTypes.NEW)))
        self.assertEqual(empty_table, str(updater_to_prettytable(updater, SiteTypes.ALL)))
        self.assertEqual(empty_table, str(updater_to_prettytable(updater, SiteTypes.MATCHING)))
        updater.update()

        updater.max_distance = 10
        updater.min_timeslots = 0
        updater.update()

        self.assertEqual(onett_table, str(updater_to_prettytable(updater, SiteTypes.NEW)))
        self.assertEqual(all_table, str(updater_to_prettytable(updater, SiteTypes.ALL)))
        self.assertEqual(onett_table, str(updater_to_prettytable(updater, SiteTypes.MATCHING)))
