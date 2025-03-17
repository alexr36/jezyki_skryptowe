import sys


def countCharacters():
    symbols = 0

    for line in sys.stdin:
        for char in line:
            if not char.isspace():
                symbols += 1

    return symbols


def printCountCharacters():
    print(countCharacters())


if __name__ == '__main__':
    printCountCharacters()