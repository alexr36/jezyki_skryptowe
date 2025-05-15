from series_validator    import SeriesValidator
from task2_3.time_series import TimeSeries



class CompositeValidator(SeriesValidator):
    def __init__(self, validators, mode='OR'):
        self.validators = validators
        self.mode = mode.upper()


    def analyze(self, series: TimeSeries) -> list[str]:
        all_messages = []

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
