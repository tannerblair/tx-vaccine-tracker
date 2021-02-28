import datetime
from typing import List

import schedule

from updateformatter import SiteType
from updater import Updater
from notifier import Notifier, WinBeeper, ConsolePrinter, LinkOpener


class AtxVaccineTracker:
    
    def __init__(self, updater: Updater, notifiers: List[Notifier], refresh_rate) -> None:
        """
        Create a new instance of the AtxVaccineTracker application.
        :param updater: the service that fetches new data from H-E-B's vaccine website and parses it
        :param notifiers: a list of Notifier instances that will be called when new vaccines are available
        """
        self.updater: Updater = updater
        self.notifiers: List[Notifier] = notifiers
        self.refresh_rate = refresh_rate
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
            notifier.notify(updater, site_type)

    def heartbeat(self) -> None:
        """
        Get the current datetime and print it to the screen so the user knows the app is still running
        """
        current_datetime = datetime.datetime.now()
        print(f"Last Updated: {current_datetime.strftime('%c')}")


def initialize():
    # The updater can be customized with a new starting location, a minimum threshold for the number of
    # vaccines you want to be notified for, and the maximum distance you're willing to travel for it.
    heb = Updater()

    # The notifier list contains WinBeeper and ConsolePrinter, which together will chime and print a notification to
    # the screen when new vaccinations are available.
    notifier_list = [WinBeeper(200, 400), ConsolePrinter(), LinkOpener()]

    # Create a new instance of the AtxVaccineTracker and set it to update every 10 seconds
    app = AtxVaccineTracker(heb, notifier_list, 10)
    app.run()


if __name__ == '__main__':
    initialize()
