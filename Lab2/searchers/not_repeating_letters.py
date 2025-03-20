from aux.aux_methods import extractSentences, extractWords, countAlphanumerals


def findLongestSentenceNotRepeatingLetters():
    longest_sentence = ''

    for sentence in extractSentences():
        words = extractWords(sentence)

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

        if not found_repeated and countAlphanumerals(sentence) > countAlphanumerals(longest_sentence):
            longest_sentence = sentence

    return longest_sentence


def printSentence():
    print(findLongestSentenceNotRepeatingLetters())


if __name__ == '__main__':
    printSentence()    