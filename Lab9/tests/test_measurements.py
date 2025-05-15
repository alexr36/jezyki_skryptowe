import pytest
from datetime                           import datetime
from tests.fixtures                     import tmp_path
from src.time_series                    import TimeSeries
from src.validators.outlier_detector    import OutlierDetector
from src.validators.threshold_detector  import ThresholdDetector
from src.validators.zero_spike_detector import ZeroSpikeDetector
from src.validators.simple_reporter     import SimpleReporter
from src.measurements                   import Measurements


# 4g)
@pytest.mark.parametrize('validator', [OutlierDetector(2.0), ThresholdDetector(50.0), ZeroSpikeDetector(), SimpleReporter()])
def test_detect_all_anomalies(validator, tmp_path):
    timestamps = [datetime(2023, 1, i + 1) for i in range(6)]
    values = [1.0, 0.0, 0.0, 0.0, 100.0, 5.0]  
    ts = TimeSeries('TEMP', 'XYZ', '24g', timestamps, values, 'C')
    measurements = Measurements(tmp_path)
    measurements._cache = {'test.csv': [ts]}
    anomalies = measurements.detect_all_anomalies(validators=[validator])

    assert isinstance(anomalies, dict)
    assert isinstance(anomalies["XYZ (TEMP)"], list)

   