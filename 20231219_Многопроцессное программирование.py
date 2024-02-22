import multiprocessing
import random


# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:


class WarehouseManager():
    def __init__(self):
        # Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
        self.data = {}

    # Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
    def process_request(self, pipe):
        request, out, inp = pipe
        name, action, quantity = request
        # print('-=-=' * 8, name, action, quantity)
        if action == 'receipt':
            ret = quantity
        elif action == 'shipment':
            if self.data[name] - quantity < 0:
                print(f'Осталось только {self.data[name]} от запрошенных {quantity}')
                ret = 0
            else:
                ret = - quantity
        else:
            print('Ошибка: действие не опознано')

        inp.send(ret)
        inp.close()
        # Есть 2 действия: receipt - получение, shipment - отгрузка.
        # а) В случае получения данные должны поступить в data
        # (добавить пару, если её не было и изменить значение ключа, если позиция уже была в словаре)
        # б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).

    # 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс,
    # запускает его(start) и замораживает(join).
    def run(self, requests):
        for request in requests:
            name = request[0]
            # print(request, name)
            output_c, input_c = multiprocessing.Pipe()
            pr = multiprocessing.Process(target=self.process_request, args=((request, output_c, input_c),))
            pr.start()
            ret = output_c.recv()
            if name not in self.data:
                self.data[name] = 0
            self.data[name] += ret
            pr.join()


class WarehouseManagerNotMulti():
    def __init__(self):
        # Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
        self.data = {}

    # Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
    def process_request(self, request):
        name, action, quantity = request
        print('-=-=' * 8, name, action, quantity)
        if action == 'receipt':
            return quantity
        elif action == 'shipment':
            if self.data[name] - quantity < 0:
                print(f'Осталось только {self.data[name]} от запрошенных {quantity}')
                return 0
            else:
                return - quantity
        else:
            print('Ошибка: действие не опознано')

    def run(self, requests):
        for request in requests:
            name = request[0]
            print(request, name)
            if name not in self.data:
                self.data[name] = 0
            self.data[name] += self.process_request(request)


if __name__ == '__main__':
    manager = WarehouseManager()
    # manager = WarehouseManagerNotMulti()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    # requests = [
    #     ("product1", "receipt", 100),
    #     ("product2", "receipt", 150),
    #     ("product1", "shipment", 30),
    #     ("product3", "receipt", 200),
    #     ("product2", "shipment", 50),
    #     ("product1", "receipt", 100),
    #     ("product2", "receipt", 150),
    #     ("product1", "shipment", 70),
    #     ("product3", "receipt", 200),
    #     ("product2", "shipment", 50)
    # ]
    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)

    # Вывод на консоль:
    # {"product1": 70, "product2": 100, "product3": 200}
