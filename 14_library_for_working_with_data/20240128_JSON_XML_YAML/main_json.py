# Напишите функцию employees_rewrite(sort_type), которая:
# Принимает параметром тип сортировки (ключ) - sort_type.
# Функция должна:
# Получить данные из employees.json и записать в employees_[sort_type]_sorted.json:
# Формат записи должен быть как в исходном файле.
# Если сортировка производится по строковым значения, то в алфавитном порядке.
# Если сортировка производится по числовым значениям, то в порядке убывания.
import json
from operator import itemgetter


def employees_rewrite(sort_type: str):
    with open('employees.json', 'r', newline='', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
    for key in data['employees'][0]:
        if sort_type.lower() == key.lower():
            sort_type = key
            break
    else:
        raise ValueError('Bad key for sorting')
    # Если сортировка производится по числовым значениям, то в порядке убывания
    # reverse_type = str(data['employees'][0][sort_type]).isdigit()
    try:  # а если число не целое (float), или просто с точкой (256.)
        float(data['employees'][0][sort_type])
        reverse_type = True
    except ValueError:
        reverse_type = False
    sort_list = sorted(data['employees'], key=itemgetter(sort_type), reverse=reverse_type)
    with open(f'employees_{sort_type}_sorted.json', 'w', encoding='utf-8') as f:
        json.dump(sort_list, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    employees_rewrite('firstName')
    employees_rewrite('lastName')
    employees_rewrite('department')
    employees_rewrite('salary')

    # list = [{"name": "Nandini", "age": 20},
    #         {"name": "Manjeet", "age": 20},
    #         {"name": "Nikhil", "age": 19}]
    #
    # # using sorted and itemgetter to print list sorted by age
    # print("Список напечатан с сортировкой по возрасту: ")
    # print(sorted(list, key=itemgetter('age')))
    #
    # print("\r")
    #
    # # using sorted and itemgetter to print
    # # list sorted by both age and name
    # # notice that "Manjeet" now comes before "Nandini"
    # print("Список напечатан с сортировкой по возрасту и имени: ")
    # print(sorted(list, key=itemgetter('age', 'name')))
    #
    # print("\r")
    #
    # # using sorted and itemgetter to print list
    # # sorted by age in descending order
    # print("The list printed sorting by age in descending order: ")
    # print(sorted(list, key=itemgetter('age'), reverse=True))