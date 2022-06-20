import os
import time
import datetime

def log_file_maker(function):
    def _wrapper():
        data_list = []
        data_list.append(datetime.date.today())
        data_list.append(time.time())
        data_list.append(f'{function}')
        with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
            for data in data_list:
                file.write(f'{data}\n')
            print(data_list)
    return _wrapper


@log_file_maker
def simple_function(name='OLEG'):
    simple_text = f'Have a nice day, {name}!'
    print(simple_text)
    return  simple_text


if __name__ == '__main__':
    simple_function()