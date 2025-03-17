from aux.aux_methods import extractSentences


def findSecondDegreeComplexSentence():
    result_sentence = ''
    sentences = extractSentences()
    commas = 0

    for sentence in sentences:
        for char in sentence:
            if char == ',':
                commas += 1

                if commas > 1:
                    result_sentence = sentence
                    return sentence

    return result_sentence


def printSentence():
    print(findSecondDegreeComplexSentence())


if __name__ == '__main__':
    printSentence()