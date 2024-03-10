import logging

log = logging.getLogger('primes')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler('primes.log', 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

def prime_numbers_generator(n):
    prime_numbers = [2, ]
    for number in range(3, n + 1, 2):
        log.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                log.debug(f'{number} делиться на {prime}')
                break
        else:
            log.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number
