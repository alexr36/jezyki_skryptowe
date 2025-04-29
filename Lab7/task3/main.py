from password_generator import PasswordGenerator



def main():
    pass_gen_next = PasswordGenerator(length=8, count=2)
    print(next(pass_gen_next))
    print(next(pass_gen_next))
    #print(next(pass_gen)) # This raises StopIteration exception if count=2

    print('-' * 16)

    pass_gen_for = PasswordGenerator(length=8)
    for password in pass_gen_for:
        print(password)



if __name__ == '__main__':
    main()