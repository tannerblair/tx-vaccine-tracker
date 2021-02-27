import datetime
import schedule
import winsound

from heb import heb_table, heb_locations_with_doses
from mailer import get_service, create_message, send_message

# Texas Capitol by default. Look your address up on Google Maps, right-click, then click the coords and paste them here.
COORDS = (30.27489682206901, -97.74035050144215)

# How far you are willing to drive in miles.
DISTANCE = 50

# The smallest number of appointments that you want to be notified for.
THRESHOLD = 10

# Enables Emails. If you want to set this up, you'll need a Gmail account and a credentials.json file.
# https://developers.google.com/gmail/api/quickstart/python#step_1_turn_on_the
# Once you've set that up, it will authenticate when launched. Occasionally, if you stop the service and restart it
# will be angry. delete the pickle file and re-authenticate and it should be good. Honestly though, the beep thing
# is faster and better.
EMAIL = False

# Gmail account address to send notifications from
SEND_ADDRESS = "sender@gmail.com"

# When emails are enabled, the script sends an email to each address in the list
MAILING_LIST = [
    "name@email.com"
]

# Number of seconds between updates. Must be a number greater than 10.
REFRESH_RATE = 30


def main(service=None):
    data = heb_locations_with_doses(COORDS, DISTANCE, THRESHOLD)
    if data:
        winsound.Beep(200, 200)

        table = heb_table(data)
        print(table)

        if service:
            send_email(service, data)
    else:
        print(f"No Doses at {datetime.datetime.now()}")


def send_email(service, data):
    table = heb_table(data)
    total = 0
    for location in data:
        total += location["openTimeslots"]
    for address in MAILING_LIST:
        msg = create_message(SEND_ADDRESS, address, f"{total} Vaccines Available!",
                             table.get_html_string(format=True))
        send_message(service, "me", msg)


if __name__ == '__main__':

    if EMAIL:
        svc = get_service()
    else:
        svc = None

    schedule.every(REFRESH_RATE).seconds.do(main, svc)
    main(svc)
    while True:
        schedule.run_pending()
