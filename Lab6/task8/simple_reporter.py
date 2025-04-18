class SimpleReporter():
    def analyze(self, series):
        return [f"Info: {series.indic} at {series.code} has mean = {series.mean:.2f}"]
