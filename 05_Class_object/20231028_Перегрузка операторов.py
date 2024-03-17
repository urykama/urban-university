class Building:

    def __init__(self, name='pers', numberOfFloors=1, buildingType='Халупа'):
        self.name = name
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    # def __eq__(self, other):
    #     if self.numberOfFloors == other.numberOfFloors:
    #         return self.buildingType == other.buildingType
    #     return False


homeNifNif = Building('NifNif', 0, 'Соломенный')
homeNafNaf = Building('NafNaf', 1, 'Деревянный')
homeNufNuf = Building('NufNuf', 2, 'Каменный')
homeBabaYaga = Building('BabaYaga', 1, 'Деревянный')
home_Daniil = Building('Daniil', 2, 'Каменный')
village = [homeNifNif, homeNafNaf, homeNufNuf, homeBabaYaga, home_Daniil]
for i in range(0, len(village) - 1):
    for j in range(i + 1, len(village)):
        if village[i] == village[j]:
            print('Похожие дома у', village[i].name, 'и', village[j].name)
