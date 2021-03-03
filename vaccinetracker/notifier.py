"""
Notifiers are used to perform and action when new matches are found.
"""
import webbrowser
import winsound
from abc import ABC, abstractmethod
from typing import List

from .location import VaccinationSite, Coords
from .updateformatter import to_vertical_table


class Notifier(ABC):
    @abstractmethod
    def notify(self, site_list: List[VaccinationSite]) -> None:
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

    def notify(self, site_list: List[VaccinationSite]) -> None:
        winsound.Beep(200, 400)


class ConsolePrinter(Notifier):
    """
    ConsolePrinter prints a table of vaccine information to the console.
    """
    def __init__(self, home_coords: Coords):
        self.home_coords = home_coords

    def notify(self, site_list: List[VaccinationSite]) -> None:
        table = to_vertical_table(site_list, self.home_coords)
        print(table)


class LinkOpener(Notifier):
    def __init__(self, tab_count: int = 1):
        self.tab_count = tab_count

    def notify(self, site_list: List[VaccinationSite]) -> None:
        for site in site_list:
            for idx in range(self.tab_count):
                webbrowser.open(site.signup_url)

