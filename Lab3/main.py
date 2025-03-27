from task2 import task2
from task3 import task3



def main():
    # === TASK 2 ===================================================================

    print("\n=== TASK 2a: Reading logs ===")
    with open('data/http_first_100k.log') as f:
        log = task2.read_log(f)
        print(log)

    print("\n=== TASK 2b: Sorting logs by index ===")
    sorting_index = int(input("Enter log sorting index: "))
    print(sorting_index)
    sorted_log = task2.sort_log(log, sorting_index)
    print(sorted_log)

    print("\n=== TASK 2c: Get entries by address ===")
    desired_ip = input("Enter ip address you are looking for: ")
    print(desired_ip)
    entries_by_ip = task2.get_entries_by_addr(log, desired_ip)
    print(entries_by_ip)

    print("\n=== TASK 2d: Get entries by status code ===")
    desired_code = int(input("Enter code you are looking for: "))
    print(desired_code)
    entries_by_code = task2.get_entries_by_code(log, desired_code)
    print(entries_by_code)

    print("\n=== TASK 2e: Get failed reads ===")
    unmerged_failed_reads = task2.get_failed_reads(log)
    print(f'Unmerged: {unmerged_failed_reads}')
    merged_failed_reads = task2.get_failed_reads(log, True)
    print(f'Merged: {merged_failed_reads}')

    print("\n=== TASK 2f: Get entries by file extension ===")
    desired_extension = input("Enter extension you are looking for: ")
    print(desired_extension)
    entries_with_extension = task2.get_entries_by_extension(log, desired_extension)
    print(entries_with_extension)

    # === TASK 3 ===================================================================

    print("\n=== TASK 3a: Convert an entry to a dictionary ===")
    entry_index = int(input("Which entry do you want to convert to dictionary?: "))
    print(entry_index)
    entries_dict = task3.entry_to_dict(log[entry_index])
    print(entries_dict)

    print("\n=== TASK 3b: Convert log to a dictionary ===")
    log_dict = task3.log_to_dict(log)
    print(log_dict)

    print("\n=== TASK 3c: Show log info by host ===")
    task3.print_dict_entry_dates(log_dict)



if __name__ == '__main__':
    main()
