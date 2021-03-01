from vaccinetracker.location import Coords
from vaccinetracker.notifier import WinBeeper, ConsolePrinter, LinkOpener
from vaccinetracker.application import Application

# The coordinates for the Texas Capitol.
home_coords = Coords(30.274915353266977, -97.74035050144215)
app = Application(
    notifiers=[
        WinBeeper(200, 400),  # play a 200Hz tone for 400ms
        ConsolePrinter(home_coords),  # Print appointment info to the console
        LinkOpener()  # Open the link to the signup form
    ],
    home_coords=home_coords,
    min_timeslots=1,  # Don't show notifications less than 1
    max_distance=20,  # Search within 20 miles
    refresh_rate=10  # update the results every 10 seconds
)
app.run()
