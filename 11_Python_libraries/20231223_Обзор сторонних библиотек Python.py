appid = "4db8cb3f1d00c7e959a7df5b329be556"# полученный при регистрации на OpenWeatherMap.org.
# Что-то вроде такого набора букв и цифр: "6d8e495ca73d5bbc1d6bf8ebd52c4123"


import requests as requests

# Проверка наличия в базе информации о нужном населенном пункте
def get_city_id(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass
    assert isinstance(city_id, int)
    return city_id


if __name__ == '__main__':
    get_city_id('Чишмы')
