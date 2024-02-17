class Building:  # Создайте новый класс Buiding
    total = 0  # с атрибутом total

    def __init__(self, num):  # Создайте инициализатор для класса Buiding,
        self.num = num
        Building.total += 1  # который будет увеличивать атрибут количества созданных объектов
        # класса Building total (по примеру класса Lemming из урока)


lemmings = []
for i in range(1, 41):  # В цикле создайте 40 объектов класса Building
    lemming = Building(i)
    lemmings.append(lemming)
    # print(lemming)  # и выведите их на экран командой print
    print('This is lemming number', lemming.num)
