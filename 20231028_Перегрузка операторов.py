class Buiding:

    def __init__(self, name='pers', numberOfFloors=1, buildingType='Халупа'):
        self.name = name
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


homeNifNif = Buiding('NifNif', 0, 'Соломенный')
homeNafNaf = Buiding('NafNaf', 1, 'Деревянный')
homeNufNuf = Buiding('NufNuf', 2, 'Каменный')
homeBabaYaga = Buiding('BabaYaga', 1, 'Деревянный')
homeHuman = Buiding('Human', 2, 'Каменный')
village = [homeNifNif, homeNafNaf, homeNufNuf, homeBabaYaga, homeHuman]
for i in range(0, len(village) - 1):
    for j in range(i + 1, len(village)):
        # print(i, j)
        if village[i] == village[j]:
            print('Похожие дома у', village[i].name, 'и', village[j].name)
