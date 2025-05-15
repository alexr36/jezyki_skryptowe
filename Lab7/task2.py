from utils import *


# a)
def forall(pred, iterable):
    return all(map(pred, iterable))


# b)
def exists(pred, iterable):
    return any(map(pred, iterable))


# c)
def atleast(n, pred, iterable):
    if n < 0: return False
    return sum(map(pred, iterable)) >= n


# d)
def atmost(n, pred, iterable):
    if n < 0: return False
    return sum(map(pred, iterable)) <= n



def main():
    gen = letter_gen()
    is_even = lambda x: x % 2 == 0
    lst = [2, 4, 6, 7]

    print_subpoint(gen)
    print(forall(is_even, lst))

    print_subpoint(gen)
    print(exists(is_even, lst))

    print_subpoint(gen)
    print(atleast(3, is_even, lst))

    print_subpoint(gen)
    print(atmost(2, is_even, lst))



if __name__ == '__main__':
    main()
