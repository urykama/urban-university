'''
Самостоятельная работа по уроку "Произвольное число параметров и HTML_DOM"
Для работы над домашнем заданием:
1. Создайте новый проект в PyCharm
Ваша задача в файле main.py:
Создайте новую функцию def test... с произвольным числом параметров разного типа,
функция должна распечатывать эти параметры внутри своего тела
'''


def test(*args, **kwargs):
    print(args, kwargs)


values_list = [101, 'Word', True]
values_dict = dict(a=4, b='словарь', c=False)
test(101, 'Word', True)
test(b=25, c=[1, 2, 3])
test(values_list)
test(values_dict)


# Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
def factorial(n):
    if n < 2:
        return n
    return n * factorial(n - 1)


for i in range(10):
    print('факториал числа ', i, 'равен =', factorial(i))
    # print(i, '! =', factorial(i))
# В ответ прикрепите получившийся файл main.py
