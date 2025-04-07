import re
from pathlib import Path
from task1 import parse_stations
from utils import show_list



def get_addresses(path, city):
    addresses = []

    if path.name.endswith('.csv'):
        stations = parse_stations(path)
        pattern = re.compile(
            r"(?P<street>[\w\s\.\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+?)"
            r"(?:\s+(?P<number>\d+[a-zA-Z]?([-/]\d+[a-zA-Z]?)?))?$"
        )

        for station in stations:
            stat_city = station['city']

            if city.lower().strip() != stat_city.lower().strip():
                continue

            address = station['address'].strip()
            match = pattern.match(address)

            if match:
                street = match.group('street').strip()
                number = match.group('number')
            else:
                street = address
                number = None

            record = (
                station['voivodeship'],
                stat_city,
                street,
                number
            )

            addresses.append(record)

    return addresses



def default_showcase():
    show_list(get_addresses(Path('data/stacje.csv'), 'Wschowa'))



if __name__ == '__main__':
    default_showcase()