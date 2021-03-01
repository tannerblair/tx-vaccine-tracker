"""
The Datasource class is used to define the source of vaccination site data.
"""

import json
import urllib.request
from abc import ABC, abstractmethod
from typing import Dict


class Datasource(ABC):
    @abstractmethod
    def fetch(self):
        """
        Get Dictionary of location data from the datasource
        """
        pass


class UrlDatasource:
    def __init__(self, url):
        """
        Create a new instance of Datasource that will fetch data from H-E-B
        :param url: The H-E-B website endpoint for vaccine_locations.json
        """
        self.url = url

    def fetch(self) -> Dict[str, Dict]:
        """
        Fetch data from url
        :return: Location data from H-E-B Vaccination website
        """
        with urllib.request.urlopen(self.url) as url:
            data = json.loads(url.read().decode())
        return data["locations"]
