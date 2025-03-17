from aux.aux_methods import extractSentences, extractWords


def findSentencesWithConjunctions():
    conjunctions = ['i', 'oraz', 'ale', 'że', 'lub']
    result_sentences = ''

    for sentence in extractSentences():
        conjunctions_count = 0

        for word in extractWords(sentence):
            if word in conjunctions:
                conjunctions_count += 1

        if conjunctions_count >= 2:
                result_sentences += sentence + '\n'

    return result_sentences    


def printSentencesWithConjunctions():
    print(findSentencesWithConjunctions())


if __name__ == '__main__':
    printSentencesWithConjunctions()    