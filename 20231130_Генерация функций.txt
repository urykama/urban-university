# Фабрика функций для сложения, вычитания, умножения, деления, :
def create_operation(operation):
    if operation == "add" or operation == "+":
        def add(x, y):
            return x + y
        return add  # возвращаем функцию, как объект!! Тут скобки не нужны
    elif operation == "subtract" or operation == '-':
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == "multiplication" or operation == '*':
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "division" or operation == '/':
        def division(x, y):
            if y == 0:
                return 'Error: Division by zero'
            return x / y
        return division


print('Задача 1: Фабрика функций')
my_func_add = create_operation("add")
my_func_subtract = create_operation("subtract")
my_func_multiplication = create_operation("multiplication")
my_func_division = create_operation("division")
print('my_func_add(31, 5) =', my_func_add(31, 5))
print('my_func_subtract(108, 72) =', my_func_subtract(108, 72))
print('my_func_multiplication(6, 6) =', my_func_multiplication(6, 6))
print('my_func_division(72, 2) =', my_func_division(72, 2))
print('my_func_division(72, 0) =', my_func_division(72, 0))

# Пример лямбда функции с аналогом через def
multiply = lambda x, y: x * y
squaring = lambda x: x ** 2

print('Задача 2: лямбда')
print('multiply(2, 3) =', multiply(2, 3))  # Выводит 6
print('squaring(16) =', squaring(16))  # Выводит 256


def multiply_def(x, y):
    return x * y
def squaring_def(x):
    return x ** 2

print(multiply_def(2, 3))  # Выводит 6
print(squaring_def(16))  # Выводит 256


# Пример создания вызываемого объекта
class Repeater:
    def __init__(self, value):
        self.value = value

    def __call__(self, n):
        return [self.value] * n

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

repeat_five = Repeater(5)
areaOfRectangle = Rect(2, 4)
print('Задача 3: Вызываемые oбъекты')
print(repeat_five(3))  # Выводит [5, 5, 5]
print(areaOfRectangle())  # Выводит 8

# Пример вывода программы
# Задача 1: Фабрика функций
# 6
# 2.0
# Error: Division by zero
# Задача 2 лямбда
# 16
# 16
# Задача 3: Вызываемые oбъекты
# Стороны: 2, 4
# Площадь: 8
