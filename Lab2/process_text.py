import sys
from aux.aux_methods import printBuffer


def extractContents():
    printBuffer(processText())


def processText():
    buffer = []
    processPreamble()

    for line in sys.stdin:
        buffer.append(line.strip())

        if '-----' in line: 
            break 

    return buffer


def processPreamble():
    empty_lines_counter = 0

    for _ in range(10):
        line = sys.stdin.readline()

        if line == '\n':
            empty_lines_counter += 1
        else:
            empty_lines_counter = 0    

        if empty_lines_counter >= 2:
            break


if __name__ == '__main__': 
    extractContents()