from vaccinetracker import *

# The coordinates for the Texas Capitol.
home_coords = (30.274915353266977, -97.74035050144215)
app = Application(
    notifiers=[
        WinBeeper(200, 400),  # play a 200Hz tone for 400ms
        ConsolePrinter(home_coords),  # Print appointment info to the console
        LinkOpener()  # Open the link to the signup form
    ],
    origin=home_coords,
    min_qty=1,  # Don't show notifications less than 1
    max_dist=25,  # Search within 25 miles
    rate=10,  # update the results every 10 seconds
    vax_type=VaxType.pfizer # only look for doses of Pfizer
)
app.run()
