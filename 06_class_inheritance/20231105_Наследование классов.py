class Car:  # Создайте родительский(базовый) класс Car,
    price = 1000000  # который имеет свойство price = 1000000

    def horse_powers(self):  # и функцию def horse_powers,
        return 250  # которая возвращает количество лошидиных сил для автомобиля

    def __str__(self, price=None):
        return 'price = ' + str(self.price) + '\t\thorse_powers = ' + str(self.horse_powers())


class Nissan(Car):  # Создайте наследника класса Car - класс Nissan
    price = 200000  # и переопределите свойство price,

    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 88


class Kia(Car):  # Дополнительно создайте класс Kia, который также будет наследником класса Car
    price = 250000  # и переопределите свойство price,

    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 104


almera = Nissan()
print('Almera   \tprice', almera.price, '\t', almera.horse_powers())
rio = Kia()
print('Rio   \tprice', rio.price, '\t', rio.horse_powers())

print(almera)
print(rio)

# дополнения к Домашнее задание по теме "Наследование классов":
# 1) создайте объекты классов Nissan и Kia.
# 2) выведите в консоль (на экран): атрибуты (свойства) и результаты работы методов (функций) созданных объектов.
