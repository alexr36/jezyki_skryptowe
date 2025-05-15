# ------------------------------------------------------------------------------
#   Definitions of fixtures used in testing all modules
# ------------------------------------------------------------------------------

import pytest
from pathlib         import Path
from src.station     import Station
from src.time_series import TimeSeries
from datetime        import datetime


@pytest.fixture
def station_sample():
    return Station(
        code        = '001',
        intern_code = '001A', 
        name        = 'Test Station',
        old_code    = None, 
        launch      = None,
        close       = None, 
        st_type     = 'Type',
        area        = 'Area', 
        kind        = 'Kind', 
        voiv        = 'Voiv',
        city        = 'City',
        addr        = 'Addr', 
        lat         = 50.0,
        lon         = 20.0
    )


@pytest.fixture
def time_series_sample():
    timestamps = [
        datetime(2025, 1, 1, 12),
        datetime(2025, 1, 2, 12),
        datetime(2025, 1, 3, 12)
    ]
    values = [10.0, 20.0, 30.0]

    return TimeSeries('TEMP', '001', '12g', timestamps, values, 'C')


@pytest.fixture
def time_series_w_nan_sample():
    timestamps = [
        datetime(2025, 1, 1, 12),
        datetime(2025, 1, 2, 12),
        datetime(2025, 1, 3, 12)
    ]
    values = [10.0, None, 30.0]

    return TimeSeries('TEMP', '001', '12g', timestamps, values, 'C')


@pytest.fixture
def tmp_path():
    return Path()