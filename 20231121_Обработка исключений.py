def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'''Ошибка: невозможно преобразовать '{s}' в число 
        ValueError — это исключение в Python, которое возникает, 
            когда недопустимое значение присваивается переменной или передаётся функции при вызове.
        Вот несколько распространённых причин возникновения ValueError:
        — Invalid Argument;
        — Неправильное использование модуля Math;
        — Нераспаковка итерируемого объекта.'''


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'''Ошибка: файл '{filename}' не найден.'''
    except IOError:
        return f'''Ошибка: ввода/вывода при работе с файлом '{filename}'.'''


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return f'''Ошибка: деление на ноль.'''
    except TypeError:
        return f'''Ошибка: аргументы {a, b} должны быть числами .'''


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'''Ошибка: индекс "{index}" вне диапазона списка.'''
    except TypeError:
        return f'''Ошибка: индекс "{index}" должен быть целым числом.'''

# print(string_to_int('sd'))
# print(divide_numbers(5, 0))
# print(divide_numbers(b=0, a='5'))
# print(divide_numbers(5, '25'))
# print(access_list_element((23, '231', 'werw'), 3))
# print(access_list_element((23, '231', 'werw'), 1))
# print(access_list_element((23, '231', 'werw'), 0.5))
