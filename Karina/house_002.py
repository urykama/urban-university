# Создайте новый класс House

# Создайте инициализатор для класса House,
# который будет задавать атрибут этажности self.numberOfFloors = 0

# Создайте метод setNewNumberOfFloors(floors),
# который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors

# Полученный код напишите в ответ к домашему заданию

class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


home = House()
# home.setNewNumberOfFloors(1)
for i in range(1, 6):
    home.setNewNumberOfFloors(i)