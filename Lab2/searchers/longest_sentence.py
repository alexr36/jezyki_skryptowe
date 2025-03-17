from aux.aux_methods import extractSentences


def findLongestSentence():
    longest_sentence = ''
    sentences = extractSentences()

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence

    return longest_sentence


def printLongestSentence():
    print(findLongestSentence())


if __name__ == '__main__':
    printLongestSentence()