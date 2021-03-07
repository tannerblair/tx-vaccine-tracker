import datetime
import time
import webbrowser
from typing import List, Tuple
from urllib import request

import schedule
from folium import Circle, CircleMarker, Map

from .location import VaccinationSite
from .notifier import Notifier
from .format_helpers import to_address_table
from .updater import Updater


class NoVaccinationSitesInRangeException(Exception):
    def __init__(self, origin: Tuple[float, float], distance: int):
        self.origin = origin
        self.distance = distance

    def __str__(self):
        return f"No vaccination sites at an H-E-B within {self.distance} miles of {self.origin}"

    def __repr__(self):
        return str(self)


class Application:

    def __init__(self, notifiers: List[Notifier], origin: Tuple[float, float],
                 min_qty: int, max_dist: int, rate: int):
        """
        Create a new instance of the AtxVaccineTracker application.
        :param notifiers: a list of Notifier instances that will be called when new vaccines are available
        """
        self.updater: Updater = Updater(origin, max_dist, min_qty)
        self.notifiers: List[Notifier] = notifiers
        self.refresh_rate: int = rate
        self.stop_trigger = False

    def run(self) -> None:
        """
        Executes the application until self.stop_trigger is True
        """
        # setup scheduler to call main every refresh_rate seconds
        schedule.every(self.refresh_rate).seconds.do(self.main)

        # call main once now to create initial update
        self.main()
        if self.updater.in_range:
            self.print_location_table()
            self.make_location_map()

            # run app and wait for stop trigger
            while self.stop_trigger is not True:
                schedule.run_pending()
                time.sleep(self.refresh_rate)

            # reset stop trigger
            self.stop_trigger = False
        else:
            raise NoVaccinationSitesInRangeException(self.updater.origin, self.updater.max_dist)

    def main(self) -> None:
        """
        Fetch new data from H-E-B, print the time and date, and notify the user if new vaccines are available.
        """
        # update data from H-E-B
        self.updater.update()

        # Print the current date to the screen
        self.heartbeat()

        # Notify user if there are new vaccinations available
        if self.updater.new:
            self.send_notifications(list(self.updater.new.values()))

    def send_notifications(self, sites: List[VaccinationSite]) -> None:
        """
        This sends all user notifications
        """
        site_list = []
        for site in sites:
            contents = request.urlopen(site.signup_url).read().decode('utf-8')
            if 'Appointments are no longer available for this location' not in contents:
                site_list.append(site)

        for notifier in self.notifiers:
            notifier.notify(site_list)

    def heartbeat(self) -> None:
        """
        Get the current datetime and print it to the screen so the user knows the app is still running
        """
        current_datetime = datetime.datetime.now()
        print(f"Last Updated: {current_datetime.strftime('%c')}")

    def make_location_map(self):
        m = Map(location=self.updater.origin, zoom_start=10)
        Circle(location=self.updater.origin, fill_color='white', radius=self.updater.max_dist * 1609.34, weight=2,
               color="#000").add_to(m)
        CircleMarker(self.updater.origin, popup="Origin", radius=3, fill=True, color='red').add_to(m)

        for item in self.updater.in_range.values():
            if item.location.coords:
                CircleMarker(item.location.coords, popup=item.location.name,
                             radius=3, fill=True, color='blue').add_to(m)
            else:
                print(f"{item.location.name} -- {item.location.address}")
        m.save("H-E-B map.html")
        webbrowser.open('H-E-B map.html')

    def print_location_table(self):
        print("Checking for vaccines at the following locations: ")
        print(to_address_table(list(self.updater.in_range.values()), self.updater.origin))
