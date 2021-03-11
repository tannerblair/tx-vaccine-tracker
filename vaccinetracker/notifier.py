"""
Notifiers are used to perform and action when new matches are found.
"""
import webbrowser
import winsound
from abc import ABC, abstractmethod
from typing import List, Tuple

from .location import VaccinationSite
from .format_helpers import to_vertical_table


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
        winsound.Beep(self.frequency, self.duration)


class ConsolePrinter(Notifier):
    """
    ConsolePrinter prints a table of vaccine information to the console.
    """
    def __init__(self, origin: Tuple[float, float]):
        self.origin = origin

    def notify(self, site_list: List[VaccinationSite]) -> None:
        table = to_vertical_table(site_list, self.origin)
        print(table)


class LinkOpener(Notifier):
    def __init__(self, tab_count: int = 1):
        self.tab_count = tab_count

    def notify(self, site_list: List[VaccinationSite]) -> None:
        for site in site_list:
            for idx in range(self.tab_count):
                webbrowser.open(site.signup_url)

