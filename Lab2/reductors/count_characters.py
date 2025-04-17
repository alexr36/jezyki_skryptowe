import sys


def count_characters():
    symbols = 0

    for line in sys.stdin:
        for char in line:
            if char.isalnum():
                symbols += 1

    return symbols


def print_count_characters():
    print(count_characters())


if __name__ == '__main__':
    print_count_characters()
