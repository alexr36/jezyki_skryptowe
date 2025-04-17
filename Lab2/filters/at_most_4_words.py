from aux.aux_methods import extract_sentences, extract_words, count_generator_elements


def find_sentences_with_at_most_words():
    result_sentences = ''
    
    for sentence in extract_sentences():
        if sentence and count_generator_elements(extract_words(sentence)) < 5:
            result_sentences += sentence + '\n'

    return result_sentences


def print_sentences_with_at_most_words():
    print(find_sentences_with_at_most_words())


if __name__ == '__main__':
    print_sentences_with_at_most_word()
