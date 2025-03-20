from aux.aux_methods import extractSentences, countAlphanumerals


def find4thQuartileSentences():
    result_sentences = ''
    sentences = list(extractSentences())
    
    if not sentences:
        return result_sentences

    sentences_lengths = sorted(countAlphanumerals(sentence.strip()) for sentence in sentences)
    sentences_count = len(sentences_lengths)

    q3_index = int(round(0.75 * sentences_count)) - 1
    q3_value = sentences_lengths[max(q3_index, 0)]

    for sentence in sentences:
        if countAlphanumerals(sentence) > q3_value:
            result_sentences += sentence + '\n'

    return result_sentences


def print4thQuartileSentences():
    print(find4thQuartileSentences())


if __name__ == '__main__':
    print4thQuartileSentences()        