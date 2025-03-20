from aux.aux_methods import extractSentences, extractWords, countGeneratorElements

def findOrderedSentences():
    result_sentences = ''

    for sentence in extractSentences():
        words_gen = extractWords(sentence)
        
        try:
            prev_word = next(words_gen)
        except StopIteration:
            continue  

        found_unordered = False

        for word in words_gen:
            if prev_word[0].lower() >= word[0].lower():
                found_unordered = True
                break  

            prev_word = word

        if not found_unordered:
            result_sentences += sentence + '\n'

    return result_sentences


def printOrderedSetnences():
    print(findOrderedSentences())


if __name__ == '__main__':
    printOrderedSetnences()
    