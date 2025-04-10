import csv, datetime, os
import constants as cs
from utils import save_to_json, str_to_date
from logger_setup import logger



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
                    'code':               row[cs.CODE],
                    'international_code': row[cs.INTERNATIONAL_CODE],
                    'name':               row[cs.NAME],
                    'old_code':           row[cs.OLD_CODE],
                    'launch_date':        parse_date(row[cs.LAUNCH_DATE]),
                    'close_date':         parse_date(row[cs.CLOSE_DATE]),
                    'station_type':       row[cs.STATION_TYPE],
                    'area_type':          row[cs.AREA_TYPE],
                    'station_kind':       row[cs.STATION_KIND],
                    'voivodeship':        row[cs.VOIVODESHIP],
                    'city':               row[cs.CITY],
                    'address':            row[cs.ADDRESS],
                    'latitude':           float(row[cs.LATITUDE]),
                    'longitude':          float(row[cs.LONGITUDE])
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
            headers = [next(reader) for _ in range(7)]  # First 6 rows are headers
            mapping = {
                i+1: {
                    'station_code':     headers[1][i + 1],
                    'indicator':        headers[2][i + 1],
                    'averaging_time':   headers[3][i + 1],
                    'unit':             headers[4][i + 1],
                    'stand_id':         headers[5][i + 1]
                }
                for i in range(len(headers[1]) - 1)
            }

            for row_num, row in enumerate(reader, start=7):
                raw_line = ','.join(row)
                logger.debug(
                    f"Row {row_num}: Read {len(raw_line.encode('utf-8'))} bytes"
                )

                try:
                    timestamp = datetime.datetime.strptime(
                        row[0].strip(), "%m/%d/%y %H:%M"
                    )
                except Exception as e:
                    logger.warning(f"Invalid timestamp at row {row_num}: {e}")
                    continue

                # Start from 1 (0 is a timestamp)
                for i in range(1, len(row)):
                    raw_value = row[i].strip()

                    if i not in mapping or not raw_value:
                        continue

                    try:
                        val = float(raw_value)
                        m = mapping[i]
                        data.append({
                            'datetime':     timestamp,
                            'station_code': m['station_code'],
                            'indicator':    m['indicator'],
                            'unit':         m['unit'],
                            'avg_time':     m['averaging_time'],
                            'value':        val,
                            'stand_id':     m['stand_id']
                        })
                    except ValueError:
                        logger.warning(
                            f"Invalid float: row {row_num}, col {i + 1}: {row[i]}"
                        )
        
            logger.info(
                f"Finished parsing '{filepath}'. Total: {len(data)} records."
            )
            return data

    except Exception as e:
        logger.error(f"Error while parsing '{filepath}': {e}")
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
