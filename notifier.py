import winsound
from abc import ABC, abstractmethod

from updater import Updater
from updateformatter import SiteTypes, updater_to_prettytable


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
    def __init__(self, updater: Updater, sitetypes: SiteTypes):
        self.updater = updater
        self.sitetypes = sitetypes

    def notify(self):
        table = updater_to_prettytable(self.updater, self.sitetypes)
        print(table)
