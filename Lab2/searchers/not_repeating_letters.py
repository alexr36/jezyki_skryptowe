from aux.aux_methods import extractSentences, extractWords


def findLongestSentenceNotRepeatingLetters():
    longest_sentence = ''

    for sentence in extractSentences():
        words = extractWords(sentence)
        words_count = len(words)

        if words_count > 1 and all(
            words[i][0] != words[i + 1][0] for i in range(words_count - 1)
        ):
            if len(longest_sentence) < len(sentence):
                longest_sentence = sentence

    return longest_sentence


def printSentence():
    print(findLongestSentenceNotRepeatingLetters())


if __name__ == '__main__':
    printSentence()    