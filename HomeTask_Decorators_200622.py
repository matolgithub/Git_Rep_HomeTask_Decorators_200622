import inspect
import os
import time

# задание №1
# создание декоратора по заданию №1
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

# применение декоратора по заданию №1
@log_file_maker
def simple_function(name='Ivan', surname='Ivanov', specialty='student'):
    simple_text = f'Hello, {specialty} {surname}! Have a nice day for you, {name}!'
    return  simple_text


# задание №2
# создание параметрического декоратора по заданию №2
def file_path_maker(folder_path):
    def log_file_maker(function):
        def _wrapper():
            data_list = []
            data_list.append(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
            data_list.append(f'{function.__name__}')
            data_list.append(inspect.signature(function))
            data_list.append(f'{function()}')
            current_path = os.getcwd()
            if not os.path.exists(f'{current_path}{folder_path}'):
                os.makedirs(f'{current_path}{folder_path}')
            os.chdir(f'{current_path}{folder_path}')
            with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
                for data in data_list:
                    file.write(f'{data}\n')
        return _wrapper
    return log_file_maker

# применение параметрического декоратора по заданию №2
@file_path_maker('\log')
def other_function(name='Sergey', surname='Sidorov', age='25'):
    other_text = f'Hello, {name} {surname}! {age} - You are so young!'
    return  other_text


if __name__ == '__main__':
    # simple_function()
    other_function()