from unittest import TestCase

from tests.mockclasses import MockDatasource, MockUpdater, starting_data
from updateformatter import updater_to_table, SiteType, TableType

empty_table_h = "+------+-----+----------+------------------------+-----------------+---------+--------------+\n" \
                "| Name | Url | Distance | Open Appointment Slots | Open Time Slots | Address | Open In Maps |\n" \
                "+------+-----+----------+------------------------+-----------------+---------+--------------+\n" \
                "+------+-----+----------+------------------------+-----------------+---------+--------------+\n"

all_table_h = "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+\n" \
              "|       Name       |      Url      | Distance | Open Appointment Slots | Open Time Slots |                                     Address                                     |                       Open In Maps                       |\n" \
              "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+\n" \
              "|  Item One H-E-B  | www.item1.com |    10    |           0            |        0        |    Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1    | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z |\n" \
              "|  Item Two H-E-B  | www.item2.com |    19    |           0            |        0        |    Item Two H-E-B | 222 Fake Street, Twoson, TX 00002 | (0.2, 0.2) | store #2   | https://www.google.com/maps/search/0.2,+0.2/@0.2,0.2,17z |\n" \
              "| Item Three H-E-B | www.item3.com |    29    |           0            |        0        |   Item Three H-E-B | 333 Fake Street, Threed, TX 00003 | (0.3, 0.3) | store #3  | https://www.google.com/maps/search/0.3,+0.3/@0.3,0.3,17z |\n" \
              "| Item Four H-E-B  | www.item4.com |    39    |           0            |        0        | Item Four H-E-B | 444 Fake Street, Foursquare, TX 00004 | (0.4, 0.4) | store #4 | https://www.google.com/maps/search/0.4,+0.4/@0.4,0.4,17z |\n" \
              "+------------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------------+----------------------------------------------------------+\n"

onett_table_h = "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+\n" \
                "|      Name      |      Url      | Distance | Open Appointment Slots | Open Time Slots |                                  Address                                  |                       Open In Maps                       |\n" \
                "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+\n" \
                "| Item One H-E-B | www.item1.com |    10    |           0            |        0        | Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1 | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z |\n" \
                "+----------------+---------------+----------+------------------------+-----------------+---------------------------------------------------------------------------+----------------------------------------------------------+\n"

empty_table_v = "+------------------------+\n" \
                "|         Store          |\n" \
                "+------------------------+\n" \
                "|          Url           |\n" \
                "|        Distance        |\n" \
                "| Open Appointment Slots |\n" \
                "|    Open Time Slots     |\n" \
                "|        Address         |\n" \
                "|      Open In Maps      |\n" \
                "+------------------------+\n"

all_table_v = "+------------------------+---------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------+\n" \
              "|         Store          | Item One H-E-B                                                            | Item Two H-E-B                                                             | Item Three H-E-B                                                             | Item Four H-E-B                                                                 |\n" \
              "+------------------------+---------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------+\n" \
              "|          Url           | www.item1.com                                                             | www.item2.com                                                              | www.item3.com                                                                | www.item4.com                                                                   |\n" \
              "|        Distance        | 10                                                                        | 19                                                                         | 29                                                                           | 39                                                                              |\n" \
              "| Open Appointment Slots | 0                                                                         | 0                                                                          | 0                                                                            | 0                                                                               |\n" \
              "|    Open Time Slots     | 0                                                                         | 0                                                                          | 0                                                                            | 0                                                                               |\n" \
              "|        Address         | Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1 | Item Two H-E-B | 222 Fake Street, Twoson, TX 00002 | (0.2, 0.2) | store #2 | Item Three H-E-B | 333 Fake Street, Threed, TX 00003 | (0.3, 0.3) | store #3 | Item Four H-E-B | 444 Fake Street, Foursquare, TX 00004 | (0.4, 0.4) | store #4 |\n" \
              "|      Open In Maps      | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z                  | https://www.google.com/maps/search/0.2,+0.2/@0.2,0.2,17z                   | https://www.google.com/maps/search/0.3,+0.3/@0.3,0.3,17z                     | https://www.google.com/maps/search/0.4,+0.4/@0.4,0.4,17z                        |\n" \
              "+------------------------+---------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------+\n"

onett_table_v = "+------------------------+---------------------------------------------------------------------------+\n" \
                "|         Store          | Item One H-E-B                                                            |\n" \
                "+------------------------+---------------------------------------------------------------------------+\n" \
                "|          Url           | www.item1.com                                                             |\n" \
                "|        Distance        | 10                                                                        |\n" \
                "| Open Appointment Slots | 0                                                                         |\n" \
                "|    Open Time Slots     | 0                                                                         |\n" \
                "|        Address         | Item One H-E-B | 111 Fake Street, Onett, TX 00001 | (0.1, 0.1) | store #1 |\n" \
                "|      Open In Maps      | https://www.google.com/maps/search/0.1,+0.1/@0.1,0.1,17z                  |\n" \
                "+------------------------+---------------------------------------------------------------------------+\n"


class Test(TestCase):
    def test_updater_to_prettytable(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        datasource.data = starting_data

        # empty on create
        self.assertEqual(empty_table_h, str(updater_to_table(updater, SiteType.NEW, TableType.HORIZONTAL))+"\n")
        self.assertEqual(empty_table_h, str(updater_to_table(updater, SiteType.ALL, TableType.HORIZONTAL))+"\n")
        self.assertEqual(empty_table_h, str(updater_to_table(updater, SiteType.MATCHING, TableType.HORIZONTAL))+"\n")
        self.assertEqual(empty_table_v, str(updater_to_table(updater, SiteType.NEW, TableType.VERTICAL))+"\n")
        self.assertEqual(empty_table_v, str(updater_to_table(updater, SiteType.ALL, TableType.VERTICAL))+"\n")
        self.assertEqual(empty_table_v, str(updater_to_table(updater, SiteType.MATCHING, TableType.VERTICAL))+"\n")
        updater.update()

        updater.max_distance = 10
        updater.min_timeslots = 0
        updater.update()

        self.assertEqual(onett_table_h, str(updater_to_table(updater, SiteType.NEW, TableType.HORIZONTAL))+"\n")
        self.assertEqual(all_table_h, str(updater_to_table(updater, SiteType.ALL, TableType.HORIZONTAL))+"\n")
        self.assertEqual(onett_table_h, str(updater_to_table(updater, SiteType.MATCHING, TableType.HORIZONTAL))+"\n")
        self.assertEqual(onett_table_v, str(updater_to_table(updater, SiteType.NEW, TableType.VERTICAL))+"\n")
        self.assertEqual(all_table_v, str(updater_to_table(updater, SiteType.ALL, TableType.VERTICAL))+"\n")
        self.assertEqual(onett_table_v, str(updater_to_table(updater, SiteType.MATCHING, TableType.VERTICAL))+"\n")
