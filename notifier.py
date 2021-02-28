import winsound
from abc import ABC, abstractmethod


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
