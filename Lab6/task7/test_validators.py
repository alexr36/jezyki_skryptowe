from task4.outlier_detector import OutlierDetector
from task4.zero_spike_detector import ZeroSpikeDetector
from task4.threshold_detector import ThresholdDetector
from task5_6.measurements import Measurements


def run_tests():
    directory = '../data/measurements'
    measurements = Measurements(directory)
    validators = [
        OutlierDetector(k=3),
        ZeroSpikeDetector(),
        ThresholdDetector(threshold=100.0)
    ]

    anomalies = measurements.detect_all_anomalies(validators, preload=True)

    if not anomalies:
        print("No anomalies detected across all series")
        return
    
    print("\nDecected anomalies:\n")

    for series_id, messages in anomalies.items():
        print(f"{series_id}:")

        for message in messages:
            print(f"    - {message}")
    


if __name__ == '__main__':
    run_tests()