import json, datetime



def save_to_json(records, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False, default=str)



def show_dict(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")



def show_list(list):
    for elem in list:
        print(elem)



def str_to_date(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d')



def show_station(station):
    if station:
        print(f"{station['name']} - {station['address']}")
    else:
        print("No matching station found")



def show_stats(stats):
    if stats:
        avg, std = stats
        print(f"Average: {avg:.10f}")
        print(f"Standard deviation: {std:.10f}")
    else:
        print("No data")