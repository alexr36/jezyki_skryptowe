import abc
from task2_3 import time_series


class SeriesValidator(abc.ABC):
    @abc.abstractmethod
    def analyze(self, series: time_series) -> list[str]:
        '''Returns list of information about anomalies or an empty list'''
        pass
