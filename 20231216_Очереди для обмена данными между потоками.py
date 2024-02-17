# Table - класс для столов, который будет содержать следующие атрибуты:
# number(int) - номер стола,
import threading


class Table():
    def __init__(self, number: int):
        self.number = number
        # is_busy(bool) - занят стол или нет.
        self.is_busy = True


# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
class Cafe():
    # Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
    def __init__(self, tables):
        pass

    # Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
    def customer_arrival(self):
        print('Посетитель номер <номер посетителя> прибыл.')
        pass

    # Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
    def serve_customer(self, customer):
        # Проверяет наличие свободных столов,
        for i in tables:
            print(i)
            # в случае наличия стола - начинает обслуживание посетителя (запуск потока),
            if i:
                print(f'Посетитель номер {customer} сел за стол {i}. (начало обслуживания)')
            # в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
            else:
                print(f'Посетитель номер {customer} ожидает свободный стол. (помещение в очередь)')
                pass

    # Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
    class Customer():
        pass

# Пример работы:
# # Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
#
# # Инициализируем кафе
cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()