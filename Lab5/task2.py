import re
from pathlib import Path
from utils import show_dict



def group_measurements_by_file(path):
    files_by_key = {}
    pattern = re.compile(
        r"(?P<year>\d{4}_(?P<metric>[A-Za-z0-9]+)_(?P<freq>[0-9a-zA-Z]+)\.csv$)"
    )

    for file in path.iterdir():
        if file.is_file():
            match = pattern.match(file.name)

            if match:
                key = (
                    match.group('year'),
                    match.group('metric'),
                    match.group('freq')
                )
                files_by_key[key] = file

    return files_by_key



def default_showcase():
    show_dict(group_measurements_by_file(Path('data/measurements')))



if __name__ == '__main__':
    default_showcase()