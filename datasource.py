import json
import urllib.request


class Datasource:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        with urllib.request.urlopen(self.url) as url:
            data = json.loads(url.read().decode())
        return data["locations"]
