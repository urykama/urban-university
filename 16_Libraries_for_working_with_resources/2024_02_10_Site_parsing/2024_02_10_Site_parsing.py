# Программа должна считывать данные с сайта CoinMarketCap.
# Для парсинга и запросов разрешено использовать любую из перечисленных библиотек:
# requests, selenium, beautifulsoup, scrapy.
import csv
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver


def html_to_file(url='https://coinmarketcap.com/'):
    """Считывать данные с сайта: название криптовалюты, текущая рыночная капитализация"""
    driver = webdriver.Chrome()
    driver.get(url)
    scroll_pause_time = 0.2

    for _ in range(15):
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
        time.sleep(scroll_pause_time)
    src = driver.page_source
    with open('index.html', 'w', encoding="utf-8") as file:
        file.write(src)
    return src


def write_cmc_top():
    """Лучше реализовать эту программу в виде функции, например, назвав её write_cmc_top.
    Записывать данные в CSV файл в следующем порядке:
    название криптовалюты, текущая рыночная капитализация, процент от общей капитализации топ-100 криптовалют."""
    with open('index.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('tbody')
    tr = table.find_all('tr')
    coins_name = []
    coins_market_cap = []
    int_cmc = []
    for td in tr:
        try:
            coin_name = td.find('p', {'class': "sc-71024e3e-0 ehyBa-d"}).text
            coin_market_cap = td.find('span', {'class': 'sc-11478e5d-1'}).text
        except:
            print('ERROR: нет данных', td)
            continue
        coins_name.append(coin_name)
        coins_market_cap.append(coin_market_cap[1:])
        int_cmc.append(int(coin_market_cap[1:].replace(',', '')))
    sum_market_cap = sum(int_cmc)
    # 6.Каждый следующий файл при записи должен иметь название в следующем формате: H.M dd.mm.yyyy,
    # где H - Часы, M-минуты, dd- день, mm-месяц, yyyy-год.
    data_file_name = datetime.datetime.now().strftime("%H.%M. %d.%m.%Y") + '.csv'
    with open(data_file_name, mode='w', newline='', encoding='utf-8') as file:
        # 5.Разделитель между столбцами в CSV файле - пробелы.
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Name', 'MC', 'MP'])
        for i in range(len(coins_name)):
            # print([coins_name[i], coins_market_cap[i], f'{round(int_cmc[i] / sum_market_cap * 100, 2)}%'])
            writer.writerow([coins_name[i], coins_market_cap[i], f'{round(int_cmc[i] / sum_market_cap * 100, 2)}%'])
    print(f"Данные успешно записаны в файл: {data_file_name}")


if __name__ == '__main__':
    url = 'https://coinmarketcap.com/'
    html_to_file(url)
    write_cmc_top()
