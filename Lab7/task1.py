from utils import *


# a)
def acronym(words):
    return ''.join(map(lambda word: word[0].upper(), words))


# b)
def median(numbers):
    sorted_numbers = sorted(numbers)
    numbers_count = len(numbers)
    index_mid = numbers_count // 2

    return (
        (sorted_numbers[index_mid - 1] + sorted_numbers[index_mid]) / 2
        if numbers_count % 2 == 0
        else sorted_numbers[index_mid]
    )


# c)
def square_root(x, epsilon=1e-10):
    def is_ok(y):
        # y >= 0 AND |y^2 - x| < epsilon
        return y >= 0 and abs(y**2 - x) < epsilon
    
    def improve(y):
        # y = (y + x/y) / 2 
        return (y + x / y) / 2
    
    def next_iter(y):
        return y if is_ok(y) else next_iter(improve(y))

    return next_iter(x if x >= 1 else 1.0)


# d)
def make_alpha_dict(text):
    words = text.split()
    chars = sorted(set(filter(str.isalpha, text)), reverse=True)

    return {
        char: [
            word for word in words 
            if char in word
        ] 
        for char in chars
    }


# e)
def flatten(sequence):
    def is_sequence(elem):
        return isinstance(elem, (list, tuple))

    return [
        item
        for elem in sequence
        for item in (flatten(elem) if is_sequence(elem) else [elem])
    ]



def main():
    gen = letter_gen()

    print_subpoint(gen)
    print(acronym(['Zaklad', 'Ubezpieczen', 'Spolecznych']))

    print_subpoint(gen)
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))

    print_subpoint(gen)
    print(square_root(3, 0.1))

    print_subpoint(gen)
    print(make_alpha_dict("on i ona"))

    print_subpoint(gen)
    print(flatten([1, [2, 3], [[4, 5], 6]]))


if __name__ == '__main__':
    main()
