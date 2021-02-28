"""
Notifiers are used to perform and action when new matches are found.
"""
import webbrowser
import winsound
from abc import ABC, abstractmethod

from updater import Updater
from updateformatter import SiteType, updater_to_table


class Notifier(ABC):
    @abstractmethod
    def notify(self, updater: Updater, site_type: SiteType) -> None:
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

    def notify(self, updater: Updater, site_type: SiteType):
        winsound.Beep(200, 400)


class ConsolePrinter(Notifier):
    """
    ConsolePrinter prints a table of vaccine information to the console.
    """
    def notify(self, updater: Updater, site_type: SiteType):
        table = updater_to_table(updater, site_type)
        print(table)


class LinkOpener(Notifier):
    def notify(self, updater: Updater, site_type: SiteType) -> None:
        for site in list(updater.new.values()):
            webbrowser.open(site.signup_url)

