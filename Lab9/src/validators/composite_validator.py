from series_validator import SeriesValidator
from src.time_series  import TimeSeries



class CompositeValidator(SeriesValidator):
    def __init__(self, validators : list[SeriesValidator], mode : str = 'OR') -> None:
        self.validators : list[SeriesValidator] = validators
        self.mode : str = mode.upper()


    def analyze(self, series: TimeSeries) -> list[str]:
        all_messages : list[list[str]] = []

        for validator in self.validators:
            all_messages.append(validator.analyze(series))

        if self.mode == 'OR':
            for messages in all_messages:
                if messages:
                    return messages
                
                return []
        elif self.mode == 'AND':
            combined = []

            for messages in all_messages:
                combined.extend(messages)
                
            return combined
        
        return [f"Unknown mode: {self.mode!r}"]