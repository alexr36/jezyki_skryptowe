import re, csv, datetime, numpy as np
from pathlib                         import Path
from src.time_series                 import TimeSeries
from src.logger_setup                import logger
from src.validators.series_validator import *
from typing                          import Optional, Iterator



class Measurements():
    '''Class aggregating data regarding one indicator'''  

    def __init__(self, directory : str | Path) -> None:
        self.directory : Path = Path(directory)
        self.files : list[tuple[Path, dict[str, str]]] = self._index_files()
        self._cache : dict[str, list[TimeSeries]] = {}


    def _index_files(self) -> list[tuple[Path, dict[str, str]]]:
        pattern = re.compile(
            r'(?P<year>\d{4})_(?P<parameter>[A-Za-z0-9()]+)_(?P<freq>\d+[a-zA-Z]+)\.csv$'
        )
        files : list[tuple[Path, dict[str, str]]] = []

        for file in self.directory.iterdir():
            if file.is_file():
                match : Optional[re.Match] = pattern.match(file.name)

                if match:
                    files.append((file, match.groupdict()))
        
        return files
    

    def _load_file(self, filepath : Path) -> list[TimeSeries]:
        series_list : list[TimeSeries] = []

        try:
            with open(filepath, encoding='utf-8') as file:
                reader : Iterator[list[str]] = csv.reader(file)
                headers : list[list[str]] = [next(reader) for _ in range(7)]

                station_codes : list[str] = headers[1][1:]
                indicators : list[str] = headers[2][1:]
                avg_times : list[str] = headers[3][1:]
                units : list[str] = headers[4][1:]

                timestamps : list[datetime.datetime] = []
                values : list[list[float]] = [[] for _ in station_codes]

                for row_num, row in enumerate(reader, start=7):
                    try:
                        timestamp : datetime.datetime = datetime.datetime.strptime(row[0].strip(), "%m/%d/%y %H:%M")
                        timestamps.append(timestamp)

                        for i, value in enumerate(row[1:]):
                            value = value.strip()
                            values[i].append(float(value) if value else np.nan)

                    except Exception as e:
                        logger.warning(f"Row {row_num}: {e}")
                        continue

                for i in range(len(station_codes)):
                    series : TimeSeries = TimeSeries(
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


    def _load_all(self) -> list[TimeSeries]:
        all_series : list[TimeSeries] = []

        for file, _ in self.files:
            filename : str = file.name

            if filename not in self._cache:
                self._cache[filename] = self._load_file(file)
            
            all_series.extend(self._cache[filename])
        
        return all_series


    def __len__(self) -> int:
        return len(self.files)


    def __contains__(self, parameter_name: str) -> bool:
        return any(
            measurement['parameter'].lower() == parameter_name.lower()
            for _, measurement in self.files
        )


    def get_by_parameter(self, param_name: str) -> list[TimeSeries]:
        results : list[TimeSeries] = []

        for timestamp in self._load_all():
            if timestamp.indic.lower() == param_name.lower():
                results.append(timestamp)
        
        return results


    def get_by_station(self, station_code: str) -> list[TimeSeries]:
        results : list[TimeSeries] = []

        for timestamp in self._load_all():
            if timestamp.code == station_code:
                results.append(timestamp)
        
        return results
    

    def detect_all_anomalies(
            self, validators: list[SeriesValidator], 
            preload: bool = False
        ) -> dict[str, list[str]]:
        anomalies : dict[str, list[str]] = {}

        if preload:
            _ = self._load_all()

        for _, series_list in self._cache.items():
            for series in series_list:
                all_issues : list[str] = []

                for validator in validators:
                    issues : list[str] = validator.analyze(series)

                    if issues:
                        all_issues.extend(issues)
                
                if all_issues:
                    key : str = f"{series.code} ({series.indic})"
                    anomalies[key] = all_issues
        
        return anomalies
