from aux.aux_methods import extract_sentences, extract_words, count_alphanumerals


def find_longest_sentence_not_repeating_letters():
    longest_sentence = ''

    for sentence in extract_sentences():
        words = extract_words(sentence)

        try:
            prev_word = next(words)
        except StopIteration:
            continue

        found_repeated = False

        for word in words:
            if prev_word[0] == word[0]:
                found_repeated = True
                break
            
            prev_word = word

        if not found_repeated and count_alphanumerals(sentence) > count_alphanumerals(longest_sentence):
            longest_sentence = sentence

    return longest_sentence


def print_sentence():
    print(find_longest_sentence_not_repeating_letters())


if __name__ == '__main__':
    print_sentence()    
