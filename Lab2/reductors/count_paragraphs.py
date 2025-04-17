import sys


def count_paragraphs():
    paragraphs = 0
    in_paragraph = False

    for line in sys.stdin:
        if line.strip():
            if not in_paragraph:
                paragraphs += 1

            in_paragraph = True
        else:
            in_paragraph = False        

    return paragraphs


def print_count_paragraphs():
    print(count_paragraphs())


if __name__ == '__main__':
    print_count_paragraphs()
