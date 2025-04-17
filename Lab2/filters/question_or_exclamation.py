from aux.aux_methods import extract_sentences


def find_questions_or_exclamations():
    result_sentences = ''

    for sentence in extract_sentences():
        if sentence.endswith('!') or sentence.endswith('?'):
            result_sentences += sentence + '\n'

    return result_sentences


def print_questions_or_exclamations():
    print(find_questions_or_exclamations())


if __name__ == '__main__':
    print_questions_or_exclamations()
