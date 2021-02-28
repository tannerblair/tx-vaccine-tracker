from unittest import TestCase

from notifier import WinBeeper, ConsolePrinter, LinkOpener
from tests.mockclasses import MockUpdater, MockDatasource, onett
from updateformatter import SiteType


class TestWinBeeper(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        datasource.data = [onett]
        updater = MockUpdater(datasource)
        updater.update()
        notifier = WinBeeper(200, 400)
        notifier.notify(updater, SiteType.ALL)


class TestConsolePrinter(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        datasource.data = [onett]
        updater = MockUpdater(datasource)
        updater.update()
        notifier = ConsolePrinter()
        notifier.notify(updater, SiteType.ALL)


class TestLinkOpener(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        updater = MockUpdater(datasource)
        updater.min_timeslots = 0
        datasource.data = [onett]
        updater.update()
        notifier = LinkOpener()
        notifier.notify(updater, SiteType.ALL)
