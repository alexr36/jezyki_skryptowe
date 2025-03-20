from aux.aux_methods import extractSentences, extractWords


def findSentencesWithConjunctions():
    result_sentences = ''

    for sentence in extractSentences():
        conjunctions_count = 0

        for word in extractWords(sentence):
            if isConjunction(word):
                conjunctions_count += 1

        if conjunctions_count >= 2:
                result_sentences += sentence + '\n'

    return result_sentences    


def isConjunction(word):
     return word == 'i' or word == 'oraz' or word == 'ale' or word == 'że' or word == 'lub'


def printSentencesWithConjunctions():
    print(findSentencesWithConjunctions())


if __name__ == '__main__':
    printSentencesWithConjunctions()    