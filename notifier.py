import winsound
from abc import ABC, abstractmethod

from updater import Updater
from updateformatter import SiteTypes, updater_to_table_str


class Notifier(ABC):
    @abstractmethod
    def notify(self):
        pass


class WinBeeper(Notifier):
    def __init__(self, frequency, duration):
        self.frequency = frequency
        self.duration = duration

    def notify(self):
        winsound.Beep(200, 400)


class ConsolePrinter(Notifier):
    def __init__(self, updater: Updater):
        self.updater = updater

    def notify(self):
        table = updater_to_table_str(self.updater, SiteTypes.ALL)
        print(table)
