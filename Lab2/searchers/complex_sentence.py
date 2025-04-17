from aux.aux_methods import extract_sentences


def find_second_degree_complex_sentence():
    result_sentence = ''
    commas = 0

    for sentence in extract_sentences():
        for char in sentence:
            if char == ',':
                commas += 1

                if commas > 1:
                    result_sentence = sentence
                    return sentence

    return result_sentence


def print_sentence():
    print(find_second_degree_complex_sentence())


if __name__ == '__main__':
    print_sentence()
