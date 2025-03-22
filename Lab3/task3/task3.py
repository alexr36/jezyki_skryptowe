from collections import Counter



def entry_to_dict(entry):
    keys = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 
            'id.resp_h', 'id.resp_p', 'trans_depth', 
            'method', 'host', 'uri', 'referrer', 
            'user_agent', 'request_body_len', 
            'response_body_len', 'status_code', 
            'status_msg', 'info_code', 'info_msg', 
            'filename', 'tags', 'username', 
            'password', 'proxied', 'orig_fuids', 
            'orig_mime_types', 'resp_fuids', 'resp_mime_types']
    
    return dict(zip(keys, entry))



def log_to_dict(log):
    log_dict = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        uid = entry_dict.get('uid')

        if uid not in log_dict:
            log_dict[uid] = []

        log_dict[uid].append(entry_dict)    

    return log_dict    



def log_to_dict_alt(log):
    log_dict = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        ip = entry_dict.get('id.orig_h')

        if ip not in log_dict:
            log_dict[ip] = []

        log_dict[ip].append(entry_dict)    

    return log_dict    



def print_dict_entry_dates(log_dict):
    for uid, entries in log_dict.items():
        if not entries:
            continue

        # Collecting required data
        ips = set(e['id.orig_h'] for e in entries if 'id.orig_h' in e)
        methods = [e['method'] for e in entries if 'method' in e]
        status_codes = [str(e['status_code']) for e in entries if 'status_code' in e]
        timestamps = set(e['ts'] for e in entries if 'ts' in e)
        method_counter = Counter(methods)
        total_requests = len(entries)

        uids = set(e['uid'] for e in entries if 'uid' in e)

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



if __name__ == '__main__':
    entry_to_dict('dsad')    