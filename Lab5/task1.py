import csv, datetime, os
from utils import save_to_json, str_to_date
from logger_setup import logger


CODE = "Kod stacji"
INTERNATIONAL_CODE = "Kod międzynarodowy"
NAME = "Nazwa stacji"
OLD_CODE = "Stary Kod stacji (o ile inny od aktualnego)"
LAUNCH_DATE = "Data uruchomienia"
CLOSE_DATE = "Data zamknięcia"
STATION_TYPE = "Typ stacji"
AREA_TYPE = "Typ obszaru"
STATION_KIND = "Rodzaj stacji"
VOIVODESHIP = "Województwo"
CITY = "Miejscowość"
ADDRESS = "Adres"
LATITUDE = "WGS84 φ N"
LONGITUDE = "WGS84 λ E"




def parse_date(date_string):
    if not date_string:
        return None
    
    try:
        if "24:00" in date_string:
            base = datetime.datetime.strptime(
                date_string.replace("24:00", "00:00"), "%Y-%m-%d %H:%M"
            )
            return base + datetime.timedelta(days=1)
        
        return str_to_date(date_string).date()
    except ValueError:
        return None



def parse_stations(filepath):
    stations = []
    logger.info(f"Reading stations from file '{filepath}'...")

    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                station = {
                    'code': row[CODE],
                    'international_code': row[INTERNATIONAL_CODE],
                    'name': row[NAME],
                    'old_code': row[OLD_CODE],
                    'launch_date': parse_date(row[LAUNCH_DATE]),
                    'close_date': parse_date(row[CLOSE_DATE]),
                    'station_type': row[STATION_TYPE],
                    'area_type': row[AREA_TYPE],
                    'station_kind': row[STATION_KIND],
                    'voivodeship': row[VOIVODESHIP],
                    'city': row[CITY],
                    'address': row[ADDRESS],
                    'latitude': float(row[LATITUDE]),
                    'longitude': float(row[LONGITUDE])
                }

                stations.append(station)
            except Exception as e:
                logger.warning(f"Could not parse record: {e}")
                continue

    logger.info(f"Succesfully read {len(stations)} stations")
    return stations



def parse_measurement(filepath):
    logger.info(f"Parsing measurements from '{filepath}'...")
    data = []

    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return data

    try:
        with open(filepath, encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = [next(reader) for _ in range(7)]
            mapping = {
                i+1: {
                    'station_code': headers[1][i + 1],
                    'indicator': headers[2][i + 1],
                    'unit': headers[4][i + 1],
                    'station_id': headers[5][i + 1]
                }
                for i in range(len(headers[1]) - 1)
            }

            for row_num, row in enumerate(reader, start=8):
                raw_line = ','.join(row)
                logger.debug(f"[Row {row_num}] Read {len(raw_line.encode('utf-8'))} bytes")

                try:
                    timestamp = datetime.datetime.strptime(
                        row[0].strip(), "%m/%d/%y %H:%M"
                    )
                except Exception as e:
                    logger.warning(f"Invalid timestamp at row {row_num}: {e}")
                    continue

                for i in range(1, len(row)):
                    raw_value = row[i].strip()
                    if i not in mapping or not raw_value:
                        continue
                

                    try:
                        val = float(raw_value)
                        m = mapping[i]
                        data.append({
                            'datetime': timestamp,
                            'station_code': m['station_code'],
                            'indicator': m['indicator'],
                            'unit': m['unit'],
                            'value': val,
                            'station_id': m['station_id']
                        })
                    except ValueError:
                        logger.warning(
                            f"Invalid float at row {row_num}, col {i + 1}: {row[i]}"
                        )
        
            logger.info(f"Finished parsing '{filepath}'. Total: {len(data)} records.")
            return data

    except Exception as e:
        logger.error(f"Critical error while parsing '{filepath}': {e}")
        return []



def parse_all_measurements(directory):
    all_measurements = []

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            path = os.path.join(directory, filename)
            measurements = parse_measurement(path)
            all_measurements.extend(measurements)
    
    return all_measurements



def default_showcase():
    source = 'data/'
    dest = 'output/'
    save_to_json(parse_stations(f"{source}stacje.csv"), f"{dest}stations.json")
    save_to_json(
        parse_all_measurements(f"{source}measurements"), 
        f"{dest}measurements.json"
    )


if __name__ == '__main__':
    default_showcase()
