# TX Vaccine Tracker

TX Vaccine Tracker is a Python application for finding vaccination appointments at H-E-B stores in the state of Texas.

## Installation


1. Clone the repository to your computer
2. If needed, install Python.
3. Install packages in requirements.txt

## Usage

### Easy Mode

There is an __init__.py file at the root directory. If run, that will start the utility with the default settings:

| Field         | Default Value                                                    | Description |
|---------------|------------------------------------------------------------------|-------------|
| notifiers     | [WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()] | What user notifications to call when a vaccine is available.<br> Default values play a tone, print details to the console, and open the signup link.
| home_coords   | Coords(30.27486, -97.74033)                                      | The home coordinates to use when calculating distances.<br>The default value is the Texas Capitol. | 
| max_distance  | 50                                                               | The maximum distance in miles you are willing to travel from home_coords for your vaccine. |
| min_timeslots | 1                                                                | The minimum number of vaccines you want to be notified for. If you are getting too many notifications, increase this number to filter out small numbers of vaccines that go too quickly. |
| refresh_rate  | 10                                                               | How often to check for new appointments, in seconds. |


### Hard(Custom) Mode

If you want to customize the search criteria, create a VaccineTracker object and override the settings that you would like to change, then call run() on it.

```
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

```

1. Importing the library instead.
2. Creating a new AtxVaccineTracker instance that uses your customized updater.
3. call run() on your AtxVaccineTracker

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)