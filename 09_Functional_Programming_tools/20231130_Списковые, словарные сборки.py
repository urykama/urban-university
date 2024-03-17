input_date = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def square(input: int):
    return input ** 2


def filterIsOdd(input: int):
    return input % 2


result = map(square, filter(filterIsOdd, input_date))
print(list(result))
