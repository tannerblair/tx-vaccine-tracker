from .location import Coords
from .notifier import WinBeeper, ConsolePrinter, LinkOpener
from .application import Application

if __name__ == '__main__':
    home_coords = Coords(30.27486, -97.74033)
    app = Application(
        notifiers=[WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()],
        home_coords=Coords(30.44798781702195, -97.68902362940327),
        min_timeslots=1,
        max_distance=20,
        refresh_rate=10
    )
    app.run()
