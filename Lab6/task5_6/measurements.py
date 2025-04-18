import re, csv, datetime, numpy as np
from pathlib import Path
from task2_3.time_series import TimeSeries
from logger_setup import logger
from task4.series_validator import *


class Measurements():
    '''Class aggregating data regarding one indicator'''  

    def __init__(self, directory):
        self.directory = Path(directory)
        self.files = self._index_files()
        self._cache = {}



    def _index_files(self):
        pattern = re.compile(
            r'(?P<year>\d{4})_(?P<parameter>[A-Za-z0-9()]+)_(?P<freq>\d+[a-zA-Z]+)\.csv$'
        )
        files = []

        for file in self.directory.iterdir():
            if file.is_file():
                match = pattern.match(file.name)

                if match:
                    files.append((file, match.groupdict()))
        
        return files
    


    def _load_file(self, filepath, meta):
        series_list = []

        try:
            with open(filepath, encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = [next(reader) for _ in range(7)]

                station_codes = headers[1][1:]
                indicators = headers[2][1:]
                avg_times = headers[3][1:]
                units = headers[4][1:]

                timestamps = []
                values = [[] for _ in station_codes]

                for row_num, row in enumerate(reader, start=7):
                    try:
                        timestamp = datetime.datetime.strptime(row[0].strip(), "%m/%d/%y %H:%M")
                        timestamps.append(timestamp)

                        for i, value in enumerate(row[1:]):
                            value = value.strip()
                            values[i].append(float(value) if value else np.nan)

                    except Exception as e:
                        logger.warning(f"Row {row_num}: {e}")
                        continue

                for i in range(len(station_codes)):
                    series = TimeSeries(
                        indic=indicators[i],
                        code=station_codes[i],
                        avg_time=avg_times[i],
                        timestamps=timestamps,
                        values=values[i],
                        unit=units[i]
                    )
                    series_list.append(series)
        except Exception as e:
            logger.error(f"Failed to parse file {filepath!r}: {e}")

        return series_list



    def _load_all(self):
        all_series = []

        for file, metadata in self.files:
            filename = file.name

            if filename not in self._cache:
                self._cache[filename] = self._load_file(file, metadata)
            
            all_series.extend(self._cache[filename])
        
        return all_series



    def __len__(self):
        return len(self.files)



    def __contains__(self, parameter_name: str):
        return any(
            measurement['parameter'].lower() == parameter_name.lower()
            for _, measurement in self.files
        )



    def get_by_parameter(self, param_name: str):
        results = []

        for timestamp in self._load_all():
            if timestamp.indic.lower() == param_name.lower():
                results.append(timestamp)
        
        return results



    def get_by_station(self, station_code: str) -> list[TimeSeries]:
        results = []

        for timestamp in self._load_all():
            if timestamp.code == station_code:
                results.append(timestamp)
        
        return results
    


    def detect_all_anomalies(
            self, validators: list[SeriesValidator], 
            preload: bool = False
        ):
        anomalies = {}

        if preload:
            _ = self._load_all()

        for _, series_list in self._cache.items():
            for series in series_list:
                all_issues = []

                for validator in validators:
                    issues = validator.analyze(series)

                    if issues:
                        all_issues.extend(issues)
                
                if all_issues:
                    key = f"{series.code} ({series.indic})"
                    anomalies[key] = all_issues
        
        return anomalies
