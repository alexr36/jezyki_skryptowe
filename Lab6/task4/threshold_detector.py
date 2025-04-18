from .series_validator import SeriesValidator
from task2_3.time_series import TimeSeries



class ThresholdDetector(SeriesValidator):
    def __init__(self, threshold):
        self.threshold = threshold



    def analyze(self, series: TimeSeries) -> list[str]:
        messages = []

        for i, value in enumerate(series.values):
            if value is not None and value > self.threshold:
                messages.append(
                    f"Value {value} exceeding threshold {self.threshold} found at {i}"
                )
        
        return messages