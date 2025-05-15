from .series_validator import SeriesValidator
from src.time_series   import TimeSeries
from typing            import Optional



class OutlierDetector(SeriesValidator):
    def __init__(self, k: float = 1.0) -> None:
        self.k : float = k

    
    def analyze(self, series: TimeSeries) -> list[str]:
        mean : Optional[float] = series.mean
        std : Optional[float] = series.stddev
        messages : list[str] = []

        if mean is None or std is None:
            return ["No suitable data for analyzing deviations"]
        
        for i, value in enumerate(series.values):
            if value is not None and abs(value - mean) > self.k * std:
                messages.append(f"Outlier detected at index {i}: {value}")

        return messages