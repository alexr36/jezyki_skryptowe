from aux.aux_methods import extractSentences, extractWords


def countSentencesWithProperNames():
    proper_names_sentences = 0
    all_sentences = 0
    sentences = extractSentences()
        
    for sentence in sentences:
        words = extractWords(sentence)
        all_sentences += 1
                
        for word in words[1:]:
            if word[0].isupper():
                proper_names_sentences += 1
                break

    try:
        return proper_names_sentences / all_sentences * 100
    except ZeroDivisionError:
        return 0
    

def printCountSentences():
    print(f"{countSentencesWithProperNames():.2f}%")


if __name__ == '__main__':
    printCountSentences()    