import datetime
from typing import List

import schedule

from hebupdater import HebUpdater
from notifier import Notifier, WinBeeper
from updateformatter import updater_to_table_str, SiteTypes


def main(updater: HebUpdater, notifiers: List[Notifier]):
    updater.update()
    if updater.new:
        for notifier in notifiers:
            notifier.notify()
        table = updater_to_table_str(updater, SiteTypes.ALL)
        print(table)

    else:
        print(f"No Doses at {datetime.datetime.now()}")


if __name__ == '__main__':
    heb = HebUpdater()
    notifier_list = [WinBeeper(200, 400)]
    refresh_rate = 30

    schedule.every(refresh_rate).seconds.do(main)

    main(heb, notifier_list)

    while True:
        schedule.run_pending()
