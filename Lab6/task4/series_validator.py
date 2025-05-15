import abc
from task2_3.time_series import TimeSeries


class SeriesValidator(abc.ABC):
    @abc.abstractmethod
    def analyze(self, series: TimeSeries) -> list[str]:
        '''Returns list of information about anomalies or an empty list'''
        pass
