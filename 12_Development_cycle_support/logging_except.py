import logging

def perky(param):
    return param / 0

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('perky.log', 'w', 'utf-8')], )

number = 36
try:
    logging.info('Посмотрим как у него это получиться...')
    perky(number)
    logging.info('Он смог!')
except Exception:
    logging.exception(f'Дерзкий не справился с {number}')
