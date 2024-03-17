cars = ["BMW", "Mercedes-Benz", "LADA", "KIA", "HONDA"]
# "Mercedes-Benz" - необходимо писать полное название (PEP-8)

# for i in cars:
#     print('Я езжу на автомобиле марки', i)

# тут я решил сделать отдельно...
cars_count = 0
for i in cars:
    cars_count += 10
    print('cars_count:', cars_count, '\t', 'Я езжу на автомобиле марки', i)

for i in range(100):
    print(i)
    i += 9
