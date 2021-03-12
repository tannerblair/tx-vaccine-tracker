import datetime
import time
import webbrowser
from typing import List, Tuple
from urllib import request

import pandas as pd
import streamlit as st

import schedule
from folium import Circle, CircleMarker, Map

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
            #self.print_location_table()
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
        self.notify_user()

    def notify_user(self):
        site_list = []
        if self.updater.new:
            for site in list(self.updater.new.values()):
                contents = request.urlopen(site.signup_url).read().decode('utf-8')
                if 'Appointments are no longer available for this location' not in contents:
                    site_list.append(site)

        if site_list:
            for notifier in self.notifiers:
                notifier.notify(site_list)

    def heartbeat(self) -> None:
        """
        Get the current datetime and print it to the screen so the user knows the app is still running
        """
        current_datetime = datetime.datetime.now()
        print(f"Last Updated: {current_datetime.strftime('%c')}")

    def make_location_map(self):
        """
        Return coords of heb's in range. And output list on page
        """
        self.main()
        coords = []
        for item in self.updater.in_range.values():
            if item.location.coords:
               coords.append(item.location.coords) 
        if coords == []: st.text("Revise Search Criteria")        
        else: self.print_location_table()
        return coords

    def print_location_table(self):
        st.text("Checking for vaccines at the following locations: ")
        st.text(to_address_table(list(self.updater.in_range.values()), self.updater.origin))
