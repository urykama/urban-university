import queue
import threading
import time


class Table(threading.Thread):  # Table - класс для столов, который будет содержать следующие атрибуты:
    def __init__(self, number, queue: int, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.number = number  # number(int) - номер стола,
        self.queue = queue
        self.is_free = True  # is_busy(bool) - занят стол или нет.

    def run(self):
        while not self.queue.empty():
            customer = self.queue.get()
            self.is_free = False
            print(f'\033[33mПосетитель номер {customer.name} сел за стол {self.number}. (начало обслуживания)', )
            time.sleep(1.5)
            print(f'\033[32mПосетитель номер {customer.name} покушал и ушёл. (конец обслуживания)')
        self.is_free = True


class Customer():  # Customer - класс посетителя.
    def __init__(self, name: str):
        self.name = name


class Cafe():  # Cafe - класс для симуляции процессов в кафе.
    def __init__(self):  # Должен содержать следующие атрибуты и методы:
        self.queue = queue.Queue()  # Атрибуты queue - очередь посетителей (создаётся внутри init),
        self.tables = [Table(number=i, queue=self.queue) for i in range(1, 4)]
        #               tables список столов (поступает из вне) >-> создается при создании cafe
        print('Создан объект Cafe')

    def customer_arrival(self):  # Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
        for name in range(1, 21):
            print(f'\033[36mПосетитель номер {customer.name} прибыл.')
            customer = Customer(name=str(name))
            self.queue.put(customer)  # - посетитель поступает в очередь.
            self.serve_customer()
            time.sleep(0.3)

    # Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
    def serve_customer(self):
        for table in self.tables:  # Проверяет наличие свободных столов,
            if table.is_free:  # в случае наличия стола -
                table.start()  # начинает обслуживание посетителя (запуск потока),
                return
            # в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
        print('\033[31mПосетитель номер {customer.name} ожидает свободный стол. (помещение в очередь)')


if __name__ == '__main__':
    # # Инициализируем кафе
    cafe = Cafe()

    # # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    customer_arrival_thread.join()
