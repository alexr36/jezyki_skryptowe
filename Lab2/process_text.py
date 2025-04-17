import sys


def process_text():
    buffer = ''
    process_preamble()

    for line in sys.stdin:
        line = line.strip()

        if line.isspace():
            continue
        
        buffer += line + '\n'

        if '-----' in line: 
            break 

    return buffer


def process_preamble():
    empty_lines_counter = 0

    for _ in range(10):
        line = sys.stdin.readline()

        if line == '\n':
            empty_lines_counter += 1
        else:
            empty_lines_counter = 0    

        if empty_lines_counter >= 2:
            break


def extract_contents():
    print(process_text())


if __name__ == '__main__': 
    extract_contents()
