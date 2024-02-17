# def greet_person(person_name):
#
#     if person_name == 'Robert':
#         raise BaseException("We don't like you, Robert")
#     print(f'Hi there {person_name}')
# greet_person('Dolly')
# greet_person('Robert')

# переброс исключений
# try:
#     raise NameError("Привет там")
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо! Его параметры {exc.args}')
#     raise

# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
#     Например, InvalidDataException (Исключение недопустимых данных) и ProcessingException (Исключение при обработке).
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте
class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def check_age(age):
    try:
        if not 1 < int(age) < 110:
            raise InvalidDataException("Некорректный возраст")
        return "Ваш возраст:", age
    except ValueError as ve:
        return (f"Введены некорректные данные {ve}")
    except InvalidDataException as e:
        print(f'Сработало исключение {e}')
        return (f"{age} - Некорректный возраст")
    else:
        print(f'Сработало исключение ProcessingException')
        raise ProcessingException('Значение а - строка')
        return ("Введены некорректные данные")
        # raise
    # else:
    #     return ("Непредвиденная ситуация, ФОРС-МАЖОР")
    finally:
        print('Выходим из функции')
        print()


print(check_age(50))
print(check_age(100))
print(check_age(200))
print(check_age(0))
print(check_age('0'))
print(check_age('fifty'))

# подсказка

# def funkcia(a):
#     try:
#         print(a)
#     except InvalidDataException as e:
#         print(f'Сработало исключение {e}')
#         raise InvalidDataException('Значение а - число')
#     else:
#         raise ProcessingException('Значение а - строка')
#     finally:
#         print('Закончили функцию')
#
#
# funkcia('3')
# funkcia(3)
