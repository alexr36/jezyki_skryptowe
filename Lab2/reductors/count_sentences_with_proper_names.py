from aux.aux_methods import extract_sentences, extract_words


def count_sentences_with_proper_names():
    proper_names_sentences = 0
    all_sentences = 0
        
    for sentence in extract_sentences():
        words = extract_words(sentence)
                
        try:
            next(words)
        except StopIteration:
            continue 

        all_sentences += 1

        for word in words:
            if word[0].isupper():
                proper_names_sentences += 1
                break

    try:
        return proper_names_sentences / all_sentences * 100
    except ZeroDivisionError:
        return 0
    

def print_count_sentences():
    print(f"{count_sentences_with_proper_names():.2f}%")


if __name__ == '__main__':
    print_count_sentences()    
