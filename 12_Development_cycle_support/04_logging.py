import logging
from primes import prime_numbers_generator

'''
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
'''

logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler('primes.log', 'w', 'utf-8')], )

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генератора {prime}')
