from task4.outlier_detector import OutlierDetector
from task4.zero_spike_detector import ZeroSpikeDetector
from task4.threshold_detector import ThresholdDetector
from .simple_reporter import SimpleReporter
from task5_6.measurements import Measurements



def get_example_series():
    path = "../data/measurements"
    measurements = Measurements(path)
    all_series = measurements._load_all()
    return all_series[0] if all_series else None



def run_tests():
    validators = [
        OutlierDetector(k=2),
        ZeroSpikeDetector(),
        ThresholdDetector(threshold=15.0),
        SimpleReporter()
    ]

    for validator in validators:
        print(f"### {validator.__class__.__name__} ###")

        for message in validator.analyze(get_example_series()):
            print(f"    - {message}")



if __name__ == '__main__':
    run_tests()