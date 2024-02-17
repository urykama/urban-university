class Car:  # Создайте родительский(базовый) класс Car,
    price = 1000000  # который имеет свойство price = 1000000

    def horse_powers(self):  # и функцию def horse_powers,
        return 250  # которая возвращает количество лошидиных сил для автомобиля


class Nissan(Car):  # Создайте наследника класса Car - класс Nissan
    price = 200000  # и переопределите свойство price,

    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 'horse_powers', 88


class Kia(Car):  # Дополнительно создайте класс Kia, который также будет наследником класса Car
    price = 250000  # и переопределите свойство price,

    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 'horse_powers', 104


almera = Nissan()
print('Almera   \tprice', almera.price, '\t', almera.horse_powers())
rio = Kia()
print('Rio   \tprice', rio.price, '\t', rio.horse_powers())
