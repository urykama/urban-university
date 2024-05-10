class Building:  # Создайте новый класс Buiding
    total = 0  # с атрибутом total

    def __init__(self, num=13):  # Создайте инициализатор для класса Buiding,
        self.num = Building.total + 1
        Building.total += 1  # который будет увеличивать атрибут количества созданных объектов
        # класса Building total (по примеру класса Lemming из урока)


# lemmings = []
# for i in range(1, 41):  # В цикле создайте 40 объектов класса Building
while Building.total < 40:
    house = Building()
    print('This is House number', house.num)


# dom1 = Building()
# dom2 = Building()
# dom3 = Building()
# doma = [dom1, dom2, dom3]
# for i in doma:
#     print(i.total)
# print()
# dom1.total = 'Свой тотал'
# for i in doma:
#     print(i.total)
# print()
# Building.total = 'change total'
# for i in doma:
#     print(i.total)
