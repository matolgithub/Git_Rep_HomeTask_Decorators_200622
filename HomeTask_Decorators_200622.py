import inspect
import os
import time

# задание №1
# создание декоратора по заданию №1
def log_file_maker(function):
    def new_function(*args, **kwargs):
        sum_res = function(*args, **kwargs)
        data_list = []
        data_list.append(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
        data_list.append(f'{function.__name__}')
        data_list.append(inspect.signature(function))
        data_list.append(f'{function(*args, **kwargs)}')
        with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
            for data in data_list:
                file.write(f'{data}\n')
        return sum_res
    return new_function

# применение декоратора по заданию №1
@log_file_maker
def summator_1(x, y):
    return x + y


# задание №2
# создание параметрического декоратора по заданию №2
def file_path_maker(folder_path):
    def log_file_maker(function):
        current_path = os.getcwd()
        if not os.path.exists(f'{current_path}{folder_path}'):
            os.makedirs(f'{current_path}{folder_path}')
        os.chdir(f'{current_path}{folder_path}')
        def new_function(*args, **kwargs):
            data_list = []
            sum_res = function(*args, **kwargs)
            data_list.append(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))
            data_list.append(f'{function.__name__}')
            data_list.append(inspect.signature(function))
            data_list.append(f'{function(*args, **kwargs)}')
            with open('home_task_logfile.log', 'w', encoding='utf-8') as file:
                for data in data_list:
                    file.write(f'{data}\n')
            return sum_res
        return new_function
    return log_file_maker

# применение параметрического декоратора по заданию №2
@file_path_maker('\log')
def summator_2(x, y):
    return x + y


if __name__ == '__main__':
    three = summator_2(1, 2)
    five = summator_2(2, 3)
    result = summator_2(three, five)
    print('result: ', result)
    print('result type: ', type(result))