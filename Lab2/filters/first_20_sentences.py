from aux.aux_methods import extract_sentences, extract_words, count_generator_elements


def find_20_first_sentences():
    result_sentences = ''
    sentences_count = 0

    for sentence in extract_sentences():
        if count_generator_elements(extract_words(sentence)) < 2:
            continue

        if sentence:
            result_sentences += sentence + '\n'
            sentences_count += 1

        if (sentences_count >= 20):
            return result_sentences

    return result_sentences


if __name__ == '__main__':
    print(find_20_first_sentences())
