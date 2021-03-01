from .location import Coords
from .notifier import WinBeeper, ConsolePrinter, LinkOpener
from .application import Application

if __name__ == '__main__':
    home_coords = Coords(30.274915353266977, -97.74035050144215)  # The Texas Capitol
    app = Application(
        notifiers=[WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()],
        home_coords=home_coords,
        min_timeslots=1,
        max_distance=20,
        refresh_rate=10
    )
    app.run()
