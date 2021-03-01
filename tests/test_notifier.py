from unittest import TestCase

from vaccinetracker.notifier import WinBeeper, ConsolePrinter, LinkOpener
from tests.mockclasses import MockUpdater, MockDatasource, onett


class TestWinBeeper(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        datasource.data = [onett]
        updater = MockUpdater(datasource)
        updater.update()
        notifier = WinBeeper(200, 400)
        notifier.notify(list(updater.all.values()))


class TestConsolePrinter(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        datasource.data = [onett]
        updater = MockUpdater(datasource)
        updater.update()
        notifier = ConsolePrinter(updater.home_coords)
        notifier.notify(list(updater.all.values()))


class TestLinkOpener(TestCase):
    def test_notify(self):
        datasource = MockDatasource()
        datasource.data = [onett]
        updater = MockUpdater(datasource)
        updater.update()
        notifier = LinkOpener()
        notifier.notify(list(updater.all.values()))
