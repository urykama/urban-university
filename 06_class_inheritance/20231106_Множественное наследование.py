class Vehicle:  # Создайте родительский(базовый) класс Vehicle,
    vehicle_type = "none"  # который имеет свойство vehicle_type = "none"


class Car:  # Создайте родительский(базовый) класс Car,
    price = 1000000  # который имеет свойство price = 1000000

    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 'horse_powers', 104  # и функцию def horse_powers, возвращает количество лошидиных сил для автомобиля

class Nissan(Car, Vehicle):  # Создайте наследника класса Car и Vehicle - класс Nissan
    price = 250000  # и переопределите свойство price
    vehicle_type = 'sedan'  # и vehicle_type,
    def horse_powers(self):  # а также переопределите функцию horse_powers
        return 'horse_powers', 90
almera = Nissan()  # Создайте экзмепляр класса Nissan
print(almera.vehicle_type, almera.price)  # и распечайте через функцию print vehicle_type, price
