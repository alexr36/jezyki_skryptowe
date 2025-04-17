from aux.aux_methods import extract_sentences, extract_words


def find_sentences_with_conjunctions():
    result_sentences = ''

    for sentence in extract_sentences():
        conjunctions_count = 0

        for word in extract_words(sentence):
            if is_conjunction(word):
                conjunctions_count += 1

        if conjunctions_count >= 2:
                result_sentences += sentence + '\n'

    return result_sentences    


def is_conjunction(word):
     return word == 'i' or word == 'oraz' or word == 'ale' or word == 'że' or word == 'lub'


def print_sentences_with_conjunctions():
    print(find_sentences_with_conjunctions())


if __name__ == '__main__':
    print_sentences_with_conjunctions()    
