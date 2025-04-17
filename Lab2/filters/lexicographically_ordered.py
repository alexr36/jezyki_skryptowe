from aux.aux_methods import extract_sentences, extract_words

def find_ordered_sentences():
    result_sentences = ''

    for sentence in extract_sentences():
        words_gen = extract_words(sentence)
        
        try:
            prev_word = next(words_gen)
        except StopIteration:
            continue  

        found_unordered = False

        for word in words_gen:
            if prev_word[0].lower() >= word[0].lower():
                found_unordered = True
                break  

            prev_word = word

        if not found_unordered:
            result_sentences += sentence + '\n'

    return result_sentences


def print_ordered_sentences():
    print(find_ordered_sentences())


if __name__ == '__main__':
    print_ordered_sentences()
    
