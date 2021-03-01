from vaccinetracker.location import Coords
from vaccinetracker.notifier import WinBeeper, ConsolePrinter, LinkOpener
from vaccinetracker.application import Application

if __name__ == '__main__':
    # The coordinates for the Whataburger on Anderson Lane.
    home_coords = Coords(30.35894120209235, -97.73708821418394)
    app = Application(
        notifiers=[
            WinBeeper(300, 500),  # play a 300Hz tone for 500ms
            ConsolePrinter,  # Print appointment info to the console
            LinkOpener()  # Open the link to the signup form
        ],
        home_coords=home_coords,
        min_timeslots=10,  # Don't show notifications less than 10
        max_distance=2,  # You don't want to get too far away from Whataburger, so nothing farther than 2 miles
        refresh_rate=30  # update the results every 30 seconds
    )
    app.run()
