# class House:
#     def __init__(self):
#         self.numberOfFloors = 0
#         print('создан объект с параметром self.numberOfFloors = ', self.numberOfFloors)
#
#     def setNewNumberOfFloors(self, floors):
#         print('я внутри метода setNewNumberOfFloors(floors)')
#         print('floors', floors)
#         # print('self.numberOfFloors', self.numberOfFloors)
#         print(self.numberOfFloors)
#         # for numberOfFloors in floors:
#         #     numberOfFloors += 1
#         #     print(House.setNewNumberOfFloors)
#         # return self.numberOfFloors
#
#
# dom = House()
# print(dom.setNewNumberOfFloors()


class House:
    def __init__(self):
        self.numberOfFloors = 0
        print('создан объект с параметром self.numberOfFloors = ', self.numberOfFloors)

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('я внутри метода setNewNumberOfFloors(floors)')
        print('floors', floors)
        print('self.numberOfFloors', self.numberOfFloors)

dom = House()
print(dom.setNewNumberOfFloors(21312))
a = []
print(a)
a = [1, 2, a]
print(a)
a = [1, 2, a]
print(a)


# Специальные методы классов
#
# Создайте новый класс House
#     Создайте инициализатор для класса House
#         который будет задавать атрибут этажности self.numberOfFloors = 0
#     Создайте метод setNewNumberOfFloors(floors),
#         который будет изменять атрибут numberOfFloors на параметр floors
#         и выводить в консоль numberOfFloors
# создайте объект класса House
# обратитесь к методу setNewNumberOfFloors(floors) класса House
#
# Полученный код напишите в ответ к домашему заданию