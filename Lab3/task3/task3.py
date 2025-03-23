from collections import Counter
import constant_fieldnames as cf


def entry_to_dict(entry):
    keys = cf.ALL_FIELDNAMES
    return dict(zip(keys, entry))



def log_to_dict(log):
    log_dict = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        uid = entry_dict.get(cf.UID)

        if uid not in log_dict:
            log_dict[uid] = []

        log_dict[uid].append(entry_dict)    

    return log_dict    



def log_to_dict_alt(log):
    log_dict = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        ip = entry_dict.get(cf.ID_ORIG_H)

        if ip not in log_dict:
            log_dict[ip] = []

        log_dict[ip].append(entry_dict)    

    return log_dict    



def print_dict_entry_dates(log_dict):
    for uid, entries in log_dict.items():
        if not entries:
            continue

        # Collecting required data
        ips = set(e[cf.ID_ORIG_H] for e in entries if cf.ID_ORIG_H in e)
        methods = [e[cf.METHOD] for e in entries if cf.METHOD in e]
        status_codes = [str(e[cf.STATUS_CODE]) for e in entries if cf.STATUS_CODE in e]
        timestamps = set(e[cf.TS] for e in entries if cf.TS in e)
        method_counter = Counter(methods)
        total_requests = len(entries)

        uids = set(e[cf.UID] for e in entries if cf.UID in e)

        # Printing info about host's requests
        print(f"\nUID: {', '.join(uids)}")  # Shouldn't it be it?

       #print(f"\nUID: {uid}") # Instead of this
        print(f"Hosts/IPs: {', '.join(ips)}")
        print(f"Requests number: {total_requests}")

        # Printing info about first and last request
        if timestamps:
            print(f"First request: {min(timestamps)}, Latest request: {max(timestamps)}")

        # Printing info about share of methods
        print("Share of methods:")
        for method, count in method_counter.items():
            percent = (count / total_requests) * 100
            print(f"    - {method}: {percent:.2f}%")    

        # Printing info about the 2xx requests ratio
        count_2xx = sum(1 for code in status_codes if code.startswith('2'))
        ratio = count_2xx / total_requests * 100
        print(f"2xx requests: {count_2xx}/{total_requests} ({ratio:.2f}%)")
   