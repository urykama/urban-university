import logging

def prime_numbers_generator(n):
    prime_numbers = [2, ]
    for number in range(3, n + 1, 2):
        logging.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                logging.debug(f'{number} делиться на {prime}')
                break
        else:
            logging.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number

# и чё? первые 5 минут вообще ни о чём, Василий полистай хотя-бы - книгу (с девушкой на обложке))),
# сравни, потом скажешь
