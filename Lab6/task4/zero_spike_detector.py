from task4.series_validator import SeriesValidator
from task2_3.time_series    import TimeSeries 



class ZeroSpikeDetector(SeriesValidator):
    def analyze(self, series: TimeSeries) -> list[str]:
        messages = []
        count = 0

        for i, value in enumerate(series.values):
            if value == 0 or value is None:
                count += 1

                if count >= 3:
                    messages.append(
                        f"Zero or missing data spike from index {i - 2} to {i}"
                    )
            else:
                count = 0
        
        return messages
