import inspect
import pprint


def introspection_info(
        obj: object = lambda: True):  # 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
    return {
        'Имя обекта:                    ': obj.__name__,
        'Тип объекта      (type)        ': type(obj),  # - Тип объекта.
        'Атрибуты объекта (attributes)  ': obj.__dict__,  # - Атрибуты объекта.
        'Методы объекта   (methods)     ': dir(obj),  # - Методы объекта.
        'Модуль, к которому объект принадлежит': obj.__module__,  # - Модуль, к которому объект принадлежит
        'Модуль, к которому объект принадлежит 2': inspect.getmodule(obj),  # - Модуль, к которому объект принадлежит
        'signature                      ': inspect.signature(obj),  # - Модуль, к которому объект принадлежит
        'isinstance(obj)                ': isinstance(obj, (float, int, str, list, dict, tuple,)),
        'inspect.isfunction(obj)        ': inspect.isfunction(obj),

    }


if __name__ == '__main__':
    pprint.pprint(introspection_info(introspection_info))
    print()
    pprint.pprint(introspection_info())

# indent Rainbow