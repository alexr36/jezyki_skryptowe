from src.time_series import TimeSeries



class SimpleReporter():
    def analyze(self, series : TimeSeries) -> list[str]:
        return [f"Info: {series.indic} at {series.code} has mean = {series.mean:.2f}"]
