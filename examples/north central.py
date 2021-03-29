from vaccinetracker import *
from geopy import Nominatim

locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode("Anderson Lane, Austin TX")
home_coords = location.latitude, location.longitude

app = Application(
    notifiers=[
        WinBeeper(200, 400),  # play a 200Hz tone for 400ms
        ConsolePrinter(home_coords),  # Print appointment info to the console
        LinkOpener()  # Open the link to the signup form
    ],
    origin=home_coords,
    min_qty=1,
    max_dist=15,
    rate=1,
    vax_type=VaxType.all
)
app.run()
