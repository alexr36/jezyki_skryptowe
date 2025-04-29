import string, random


class PasswordGenerator:
    def __init__(self, length, charset=string.ascii_letters+string.digits, count=10):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated = 0
        


    def __iter__(self):
        '''Returns new iterator'''
        return self



    def __next__(self):
        '''Returns new randomly generated password'''
        if self.generated >= self.count:
            raise StopIteration
        
        password = ''.join((random.choice(self.charset)) for _ in range(self.length))
        self.generated += 1
        return password
    

