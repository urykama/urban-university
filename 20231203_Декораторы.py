#  Изначально по определению простым является натуральное число.
#  А натуральным могут быть только целые и положительные числа.
#  Целое число 1 не является ни простым, ни составным числом.
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print('Не простое')
        elif result == 2:
            print('Простое')
        elif result % 2 == 0:
            print('Составное')
        else:
            for i in range(3, int(result ** 0.5 + 1), 2):
                if result % i == 0:
                    print('Составное')
                    break
            print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


# result = sum_three(1, 0, 0)
# print(result)
print(sum_three(0, 0, 0))
print(sum_three(0, 0, 1))
print(sum_three(0, 1, 1))
print(sum_three(1, 1, 1))
print(sum_three(1, 1, 2))
print(sum_three(1, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(2, 2, 3))
