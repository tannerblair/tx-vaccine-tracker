from unittest import TestCase

from notifier import WinBeeper, ConsolePrinter
from tests.mockclasses import MockUpdater, MockDatasource
from updateformatter import SiteType


class TestWinBeeper(TestCase):
    def test_notify(self):
        notifier = WinBeeper(200, 400)
        notifier.notify()


class TestConsolePrinter(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        updater.update()
        notifier = ConsolePrinter(updater, SiteType.ALL)
        notifier.notify()
