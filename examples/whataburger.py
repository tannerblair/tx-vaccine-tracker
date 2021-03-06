from vaccinetracker import *

# The coordinates for the Whataburger on Anderson Lane.
home_coords = (30.35894120209235, -97.73708821418394)
app = Application(
    notifiers=[
        WinBeeper(300, 500),  # play a 300Hz tone for 500ms
        ConsolePrinter(home_coords),  # Print appointment info to the console
        LinkOpener()  # Open the link to the signup form
    ],
    origin=home_coords,
    min_qty=10,  # Don't show notifications less than 10
    max_dist=10,  # You don't want to get too far away from Whataburger, so nothing farther than 10 miles
    rate=30  # update the results every 30 seconds
)
app.run()
