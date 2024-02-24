import queue
import threading
import time

customers = []


class Table():  # Table - класс для столов, который будет содержать следующие атрибуты:
    def __init__(self, number: int):
        self.number = number  # number(int) - номер стола,
        self.is_free = True  # is_busy(bool) - занят стол или нет.
        # переименовано в is_free - свободен, чтобы отказаться от конструкции <if not table.is_busy:>


class Customer(threading.Thread):  # Customer - класс (поток) посетителя.
    def __init__(self, name, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.name = name
        self.table = None

    def run(self):
        print(f'\033[33mПосетитель номер {self.name} сел за стол {self.table.number}. (начало обслуживания)', )
        time.sleep(1.5)
        print(f'\033[32mПосетитель номер {self.name} покушал и ушёл. (конец обслуживания)')
        self.table.is_free = True
        cafe.serve_customer()


class Cafe():  # Cafe - класс для симуляции процессов в кафе.
    def __init__(self, tables):  # Должен содержать следующие атрибуты и методы:
        # self.queue = queue.Queue(maxsize=3)
        self.queue = queue.Queue()  # Атрибуты queue - очередь посетителей (создаётся внутри init),
        self.tables = tables  # tables список столов (поступает из вне).
        print('Создан объект Cafe')
        self.customers = []

    def customer_arrival(self):  # Метод customer_arrival(self) - моделирует прибытие посетителя(каждую секунду).
        for name in range(1, 21):
            time.sleep(0.3)
            customer = Customer(name=str(name))
            self.customers.append(customer)
            print(f'\033[36mПосетитель номер {customer.name} прибыл.')
            self.queue.put(customer)
            self.serve_customer(str(name))
        print('\033[39mВсе гости прибыли')
        for visitor in self.customers:  # ждем когда закроются потоки посетителей
            visitor.join()
        print('\033[38mОчередь пуста --- GAME OVER --- Кафе закрывается!')

    # Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
    def serve_customer(self, customer_name=''):
        if not self.queue.empty():  # Если клиенты в очереди есть
            for table in self.tables:  # Проверяет наличие свободных столов,
                if table.is_free:  # в случае наличия стола -
                    table.is_free = False
                    customer = self.queue.get()
                    customer.table = table
                    customer.start()  # начинает обслуживание посетителя (запуск потока),
                    return
            # в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
            print(f'\033[31mПосетитель номер {customer_name} ожидает свободный стол. (помещение в очередь)')


if __name__ == '__main__':
    # # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables_global = [table1, table2, table3]
    # tables_global = [Table(i) for i in range(1, 4)]

    # # Инициализируем кафе
    cafe = Cafe(tables_global)

    # # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()
