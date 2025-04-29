from functools import lru_cache


# Task 4
def make_generator(func):
    def generator():
        n = 1

        while True:
            yield func(n)
            n += 1

    return generator()


# Task 5
def make_generator_mem(func):
    memoized_func = lru_cache(maxsize=None)(func)
    return make_generator(memoized_func)


# -- Fibonacci sequence and Catalan numbers ------------------------------------

def fibonacci(n):
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# c_n = c_(n-1) * 2(2n-1)/(n+1)
def catalan(n):
    if n == 0:
        return 1
    
    return catalan(n - 1) * 2 * (2 * n - 1) // (n + 1)


# -- Custom sequences ----------------------------------------------------------

# a_n = 3n + 5
series_arithmetic = lambda n: 3 * n + 5

# a_n = 2 * 3^n
series_geometric = lambda n: 2 * 3**n

# a_n = n^2 + 2n + 1
series_power = lambda n: n**2 + 2*n + 1 



def generate(generator, count):
    for _ in range(count):
        print(next(generator))



def demonstrate_gen(generator, count, name):
    print(f"-- {name} --------")
    generate(generator, count)
    print()



def show_task_4(count):
    print("########### TASK 4 ###########")
    fibonacci_gen = make_generator(fibonacci)
    demonstrate_gen(fibonacci_gen, count, 'Fibonacci sequence')

    catalan_gen = make_generator(catalan)
    demonstrate_gen(catalan_gen, count, 'Catalan numbers')

    arithmetic_gen = make_generator(series_arithmetic)
    demonstrate_gen(arithmetic_gen, count, 'Arithmetic series')

    geometric_gen = make_generator(series_geometric)
    demonstrate_gen(geometric_gen, count, 'Geometric series')

    power_gen = make_generator(series_power)
    demonstrate_gen(power_gen, count, 'Power series')   



def show_task_5(count):
    print("########### TASK 5 ###########")
    fibonacci_gen = make_generator_mem(fibonacci)
    demonstrate_gen(fibonacci_gen, count, 'Fibonacci sequence')

    catalan_gen = make_generator_mem(catalan)
    demonstrate_gen(catalan_gen, count, 'Catalan numbers')

    arithmetic_gen = make_generator_mem(series_arithmetic)
    demonstrate_gen(arithmetic_gen, count, 'Arithmetic series')

    geometric_gen = make_generator_mem(series_geometric)
    demonstrate_gen(geometric_gen, count, 'Geometric series')

    power_gen = make_generator_mem(series_power)
    demonstrate_gen(power_gen, count, 'Power series')   


def main():
    count = 10
    show_task_4(count)
    show_task_5(count)
    



if __name__ == '__main__':
    main()