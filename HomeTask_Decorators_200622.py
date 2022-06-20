import inspect
import os
import time

def log_file_maker(function):
    def _wrapper():
        data_list = []
        data_list.append(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
        data_list.append(f'{function.__name__}')
        data_list.append(inspect.signature(function))
        data_list.append(f'{function()}')
        with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
            for data in data_list:
                file.write(f'{data}\n')
    return _wrapper


@log_file_maker
def simple_function(name='Ivan', surname='Ivanov', specialty='student'):
    simple_text = f'Hello, {specialty} {surname}! Have a nice day for you, {name}!'
    return  simple_text


if __name__ == '__main__':
    simple_function()