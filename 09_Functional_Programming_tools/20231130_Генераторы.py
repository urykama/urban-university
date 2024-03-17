def all_variants(line):
    text = str(line)  # чтоб работало и с INT и FLOAT
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


for substr in all_variants('12345'):
    print(substr)

# a = all_variants(12345)
# print(next(a))
# print(next(a))
# print(next(a))

# def fibo(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# fib = fibo(n=10)
# print(fib)
# for i in fib:
#     print(i)
