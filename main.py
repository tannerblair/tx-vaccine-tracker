import datetime
from typing import List

import schedule

from updater import Updater
from notifier import Notifier, WinBeeper, ConsolePrinter


def main(updater: Updater, notifiers: List[Notifier]):
    updater.update()
    if updater.all:
        for notifier in notifiers:
            notifier.notify()

    else:
        print(f"No Doses at {datetime.datetime.now()}")


if __name__ == '__main__':
    heb = Updater()
    notifier_list = [WinBeeper(200, 400), ConsolePrinter(heb)]
    refresh_rate = 30

    schedule.every(refresh_rate).seconds.do(main, heb, notifier_list)

    main(heb, notifier_list)

    while True:
        schedule.run_pending()
