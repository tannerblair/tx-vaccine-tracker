import datetime
from typing import List

import schedule

from location import Coords
from notifier import Notifier
from updateformatter import SiteType
from updater import Updater


class VaccineTracker:

    def __init__(self, notifiers: List[Notifier], home_coords: Coords,
                 min_timeslots: int, max_distance: int, refresh_rate: int):
        """
        Create a new instance of the AtxVaccineTracker application.
        :param notifiers: a list of Notifier instances that will be called when new vaccines are available
        """
        self.updater: Updater = Updater(home_coords, min_timeslots, max_distance)
        self.notifiers: List[Notifier] = notifiers
        self.refresh_rate: int = refresh_rate
        self.stop_trigger = False

    def run(self) -> None:
        """
        Executes the application until self.stop_trigger is True
        """
        # setup scheduler to call main every refresh_rate seconds
        schedule.every(self.refresh_rate).seconds.do(self.main)

        # call main once now to create initial update
        self.main()

        # run app and wait for stop trigger
        while self.stop_trigger is not True:
            schedule.run_pending()

        # reset stop trigger
        self.stop_trigger = False

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
            self.send_notifications(self.updater, SiteType.NEW)

    def send_notifications(self, updater: Updater, site_type: SiteType) -> None:
        """
        This sends all user notifications
        """
        for notifier in self.notifiers:
            notifier.notify(list(updater.new.values()))

    def heartbeat(self) -> None:
        """
        Get the current datetime and print it to the screen so the user knows the app is still running
        """
        current_datetime = datetime.datetime.now()
        print(f"Last Updated: {current_datetime.strftime('%c')}")