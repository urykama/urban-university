class House:
    def __init__(self):
        self.name = 'Google'
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Текущее количество этажей', self.numberOfFloors)


home = House()
numberOfFloors = 10  # это просто местная переменная, сколько этажей строить
for i in range(1, numberOfFloors + 1):
    home.setNewNumberOfFloors(i)
    # тут типа дом строят

# Я просто делал по пунктам:
#
# Создал новый класс class House:
# Создал инициализатор для класса House,
#     который будет задавать атрибут этажности self.numberOfFloors = 0
# Создал функцию def setNewNumberOfFloors(floors),
#     которя изменяет атрибут numberOfFloors на параметр floors
#     и выводит в консоль numberOfFloors
#
# потом создал объект класса class House:
# потом вызвал метод объекта .setNewNumberOfFloors

# Вот в догонку...
# - Как вас зовут?
# Камалетдинов Урал Аданисович, он же Уралыч, Камазыч, Камаз, и т.п.
# - Сколько вам лет ?
# 2024 - июнь 1977 года выпуска = 46 лет
# - Из какого вы города?
# Уфа - город трёх шурупов - столица R&B (республика Башкортостан)
# - Чем увлекаетесь?
# мне всё надоело(тошнит от моей работы), алкоголь не употребляю, несколько раз бросал курить, грешен - играю в World Of Tanks
# - С какой целью пришли на курс?
# Возможно это моя очередная глупость, но я хотел-бы зайти в IT(почти любым разумным способом)
# - Был ли у вас ранее опыт работы в IT-сфере?
# 3 место на районной школьной олимпиаде по информатике (в 1993 или 1994 году)
# работал в 1C Первый Бит, не могу кодить на русском языке(там весь код на русском(можно по английски, но там так не принято))

# h1 = House()
# h2 = House()
# h1.setNewNumberOfFloors(5)
# h2.setNewNumberOfFloors(9)