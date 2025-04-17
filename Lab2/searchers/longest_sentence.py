from aux.aux_methods import extract_sentences, count_alphanumerals


def find_longest_sentence():
    longest_sentence = ''

    for sentence in extract_sentences():
        sentence = sentence.strip()

        if count_alphanumerals(sentence) > count_alphanumeralss(longest_sentence):
            longest_sentence = sentence

    return longest_sentence


def print_longest_sentence():
    print(find_longest_sentence())


if __name__ == '__main__':
    print_longest_sentence()
