from aux.aux_methods import extractSentences, countAlphanumerals


def find_4th_quartile_sentences():
    result_sentences = ''
    sentences = list(extract_sentences())
    
    if not sentences:
        return result_sentences

    sentences_lengths = sorted(count_alphanumerals(sentence.strip()) for sentence in sentences)
    sentences_count = len(sentences_lengths)

    q3_index = int(round(0.75 * sentences_count)) - 1
    q3_value = sentences_lengths[max(q3_index, 0)]

    for sentence in sentences:
        if count_alphanumerals(sentence) > q3_value:
            result_sentences += sentence + '\n'

    return result_sentences


def print_4th_quartile_sentences():
    print(find_4th_quartile_sentences())


if __name__ == '__main__':
    print_4th_quartile_sentences()        
