from src.validators.outlier_detector    import OutlierDetector
from src.validators.threshold_detector  import ThresholdDetector
from src.validators.zero_spike_detector import ZeroSpikeDetector
from src.time_series                    import TimeSeries
from datetime                           import datetime


# 4d)
def test_outlier_detector():
    ts = TimeSeries(
        indic      = 'TEMP',
        code       = '001',
        avg_time   = '24g',
        timestamps = [datetime(2025, 1, i + 1) for i in range(4)], 
        values     = [10, 10, 10, 100], 
        unit       = 'C'
    )
    detector = OutlierDetector(1.5)
    assert any('outlier' in msg.lower() for msg in detector.analyze(ts))

# 4e)
def test_zero_spike_detector():
    ts = TimeSeries('TEMP', '001', '24g', [datetime(2025, 1, i + 1) for i in range(5)], [1, 0, 0, 0, 5], 'C')
    detector = ZeroSpikeDetector()
    assert any('zero' in msg.lower() for msg in detector.analyze(ts))

# 4f)
def test_threshold_detector():
    ts = TimeSeries('TEMP', '001', '24g', [datetime(2025, 1, i + 1) for i in range(3)], [2, 20, 50], 'C')
    detector = ThresholdDetector(30.0)
    assert any('threshold' in msg.lower() for msg in detector.analyze(ts))
