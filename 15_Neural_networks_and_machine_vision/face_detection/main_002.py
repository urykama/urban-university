# https://waksoft.susu.ru/2021/04/02/raspoznavanie-licz-s-ispolzovaniem-opencv-v-python/

import cv2
import numpy as np

def face_detect(image):
    img = cv2.imread(image)
        # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    # cap = cv2.VideoCapture(1)
    # success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
        # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # загрузите каскад Хаара для обнаружения этих лиц
    results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # Функция detectMultiScale() принимает изображение в качестве параметра
        # и обнаруживает объекты разных размеров в виде списка прямоугольников
    print(results)
    for x, y, w, h in results:
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))

    cv2.imshow("Result", img)
    cv2.waitKey(0)

def face_detect_SSD(image):
    # https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
    prototxt_path = "weights/deploy.prototxt.txt"
    # https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel
    model_path = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"
        # Теперь, чтобы загрузить реальную модель, нам нужно использовать метод readNetFromCaffe(),
        # который принимает в качестве аргументов архитектуру модели и веса:
        # загрузим модель Caffe
    model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    # читаем изображение
    image = cv2.imread(image)
    # получаем ширину и высоту изображения
    h, w = image.shape[:2]
    # предварительная обработка: изменение размера и вычитание среднего
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    # устанавливаем на вход нейронной сети изображение
    model.setInput(blob)
    # выполняем логический вывод и получаем результат
    output = np.squeeze(model.forward())
    # Теперь выходной объект содержит все обнаруженные объекты (в данном случае лица),
    # давайте переберем этот массив и нарисуем все лица на изображении с достоверностью более 50%:
    font_scale = 1.0

    for i in range(0, output.shape[0]):
        # получить уверенность
        confidence = output[i, 2]
        # если достоверность выше 50%, то нарисуйте окружающий прямоугольник
        if confidence > 0.5:
            # получить координаты окружающего блока и масштабировать их до исходного изображения
            box = output[i, 3:7] * np.array([w, h, w, h])
            # преобразовать в целые числа
            print('print(box)', box)
            print((np.round(box)))
            print(box.astype(np.int_))

            start_x, start_y, end_x, end_y = box.astype(np.int_)
            # start_x, start_y, end_x, end_y = np.round(box)
            print(type(start_x))
            # рисуем прямоугольник вокруг лица
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
            # также нарисуем текст
            cv2.putText(image, f"{confidence * 100:.2f}%", (start_x, start_y - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                        (255, 0, 0), 2)
    # show the image
    cv2.imshow("image", image)
    cv2.waitKey(0)
    # save the image with rectangles
    # cv2.imwrite("kids_detected_dnn.jpg", image)

if __name__ == '__main__':
    images = ['images/1614543532_9-p-lyudi-na-belom-fone-10.jpg',
              'images/foto-i-kartinki-aplodismentov-6.jpg',
              'images/img_63.jpg',
              'images/rukovoditeli-novogo-.jpg']
    for i in images:
        face_detect(i)
        face_detect_SSD(i)
