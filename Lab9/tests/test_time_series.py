import pytest
from tests.fixtures import time_series_sample, time_series_w_none_sample
from datetime       import date

# -- 4b) -----------------------------------------------------------------------

# i.
def test_time_series_get_by_index(time_series_sample):
    assert time_series_sample[0] == (time_series_sample.timestamps[0], 10.0)

# ii.
def test_time_series_get_by_slice(time_series_sample):
    assert len(time_series_sample[:2]) == 2

# iii.
def test_time_series_get_by_existing_date(time_series_sample):
    assert [20.0] == time_series_sample[date(2025, 1, 2)]

# iv.
def test_time_series_get_by_missing_date(time_series_sample):
    with pytest.raises(KeyError):
        _ = time_series_sample[date(2025, 1, 4)]


# -- 4c) -----------------------------------------------------------------------

# i.
def test_time_series_mean_stddev_complete(time_series_sample):
    assert time_series_sample.mean == 20.0
    assert round(time_series_sample.stddev, 5) ==  8.16497

# ii.
def test_time_series_mean_stddev_incomplete(time_series_w_none_sample):
    assert time_series_w_none_sample.mean == 20.0
    assert round(time_series_w_none_sample.stddev, 5) == 10.0
