import os
import time
import datetime

def log_file_maker(function):
    def _wrapper():
        pass
    return _wrapper


@log_file_maker
def simple_function():
    print("Hello, World!")


if __name__ == '__main__':
    # log_file_maker(simple_function)
    simple_function()