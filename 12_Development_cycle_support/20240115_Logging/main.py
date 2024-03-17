import requests
import logging


# закоментированно и изменено, чтобы логи были как в задании
# логи ошибок переделывать не стал, сорян
log_200 = logging.getLogger('RequestsLogger')
log_200.setLevel(logging.INFO)
log_200_fh = logging.FileHandler('success_responses.log', 'w', 'utf-8')
# log_200_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_200_formatter = logging.Formatter('%(message)s')
log_200_fh.setFormatter(log_200_formatter)
log_200.addHandler(log_200_fh)

log_bad = logging.getLogger('RequestsLoggerBad')
log_bad.setLevel(logging.INFO)
log_bad_fh = logging.FileHandler('bad_responses.log', 'w', 'utf-8')
# log_bad_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_bad_formatter = logging.Formatter('%(message)s')
log_bad_fh.setFormatter(log_bad_formatter)
log_bad.addHandler(log_bad_fh)

log_error = logging.getLogger('RequestsLoggerError')
log_error.setLevel(logging.ERROR)
log_error_fh = logging.FileHandler('blocked_responses.log', 'w', 'utf-8')
# log_error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_error_formatter = logging.Formatter('%(message)s')
log_error_fh.setFormatter(log_error_formatter)
log_error.addHandler(log_error_fh)


def respond(site):
    try:
        response = requests.get(site, timeout=3)
        if response.status_code == 200:
            # log_200.info(f'Получен ответ 200 от сайта: {site}')
            log_200.info(f"INFO: '{site}', response - 200")
        else:
            # log_bad.info(f'Получен ответ {response.status_code} от сайта: {site}')
            log_bad.info(f"WARNING: '{site}', response - {response.status_code}")
    except requests.exceptions.Timeout:
        log_error.exception(f'Сервер болеет, можно попробовать ретрай через N секунд: {site}')
    except requests.exceptions.TooManyRedirects:
        log_error.exception(f'Вероятно некорректный URL сайта: {site}')
    except requests.ConnectionError:
        log_error.exception(f'Нет соединения с сервером сайта: {site}')
    except:
        # log_error.exception(f'Не удалось получить ответ от сайта: {site}')
        log_error.exception(f'ERROR: {site}, NO CONNECTION')


def run(sites):
    for i in range(len(sites)):
        site = sites[i]
        print(f'{i + 1} из {len(sites)} \t {site}')
        respond(site)


if __name__ == '__main__':
    sites = ['https://www.youtube.com', 'https://instagram.com', 'https://wikipedia.org',
             'https://yahoo.com', 'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com',
             'https://amazon.com', 'https://tiktok.com', 'https://www.ozon.ru']
    # sites = ['https://www.youtube.com', 'https://instagram.com', 'https://wikipedia.org',]
    run(sites)
