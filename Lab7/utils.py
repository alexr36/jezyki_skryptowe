import string



def letter_gen():
    '''Yields next letter in ascii_letters sequence'''
    for letter in string.ascii_letters:
        yield letter



def print_subpoint(gen):
    print(f"\n-- {gen.__next__()}) ------")
