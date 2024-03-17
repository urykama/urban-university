class House:
    def __init__(self):
        self.name = 'Google'

home = House()
home.numberOfFloors = 10
for i in range(1, home.numberOfFloors + 1):
    print('Текущий этаж равен', i)

# нужно понять:
# переменные
# циклы (for, while)
# условные операторы (if, elif, else:)
# функции и вызов фунций
# классы создание классов и работа с ними

# range это не сложно, там только 3 параметра (начало, конец, с каким шагом)
# например:
# от 0 до 10 range(10)
# от 5 до 20 range(5, 20)
# от 5 до 20 c шагом 5 range(5, 20, 5)
for i in range(5, 20, 5):
    print(i)
