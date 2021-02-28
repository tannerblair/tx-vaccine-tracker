import datetime
from typing import List

import schedule

from updateformatter import SiteTypes
from updater import Updater
from notifier import Notifier, WinBeeper, ConsolePrinter


class Application:
    def __init__(self, updater: Updater, notifiers: List[Notifier]):
        self.updater: Updater = updater
        self.notifiers: List[Notifier] = notifiers

    def main(self):
        self.updater.update()
        self.heartbeat()
        if self.updater.new:
            self.send_notifications()

    def send_notifications(self):
        for notifier in self.notifiers:
            notifier.notify()

    def heartbeat(self):
        current_datetime = datetime.datetime.now()
        print(f"Last Updated: {current_datetime.strftime('%c')}")



if __name__ == '__main__':
    heb = Updater()
    notifier_list = [WinBeeper(200, 400), ConsolePrinter(heb, SiteTypes.NEW)]
    refresh_rate = 10
    app = Application(heb, notifier_list)

    schedule.every(refresh_rate).seconds.do(app.main)

    app.main()

    while True:
        schedule.run_pending()
