class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'barking "BARK-BARK"')
        else:
            print(self.name, 'barking "bark-bark"')

    def human_age(self):
        human_age = (self.age) * 7
        print('Вашей собаке',
              self.name,
              'сейчас',
              human_age,
              'по меркам людей')
    def __str__(self):
        return 'я собака по кличке ' + self.name

tuzik = Dog('Тузик ', 12, 38)
jackson = Dog('Джексон ', 9, 12)
tuzik.bark()
jackson.bark()
tuzik.human_age()
jackson.human_age()
print(tuzik)
print(jackson)
