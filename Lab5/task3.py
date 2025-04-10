import re
from pathlib import Path
from task1 import parse_stations
from utils import show_list



def get_addresses(path, city):
    addresses = []

    if not path.name.endswith('.csv'):
        return addresses
    
    stations = parse_stations(path)
    pattern = re.compile(
        r"(?P<street>[\w\s\.\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+?)"
        r"(?:\s+(?P<number>\d+[a-zA-Z]?([-/]\d+[a-zA-Z]?)?))?$"
    )

    for station in stations:
        station_city = station['city']

        if city.lower().strip() != station_city.lower().strip():
            continue

        address = station['address'].strip()
        match = pattern.match(address)

        street = match.group('street').strip() if match else address
        number = match.group('number') if match else None

        addresses.append((
            station['voivodeship'],
            station_city,
            street,
            number
        ))

    return addresses



def default_showcase():
    show_list(get_addresses(Path('data/stacje.csv'), 'Wschowa'))



if __name__ == '__main__':
    default_showcase()