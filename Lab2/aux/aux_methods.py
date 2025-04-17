import sys


def extract_sentences():
    sentence = ''
    paragraph_active = False
    last_char_was_space = False  

    for char in iter(lambda: sys.stdin.read(1), ''):
        if char.isspace():  
            if char == '\n':  
                if paragraph_active:  
                    yield sentence.strip()  
                    sentence = ''  
                    paragraph_active = False  

                last_char_was_space = False  
            else:
                if sentence and not last_char_was_space:  
                    sentence += ' '  
                    
                last_char_was_space = True  
            continue  

        paragraph_active = True  
        sentence += char  
        last_char_was_space = False  

        if char in '.!?':
            yield sentence.strip()
            sentence = ''

    if sentence:
        yield sentence.strip()


def extract_words(sentence):
    word = ''
    
    for char in sentence:
        if char.isalnum() or char in "-'":
            word += char
        elif word:
            yield word
            word = ''

    if word:
        yield word              


def count_generator_elements(gen):
    return sum(1 for _ in gen)


def count_alphanumerals(text):
    count = 0

    for char in text:
        if char.isalnum():
            count += 1

    return count        
