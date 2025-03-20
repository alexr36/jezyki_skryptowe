from aux.aux_methods import extractSentences, countAlphanumerals


def findLongestSentence():
    longest_sentence = ''

    for sentence in extractSentences():
        sentence = sentence.strip()

        if countAlphanumerals(sentence) > countAlphanumerals(longest_sentence):
            longest_sentence = sentence

    return longest_sentence


def printLongestSentence():
    print(findLongestSentence())


if __name__ == '__main__':
    printLongestSentence()