import queue
import threading
import time


class Table():  # Table - класс для столов, который будет содержать следующие атрибуты:
    def __init__(self, number: int):
        self.number = number  # number(int) - номер стола,
        self.is_busy = True  # is_busy(bool) - занят стол или нет.


# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
class Customer(threading.Thread):
    def __init__(self, name, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.name = name
        self.table = ''

    def run(self):
        print(f'\033[33mПосетитель номер {self.name} сел за стол {self.table.number}. (начало обслуживания)', )
        time.sleep(1.5)
        print(f'\033[32mПосетитель номер {self.name} покушал и ушёл. (конец обслуживания)')
        self.table.is_busy = True
        cafe.serve_customer()


# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
class Cafe():
    def __init__(self, tables):
        # Атрибуты queue - очередь посетителей (создаётся внутри init),
        self.queue = queue.Queue(maxsize=3)
        # tables список столов (поступает из вне).
        self.tables = tables
        print('Создан объект Cafe')
        self.visitors = []

    # Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
    def customer_arrival(self):
        # print('Посетитель номер {i} прибыл.')
        for name in range(1, 21):
            time.sleep(0.3)
            customer = Customer(name=str(name), args=(self.queue,))
            visitors.append(customer)
            print(f'\033[36mПосетитель номер {customer.name} прибыл.')
            self.queue.put(customer)
            self.serve_customer()

    # Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
    def serve_customer(self):
        for table in self.tables:  # Проверяет наличие свободных столов,
            if table.is_busy:  # в случае наличия стола -
                table.is_busy = False
                customer = self.queue.get()
                customer.table = table
                customer.start()  # начинает обслуживание посетителя (запуск потока),
                return
            # в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
        print('\033[31mПосетитель номер {customer.name} ожидает свободный стол. (помещение в очередь)')


if __name__ == '__main__':
    # # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    # # Инициализируем кафе
    cafe = Cafe(tables)

    # # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    customer_arrival_thread.join()

    visitors = []
    print('\033[38mВсе гости прибыли')
    for visitor in visitors:
        print('\033[38mВсе гости прибыли', visitor.name, visitor)
        visitor.join()
    print('\033[38mочередь пуста')
    # # Ожидаем завершения работы прибытия посетителей

if __name__ == '__main__':
    queue = queue.Queue()
    # queue.put(1)
    pr_list = []
    for i in range(10):
        queue.put(i % 3)
        customer = Customer(name=str(i), args=(queue,))
        customer.table = i % 3
        # pr = queue.Process(target=get_text, args=(queue,))
        pr_list.append(customer)
        customer.start()

    for i in pr_list:
        i.join()
