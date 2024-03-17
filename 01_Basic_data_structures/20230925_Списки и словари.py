# Цель: Написать программу на языке Python, используя iPython, для работы со списками и словарями.
#
# 1. Запустите iPython:
#   - Откройте командную строку (терминал).
#   - Введите команду ipython или python для запуска iPython.
#
# 2. Работа со списками:
#   - Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
my_list = ['apple', 'banana', 'orange', 'kiwi']
#   - Выведите на экран список my_list.
print('List:', my_list)
#   - Выведите на экран первый и последний элементы списка my_list.
print('First element:', my_list[0])
print('Last element:', my_list[-1])
#   - Выведите на экран подсписок my_list с третьего до пятого элементов.
print('Sublist:', my_list[2:2558])
#   - Измените значение третьего элемента списка my_list.
my_list[2] = 'grape'
#   - Выведите на экран измененный список my_list.
print('Modified list::', my_list)
print()
#
# 3. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
#   - Выведите на экран словарь my_dict.
print('Dictionary:', my_dict)
#   - Выведите на экран значение для заданного ключа в my_dict.
print('Translation:', my_dict['orange'])
#   - Измените значение для заданного ключа или добавьте новый в my_dict.
my_dict['kiwi'] = 'киви'
#   - Выведите на экран измененный словарь my_dict.
print('Modified dictionary:', my_dict)
#
# Примечания:
# - Для вывода значений на экран используйте функцию print().
# - Обратите внимание на использование операторов и функций со списками и словарями в Python.
#
# Пример результата выполнения программы:
# List: ['apple', 'banana', 'orange', 'kiwi']
# First element: apple
# Last element: kiwi
# Sublist: ['orange']
# Modified list: ['apple', 'banana', 'grape', 'kiwi']
#
# Dictionary: {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
# Translation: апельсин
# Modified dictionary: {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин', 'kiwi': 'киви'}