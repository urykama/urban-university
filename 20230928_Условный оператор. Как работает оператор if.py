x = 38

print('дратути!')
if x < 0:
    print('x =', x, '\tменьше нуля')
elif x == 0:
    print('x =', x, '\tравно нулю')
else:
    print('x =', x, '\tбольше нуля')
print('дотвидания!')

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех a > b and a > 0')

if (a > b) and (a > 0 or b < 1000):
    print('успех (a > b) and (a > 0 or b < 1000)')

# if 5 < b and b < 10:
if 5 <= b < 10:
    print('успех 5 <= b < 10')

if '34' > '123':
    print("успех '34' > '123'")

if '123' > '12':
    print("успех '123' > '12'")

if [1, 2] > [1, 1]:
    print('успех [1, 2] > [1, 1]')

if '6' != 5:
    print("успех '6' != 5'")

if '6' > 5:
    print('успех')

if [5, 6] > 5:
    print('успех [5, 6] > 5')
