from aux.aux_methods import extractSentences, extractWords

def findOrderedSentences():
    result_sentences = ''

    for sentence in extractSentences():
        words = extractWords(sentence)
        words_count = len(words)

        if len(words) < 2:
            continue

        if all(words[i] < words[i + 1] for i in range(words_count - 1)):
            result_sentences += sentence + '\n'

    return result_sentences


def printOrderedSetnences():
    print(findOrderedSentences())


if __name__ == '__main__':
    printOrderedSetnences()
    