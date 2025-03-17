from aux.aux_methods import extractSentences


def findQuestionsOrExclamations():
    result_sentences = ''

    for sentence in extractSentences():
        if sentence.endswith('!') or sentence.endswith('?'):
            result_sentences += sentence + '\n'

    return result_sentences


def printQuestionsOrExclamations():
    print(findQuestionsOrExclamations())


if __name__ == '__main__':
    printQuestionsOrExclamations()