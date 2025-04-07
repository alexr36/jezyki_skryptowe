import re, datetime
from pathlib import Path
from task1 import parse_stations
from utils import show_list


#   a)
def extract_dates(stations):
    dates = set()
    pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

    for station in stations:
        for field in ['launch_date', 'close_date']:
            value = station.get(field)

            if value:
                match = pattern.search(str(value))

                if match:
                    dates.add(match.group())

    return sorted(dates)


#   b)
def extract_coordinates(stations):
    coordinates = []
    pattern = re.compile(r"\d{2}.\d{6}")

    for station in stations:
        lat = f"{station['latitude']:.6f}"
        lon = f"{station['longitude']:.6f}"

        if pattern.fullmatch(lat) and pattern.fullmatch(lon):
            coordinates.append((lat, lon))

    return coordinates


#   c)
def find_two_part_named_stations(stations):
    two_parts = []
    pattern = re.compile(r"^[^-\-]+ *[--] *[^-\-]+$")

    for station in stations:
        name = station['name']
        match = pattern.match(name)

        if match:
            two_parts.append(name)

    return two_parts


#   d)
def normalize_names(stations):
    def normalize(text):
        text = re.sub(r'\s+', '_', text)
        diacritics = {
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l',
            'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
            'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L',
            'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
        }
        
        return ''.join(diacritics.get(char, char) for char in text)
    
    normalized = []
    
    for station in stations:
        normalized.append(normalize(station['name']))

    return normalized


#   e)
def find_incorrectly_mob_coded_stations(stations):
    incorrects = []
    pattern = re.compile(r"MOB$", re.IGNORECASE)

    for station in stations:
        code = station['code']
        kind = station['station_kind'].lower()

        if pattern.search(code) and kind != 'mobilna':
            incorrects.append((code, kind))

    return incorrects


#   f)
def extract_three_part_name_locations(stations):
    pattern = re.compile(r"^\s*[^-]+?\s*-\s*[^-]+?\s*-\s*[^-]+?\s*$")
    localizations = []

    for station in stations:
        location = station['address']

        if pattern.match(location):
            localizations.append(location.strip())
    
    return localizations


#   g)
def find_locations_with_comma_and_streetname(stations):
    locations = []
    pattern = re.compile(r"(ul\.|al\.).*?,|,.*?(ul\.|al\.)", re.IGNORECASE)

    for station in stations:
        address = station['address']

        if pattern.search(address):
            locations.append(address)

    return locations



def default_showcase():
    stations = parse_stations('data/stacje.csv')

    print("\n\na) Dates in YYYY-MM-DD format\n")
    show_list(extract_dates(stations))

    print("\\nb) Coordinates (latitude, longitude)")
    show_list(extract_coordinates(stations))

    print("\n\nc) Two-part names")
    show_list(find_two_part_named_stations(stations))

    print("\n\nd) Normalized names")
    show_list(normalize_names(stations))

    print("\n\ne) Incorrectly MOB-coded stations")
    show_list(find_incorrectly_mob_coded_stations(stations))

    print("\n\nf) Three-part named locations")
    show_list(extract_three_part_name_locations(stations))

    print("\n\ng) Locations with a comma and a street name")
    show_list(find_locations_with_comma_and_streetname(stations))



if __name__ == '__main__':
    default_showcase()