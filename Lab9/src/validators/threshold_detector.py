from .series_validator import SeriesValidator
from src.time_series   import TimeSeries



class ThresholdDetector(SeriesValidator):
    def __init__(self, threshold : float) -> None:
        self.threshold : float = threshold


    def analyze(self, series: TimeSeries) -> list[str]:
        messages : list[str] = []

        for i, value in enumerate(series.values):
            if value is not None and value > self.threshold:
                messages.append(
                    f"Value {value} exceeding threshold {self.threshold} found at {i}"
                )
        
        return messages