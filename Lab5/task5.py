import argparse, random, logging
from task1 import parse_stations, parse_all_measurements
from statistics import mean, stdev
from utils import str_to_date, show_station, show_stats
from logger_setup import logger


def parse_args():
    parser = argparse.ArgumentParser(description="CLI for meteo stations' data analysis")
    parser.add_argument('--metric', required=True, help="Measured metric, i.e. PM2.5 or PM10")
    parser.add_argument('--freq', required=True, help="Measurement's frequency, i.e. 1g or 24g")
    parser.add_argument('--start', required=True, help="Beginning of the measured period (yyyy-mm-dd)")
    parser.add_argument('--end', required=True, help="End of the measured period (yyyy-mm-dd)")

    subparsers = parser.add_subparsers(dest='command', required=True)

    random_parser = subparsers.add_parser('random_station', help="Enter a random station")
    random_parser.set_defaults(func=handle_random_station)

    stats_parser = subparsers.add_parser('stats', help="Calculate average and standard deviation")
    stats_parser.add_argument('--station', required=True, help="Station's code, i.e. DsGlogWiStwo")

    return parser.parse_args()



def get_filtered_measurements(metric, freq, start, end, station=None):
    start_date = str_to_date(start)
    end_date = str_to_date(end)
    filtered = []

    for measurement in MEASUREMENTS:
        if (
            measurement['indicator'].upper() == metric.upper()
            and freq in measurement['station_id']
            and start_date <= measurement['datetime'] <= end_date
            and (station is None or measurement['station_code'] == station)
        ):
            filtered.append(measurement)

    if not filtered:
        logger.warning("No data matching given criteria found")

    return filtered



def handle_random_station(args):
    matching = get_filtered_measurements(args.metric, args.freq, args.start, args.end)

    if not matching:
        logger.warning("No measurements matching given parameters")
        return None
    
    chosen = random.choice(matching)
    station = next(
        (s for s in STATIONS if s['code'] == chosen['station_code']), 
        None
    )

    if not station:
        logger.warning("No station matching the measure found")
        return None
    
    return station



def handle_stats(args):
    matching = get_filtered_measurements(args.metric, args.freq, args.start, args.end, args.station)

    if not matching:
        logger.warning("No measurements matching given parameters")
        return None
    
    values = [m['value'] for m in matching]

    if len(values) < 2:
        logging.warning("Not enough values to compute standard deviation")
        return None

    avg = mean(values)
    std = stdev(values)

    return (avg, std)



def main():
    args = parse_args()

    global STATIONS, MEASUREMENTS

    STATIONS = parse_stations('data/stacje.csv')
    MEASUREMENTS = parse_all_measurements('data/measurements')

    if args.command == "random_station":
        station = handle_random_station(args)

        if station:
            show_station(station)
        else:
            print("No station's data found")

    elif args.command == "stats":
        stats = handle_stats(args)

        if stats:
            show_stats(stats)
        else:
            print("Not enough data for statistic calculations")



if __name__ == '__main__':
    main()





# python task5.py --metric "BjF(PM10)" --freq 24g --start 2023-01-01 --end 2023-01-08 stats --station DsOsieczow21
# python task5.py --metric PM10 --freq 1g --start 2023-01-01 --end 2023-01-31 random_station