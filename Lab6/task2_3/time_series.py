import numpy as np
from datetime import date, datetime


class TimeSeries:
    '''Class representing measurement data for a certain indicator'''

    def __init__(self, indic, code, avg_time, timestamps, values, unit):
        self.indic = indic
        self.code = code
        self.avg_time = avg_time
        self.timestamps = timestamps
        self.values = np.array(values, dtype=np.float64)
        self.unit = unit



    def __getitem__(self, key):
        if isinstance(key, (int, slice)):
            return list(zip(self.timestamps, self.values))[key]
        
        if isinstance(key, (date, datetime)):
            matches = []
            is_date = isinstance(key, date) and not isinstance(key, datetime)

            for timestamp, value in zip(self.timestamps, self.values):
                if is_date and timestamp.date() == key:
                    matches.append[value]
                elif timestamp == key:
                    matches.append(value)

            if not matches:
                raise KeyError(f"No data for timestamp {key!r}")
            
            return matches if is_date else matches[0]
        
        raise TypeError(f"Unsupported key type: {type(key)}")
    


    def __str__(self):
        return (
            f"'indicator:'  {self.indic}\n"
            f"'code:'       {self.code}\n"
            f"'avg_time:'   {self.avg_time}\n"
            f"'timestamps': {self.timestamps}\n"
            f"'values':     {self.values}\n"
            f"'unit':       {self.unit}"
        )
    


    def __repr__(self):
        return (
            "TimeSeries("
            f"indicator=    {self.indic!r}, "
            f"code=         {self.code!r}, "
            f"avg_time=     {self.avg_time!r}, "
            f"timestamps=   {self.timestamps!r}, "
            f"values=       {self.values!r}, "
            f"unit=         {self.unit!r})"
        )
    

    # ==========================================================================
    #   Properties
    # ==========================================================================

    @property
    def mean(self):
        '''Returns mean of measured values or None if no suitable data'''
        valid_values = self._validate_values(self.values)
        return float(np.mean(valid_values)) if len(valid_values) > 0 else None
    

    @property
    def stddev(self):
        '''Returns standard deviation of measured values 
           or None if no suitable data'''
        valid_values = self._validate_values(self.values)
        return float(np.std(valid_values)) if len(valid_values) > 0 else None
    

    # ==========================================================================
    #   Private methods
    # ==========================================================================

    def _validate_values(self, vals):
        return vals[~np.isnan(vals)]
    