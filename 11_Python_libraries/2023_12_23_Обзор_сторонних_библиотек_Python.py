# import requests
#
# # Запрос данных с помощью метода GET
# response = requests.get('https://api.example.com/data')
#
# # Проверка статуса запроса
# if response.status_code == 200:
#     data = response.json()  # Получение данных в формате JSON
#     print(data)
# else:
#     print('Ошибка при запросе данных:', response.status_code)

# import pandas as pd
#
# # Чтение данных из CSV файла
# df = pd.read_csv('data.csv')
#
# # Вывод первых нескольких строк данных
# print(df.head())
#
# # Выполнение простого анализа данных
# print(df.describe())

import numpy as np

# Создание массива чисел от 1 до 10
arr = np.arange(1, 11)

# Вывод массива
print(arr)

# Выполнение математических операций
print('Сумма элементов:', np.sum(arr))
print('Среднее значение:', np.mean(arr))

import matplotlib.pyplot as plt

# Создание данных
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Построение графика
plt.plot(x, y)
plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('Синусоидальная волна')
plt.grid(True)
plt.show()
#
# from PIL import Image, ImageFilter
#
# # Открытие изображения
# img = Image.open('image.jpeg')
#
# # Изменение размера изображения
# resized_img = img.resize((300, 200))
#
# # Применение эффекта
# blurred_img = img.filter(ImageFilter.BLUR)
#
# # Сохранение изображения в другом формате
# resized_img.save('resized_image.jpg')
# blurred_img.save('blurred_image.jpg')
# Эти примеры демонстрируют,
# как можно использовать различные сторонние библиотеки в Python для решения различных задач.
# Каждая библиотека предоставляет мощные инструменты для работы с данными, визуализации и обработки изображений,
# что делает их полезными для широкого спектра приложений.
