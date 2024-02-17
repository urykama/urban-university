# Создайте новую функцию def test_function
def test_function():
    # Создайте другую функцию внутри функции inner_function,
    def inner_function():
        # функция должна печатать значение "Я в области видимости функции test_function"
        print("Я в области видимости функции test_function")
    # Вызовите функцию inner_function внутри функции test_function
    print('вызов из внутри функции test_function()')
    inner_function()
    print('вызов из внутри функции test_function()')
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# inner_function()
try:
    print('вызов inner_function вне функции test_function()')
    inner_function()
    print('вызов inner_function вне функции test_function()')
except:
    print("  ошибка   ")
    print("  NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?   ")
    print("  NameError: имя 'inner_function' не определено. Вы имели в виду: 'test_function'?   ")
# PyCharm подчеркивает красным
# (Unresolved reference 'inner_function' --- Неразрешенная ссылка 'inner_function')
# наверно значит, что этой функции не видно отсюда

# Полученный код напишите в ответ к домашему заданию
test_function()