class House:
    def __init__(self):
        self.name = 'Google'

home = House()
home.numberOfFloors = 10
for i in range(1, home.numberOfFloors + 1):
    print('Текущий этаж равен', i)
