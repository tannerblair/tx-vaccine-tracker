import json
import urllib.request
import prettytable
from geopy.distance import geodesic


def heb_locations(coords, distance=-1):
    # Use a breakpoint in the code line below to debug your script.
    with urllib.request.urlopen("https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json") as url:
        data = json.loads(url.read().decode())
    data = data["locations"]
    for location in data:
        location["distance"] = geodesic(coords, (location["latitude"], location["longitude"])).miles
    if distance != -1:
        data = filter_distance(data, distance)
    return data


def filter_has_appointments(data, threshold=10):
    data = [site for site in data if site["openTimeslots"] > threshold]

    return data


def filter_distance(data, distance):
    if data:
        data = [site for site in data if site["distance"] <= distance]
    return data


def heb_locations_with_doses(coords, distance=-1, threshold=10):
    data = filter_has_appointments(heb_locations(coords, distance), threshold)
    return data


def heb_table(data):
    table = prettytable.PrettyTable(["Name", "Url", "Distance", "Open Appointment Slots",
                                     "Open Time Slots", "Street", "City", "ZIP", "Open In Maps"])
    for location in data:
        loc_url = f"https://www.google.com/maps/@{location['latitude']},{location['longitude']},17z"
        table.add_row([
            location["name"],
            location["url"],
            round(location["distance"]),
            location['openAppointmentSlots'],
            location["openTimeslots"],
            location["street"],
            location["city"],
            location["zip"],
            loc_url
        ])
    return table
