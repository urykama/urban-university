# Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра
# со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a=1, b='строка', c=True):
    print('a =', a, '\t', 'b =', b, '\t', 'c =', c)
    print(f'a = {a}      b = {b}      c = {c}')
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('a =', a, '\t', 'b =', b, '\t', 'c =', c)



# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(5, 6, 7)
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])
#
# Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
values_list = [101, 'Word', True]
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = dict(a=4, b='словарь', c=False)
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
values_list_2 = ['E', True]
print_params(*values_list_2, 42)
