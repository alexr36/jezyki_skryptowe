from aux.aux_methods import extractSentences, extractWords, countGeneratorElements


def findSentencesWithAtMost4Words():
    result_sentences = ''
    
    for sentence in extractSentences():
        if sentence and countGeneratorElements(extractWords(sentence)) < 5:
            result_sentences += sentence + '\n'

    return result_sentences


def printSentencesWithAtMost4Words():
    print(findSentencesWithAtMost4Words())


if __name__ == '__main__':
    printSentencesWithAtMost4Words()