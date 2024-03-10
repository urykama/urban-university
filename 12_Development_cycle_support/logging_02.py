import logging

def perky(param):
    return param / 0

log = logging.getLogger('perky')
log.setLevel(logging.INFO)
fh = logging.FileHandler('perky.log', 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

number = 36
try:
    log.info('Посмотрим как у него это получиться...')
    perky(number)
    log.info('Он смог!')
except Exception:
    log.exception(f'Дерзкий не справился с {number}')
