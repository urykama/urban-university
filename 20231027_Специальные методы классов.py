class House:
    def __init__(self):
        self.name = 'Google'
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Текущее количество этажей', self.numberOfFloors)


home = House()
numberOfFloors = 10  # это просто местная переменная
for i in range(1, numberOfFloors + 1):
    home.setNewNumberOfFloors(i)
    # тут типа дом строят
