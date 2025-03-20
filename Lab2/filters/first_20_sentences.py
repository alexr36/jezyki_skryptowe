from aux.aux_methods import extractSentences, extractWords, countGeneratorElements


def find20FirstSentences():
    result_sentences = ''
    sentences_count = 0

    for sentence in extractSentences():
        if countGeneratorElements(extractWords(sentence)) < 2:
            continue

        if sentence:
            result_sentences += sentence + '\n'
            sentences_count += 1

        if (sentences_count >= 20):
            return result_sentences

    return result_sentences


if __name__ == '__main__':
    print(find20FirstSentences())