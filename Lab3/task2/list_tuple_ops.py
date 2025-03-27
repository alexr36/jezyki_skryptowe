import sys, datetime, ipaddress



def read_log(source = sys.stdin):
    record_tuples = []

    for i, line in enumerate(source):
        if not line.strip():
            continue

        fields = line.strip().split('\t')

        # Converting fields to appropriate datatypes
        try:
            fields[0] = datetime.datetime.fromtimestamp((float(fields[0])))
            fields[3] = int(fields[3])
            fields[5] = int(fields[5])
            fields[6] = int(fields[6])

            if fields[14].isdigit():
                fields[14] = int(fields[14])
        except (ValueError, IndexError):
            print(f"Conversion error in line {i + 1}.") 

        record_tuples.append(tuple(fields))    

    return record_tuples    



def sort_log(log, index):
    try:
        return sorted(log, key = lambda entry: entry[index])
    except (IndexError, TypeError):
        return log
    


def get_entries_by_addr(log, addr):
    # Inner method for validating given address
    def is_valid_ip(ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    entries = []

    # Collecting entries with given address
    if is_valid_ip(addr):
        for record in log:
            if addr in record:
                entries.append(record) 

    return entries            



def get_entries_by_code(log, code):
    # Determining if the code is OK
    entries = []

    # Collecting entries with given code
    if isinstance(code, int):
        for record in log:
            if record[14] == code:
                entries.append(record)

    return entries            



def get_failed_reads(log, merge = False):
    list_of_4xx = []
    list_of_5xx = []

    for record in log:
        code = str(record[14])

        if not code.isdigit():
            continue

        # Determining if the code is OK
        if len(code) == 3:
            if code.startswith('4'):
                list_of_4xx.append(record)
            elif code.startswith('5'):
                list_of_5xx.append(record)

    # Returning result in appropriate form
    if merge:
        return list_of_4xx + list_of_5xx
    else:
        return (list_of_4xx, list_of_5xx) 
    


def get_entries_by_extension(log, extension):
    entries = []

    for record in log:
        for field in record:
            # Checking if current field is valid
            if isinstance(field, str) and field.lower().endswith(f'.{extension.lower()}'):
                entries.append(record)
                break

    return entries        
  


if __name__ == '__main__':
    print(read_log())