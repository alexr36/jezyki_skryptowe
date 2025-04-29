import logging, time
from functools import wraps
from datetime import datetime



def log(level=logging.INFO):
    def decorator(object):
        if isinstance(object, type):
            # If passed object is a (class) type,
            # wrap it's __init__ method, instantiate it and log info
            old_init = object.__init__

            @wraps(old_init)
            def new_init(self, *args, **kwargs):
                logging.log(
                    level, (
                        f"Instantiaging {object.__name__!r} "
                        f"with args={args}, kwargs={kwargs}"
                    )
                )
                old_init(self, *args, **kwargs)
            
            object.__init__ = new_init
            return object
        else:
            # If passed object is a function, wrap it, execute and log info
            func_name = object.__name__

            @wraps(object)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                logging.log(
                    level, (
                        f"Calling function {func_name!r} "
                        f"at: {datetime.fromtimestamp(start_time)} "
                        f"with args={args}, kwargs={kwargs}"
                    )
                )

                result = object(*args, **kwargs)
                end_time = time.time()
                logging.log(
                    level, (
                        f"Function {func_name!r} returned: {result!r} "
                        f"(Execution time: {end_time - start_time} seconds)"
                    )
                )

            return wrapper

    return decorator



@log(logging.DEBUG)
def add(a, b):
    return a + b



@log(logging.INFO)
class Example:
    def __init__(self, name):
        self.name = name



def main():
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    add(5, 7)
    Example("Alex")



if __name__ == '__main__':
    main()
