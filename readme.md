# TX Vaccine Tracker

TX Vaccine Tracker is a Python application for finding vaccination appointments at H-E-B stores in the state of Texas.

## Installation


1. Clone the repository to your computer
2. If needed, install Python.
3. Install packages in requirements.txt

## Usage

### Easy Mode

There is an __init__.py file at the root directory. If run, that will start the utility with the default settings:

| Field | Default Value | Description |
|-------|-------|-------------|
| notifiers | `[WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()]` | What user notifications to call when a vaccine is available.
| home_coords | `Coords(30.27486, -97.74033)` (Texas Capitol) | The home coordinates to use when calculating distances. | 
| min_timeslots | `1` | The minimum number of vaccines you want to be notified for. If you are getting too many notifications, increase this number to filter out small numbers of vaccines that go too quickly. |
| max_distance | `50` | The maximum distance you are willing to travel from home_coords for your vaccine. |
| refresh_rate | `10` | How often to check for new appointments, in seconds.

If you want to customize the search criteria, create a VaccineTracker object and override the settings that you would like to change, then call run() on it.

```
home_coords = Coords(30.27486, -97.74033)
    app = VaccineTracker(
        notifiers=[WinBeeper(200, 400), ConsolePrinter(home_coords), LinkOpener()],
        home_coords=Coords(30.27486, -97.74033),
        min_timeslots=1,
        max_distance=50,
        refresh_rate=10
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