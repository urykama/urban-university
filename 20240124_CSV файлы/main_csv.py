import csv


def add_list(kit, add_data):
    for elem in add_data.split(';'):
        kit.add(elem)
    return kit


def create_table(otvetka):
    # with open('python_snippets/external_data/travel-notes.csv', 'w', newline='', ) as csv_file:
    with open('holiday.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(otvetka)


def write_holiday_cities(first_letter):
    d1 = set()
    d2 = set()
    d3 = set()
    with open('travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            if first_letter == row[0][0]:
                d1 = add_list(d1, row[1])
                d2 = add_list(d2, row[2])
    create_table(['Посетили:'] + list(sorted(d1)))
    create_table(['Хотят посетить:'] + list(sorted(d2)))
    for i in sorted(d2):
        if i not in d1:
            d3.add(i)
    create_table(['Никогда не были в:'] + list(sorted(d3)))
    create_table(['Следующим городом будет:'] + [sorted(d2)[0]])

def start(letter):
    create_table([])
    create_table(['Информация о городах людей, имена которых начинаются на'] + [letter])
    write_holiday_cities(letter)

if __name__ == '__main__':
    start('A')  # Здесь менять первую букву имени
    start('E')  # Здесь менять первую букву имени
    start('L')  # Здесь менять первую букву имени
    start('R')  # Здесь менять первую букву имени

'''
    d = {
        "A": ['one', 'two', 'three', 'four', 'five'],
        "B": [1, 2, 3, 4, 5],
        "C": [0.1, 0.2, 0.3, 0.4, 0.5]
    }
    df = pd.DataFrame(d)
    print(df)
'''
