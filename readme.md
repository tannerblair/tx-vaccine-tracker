# ATX Vaccine Tracker

ATX Vaccine Tracker is a Python application for finding vaccination appointments at H-E-B stores in the state of Texas.

## Installation


1. Clone the repository to your computer
2. Create a new venv
3. Install packages in requirements.txt

## Usage

From the python console, run main.initialize().

If you want to customize the search criteria, you can do so by:

1. Creating a new Updater with your parameters
2. Creating a new AtxVaccineTracker instance that uses your customized updater.
3. call run() on your AtxVaccineTracker

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)