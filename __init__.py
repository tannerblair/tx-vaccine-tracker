from location import Coords
from notifier import WinBeeper, ConsolePrinter, LinkOpener
from vaccinetracker import VaccineTracker

if __name__ == '__main__':
    home_coords = Coords(30.27486, -97.74033)
    app = VaccineTracker(
        notifiers=[WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()],
        home_coords=Coords(30.27486, -97.74033),
        min_timeslots=1,
        max_distance=50,
        refresh_rate=10
    )
    app.run()
