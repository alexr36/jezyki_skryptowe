import sys


def extractSentences():
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


def extractWords(sentence):
    return sentence.split()


def printBuffer(buffer):
    for elem in buffer:
        print(elem)