from aux.aux_methods import extractSentences


def find4thQuartileSentences():
    sentences_lengths = {}
    result_sentences = ''
    sentences = extractSentences()
    sentences_count = 0
    
    for sentence in sentences:
        if sentence:
            sentences_count += 1
            length = len(sentence.strip())
            sentences_lengths[length] = sentences_lengths.get(length, 0) + 1

    if sentences_count == 0:
        return ''
    
    q3_index = int(round(0.75 * sentences_count))
    current_count = 0
    q3_value = 0

    for length in sorted(sentences_lengths):
        current_count += sentences_lengths[length]

        if current_count >= q3_index:
            q3_value = length
            break

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence and len(sentence) > q3_value:
            result_sentences += sentence + '\n'

    return result_sentences


def print4thQuartileSentences():
    print(find4thQuartileSentences())


if __name__ == '__main__':
    print4thQuartileSentences()        