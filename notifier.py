"""
Notifiers are used to perform and action when new matches are found.
"""

import winsound
from abc import ABC, abstractmethod

from updater import Updater
from updateformatter import SiteTypes, updater_to_prettytable


class Notifier(ABC):
    @abstractmethod
    def notify(self) -> None:
        """
        Trigger notification action
        """
        pass


class WinBeeper(Notifier):
    """
    WinBeeper generates a tone when notify is called
    """
    def __init__(self, frequency, duration):
        """
        Initialize a new WinBeeper instance
        :param frequency: the frequency of the tone to generate
        :param duration: the duration to play the tone for
        """
        self.frequency = frequency
        self.duration = duration

    def notify(self):
        winsound.Beep(200, 400)


class ConsolePrinter(Notifier):
    """
    ConsolePrinter prints a table of vaccine information to the console.
    """
    def __init__(self, updater: Updater, sitetypes: SiteTypes):
        """
        Initialize a new ConsolePrinter instance
        :param updater: the updater to use for vaccine data updates
        :param sitetypes: the types of sites to add to the table
        """
        self.updater = updater
        self.site_types = sitetypes

    def notify(self):
        table = updater_to_prettytable(self.updater, self.site_types)
        print(table)
