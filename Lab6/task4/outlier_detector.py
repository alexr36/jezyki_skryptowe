from .series_validator import SeriesValidator
from task2_3.time_series import TimeSeries



class OutlierDetector(SeriesValidator):
    def __init__(self, k: float = 1.0):
        self.k = k

    
    
    def analyze(self, series: TimeSeries) -> list[str]:
        mean = series.mean
        std = series.stddev
        messages = []

        if mean is None or std is None:
            return ["No suitable data for analyzing deviations"]
        
        for i, value in enumerate(series.values):
            if value is not None and abs(value - mean) > self.k * std:
                messages.append(f"Outlier detected at index {i}: {value}")

        return messages