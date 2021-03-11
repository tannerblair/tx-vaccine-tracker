# TX Vaccine Tracker

TX Vaccine Tracker is a Python application for finding vaccination appointments at H-E-B stores in the state of Texas.

## Installation

1. Clone the repository to your computer
2. If needed, install Python.
3. Install packages in requirements.txt

## Usage

### VaccineTracker Parameters

| Field        | Datatype            | Description                                                                                |
|--------------|---------------------|--------------------------------------------------------------------------------------------|
| notifiers    | List[Notifier]      | What user notifications to call when a vaccine is available.                               |
| origin       | Tuple[float, float] | The home coordinates to use when calculating distances.                                    | 
| max_dist     | int                 | The maximum distance in miles you are willing to travel from home_coords for your vaccine. |
| min_qty      | int                 | The minimum number of available vaccines you want to be notified for.                      |
| refresh_rate | int                 | How often to check for new appointments, in seconds.                                       |


### Examples

There are examples in the `examples` directory, and basic usage is shown below:

```
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
    max_dist=20,  # Search within 20 miles
    rate=10  # update the results every 10 seconds
)
app.run()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
