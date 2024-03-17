class Building:  # Создайте новый класс Buiding
    total = 0  # с атрибутом total

    def __init__(self, num=13):  # Создайте инициализатор для класса Buiding,
        self.num = Building.total + 1
        Building.total += 1  # который будет увеличивать атрибут количества созданных объектов
        # класса Building total (по примеру класса Lemming из урока)


# lemmings = []
# for i in range(1, 41):  # В цикле создайте 40 объектов класса Building
while Building.total < 40:
    lemming = Building(13)
    # lemmings.append(lemming)
    # print(lemming)  # и выведите их на экран командой print
    print('This is lemming number', lemming.num)
