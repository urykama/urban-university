# Разработайте функцию для извлечения информации из HTML-текста (строки Python)
# о ссылках на изображения (URL-адресах картинок).
# Функция должна находить все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и возвращать их список.
#
# 1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
# 2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
# 3. Верните список всех найденных ссылок на изображения.

import re


def extract_image_links(html_text):
    return re.findall('http[^\"|\']*\.(?:jpeg|jpg|gif|png)', html_text)


sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>" \
              " <img src='https://example.com/image3.gif'>"

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")


# дальше решения задачи с CODEWARS
# def get_number_from_string(st):
#     # q1 = (re.findall('\d', st))
#     # ret = ''
#     # ret = ret.join(q1)
#     #
#     # return ret
#     # return ''.join(re.findall('\d', st))
#     return int(re.sub(r'\D', '', st))
#
#
# tests = (
#     ("1", 1),
#     ("123", 123),
#     ("this is number: 7", 7),
#     ("$100 000 000", 100000000),
#     ("hell5o wor6ld", 56),
#     ("one1 two2 three3 four4 five5", 12345),)
# print(get_number_from_string('1'))
# print(get_number_from_string('123'))
# print(get_number_from_string("one1 two2 three3 four4 five5"))