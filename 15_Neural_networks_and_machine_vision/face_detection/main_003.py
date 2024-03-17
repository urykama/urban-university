# https://waksoft.susu.ru/2021/04/02/raspoznavanie-licz-s-ispolzovaniem-opencv-v-python/

import cv2
import numpy as np


def eye_detect_02(image):
    # загрузите каскад Хаара для обнаружения этих лиц
    # faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    # img = cv2.imread(image)
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
        # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого

        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        if len(eyes) < 2:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue
        # for x, y, w, h in eyes:
            # print(x, y, w, h)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 200, 200), thickness=2)
        # Нарисуйте прямоугольник вокруг граней, который является нашей областью интереса (ROI)
        x, y, w, h = eyes[0]
        x1, y1, w1, h1 = eyes[1]
        # print(type(x), y, w, h)
        # print(x1, y1, w1, h1)

        # rect = cv2.rectangle(img, (min(x, x1), min(y, y1)), (max(x + w, x1 + w1), max(y + h, y1 + h1)), (200, 0, 200),
        #                      thickness=0)
        # roi = img[y:y + h, x:x + w]
        roi = img[min(y, y1):max(y + h, y1 + h1), min(x, x1):max(x + w, x1 + w1)]
        # применение размытия по Гауссу к этой новой прямоугольной области
        roi = cv2.GaussianBlur(roi, (35, 35), 35)
        # наложите это размытое изображение на исходное изображение, чтобы получить окончательное изображение
        img[min(y, y1):max(y + h, y1 + h1), min(x, x1):max(x + w, x1 + w1)] = roi
        # cv2.blur(rect.copy(), (5, 5))
        #     img = cv2.bitwise_and(img, rect)

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def eye_detect(image):
    # загрузите каскад Хаара для обнаружения этих лиц
    faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    img = cv2.imread(image)
    # cap = cv2.VideoCapture(1)
    temp = 0
    while True:
        temp += 1
        # success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
        # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого

        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
        print(len(eyes))
        for ex, ey, ew, eh in eyes:
            # print(x, y, w, h)
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 200, 200), thickness=2)

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()


def face_eye_detect(image):
    # загрузите каскад Хаара для обнаружения этих лиц
    faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    img = cv2.imread(image)
    # cap = cv2.VideoCapture(1)
    # success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
    # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого
    faces = faces_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=0)
    # Функция detectMultiScale() принимает изображение в качестве параметра
    # и обнаруживает объекты разных размеров в виде списка прямоугольников
    # print(results)
    for x, y, w, h in faces:
        # print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))
        img_eye = gray[x:x + w, y:y + h]
        eyes = eye_cascade.detectMultiScale(img_eye, scaleFactor=1.05, minNeighbors=0)
        for _ in range(10):
            for ex, ey, ew, eh in eyes:
                # print(x, y, w, h)
                cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 200, 200), thickness=2)

        # cv2.imshow("Result", img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    cv2.imshow("image", img)
    cv2.waitKey(0)
    # cap.release()
    cv2.destroyAllWindows()


def face_eye_detect_video_camera():
    # загрузите каскад Хаара для обнаружения этих лиц
    faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    # img = cv2.imread(image)
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
        # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого
        faces = faces_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # Функция detectMultiScale() принимает изображение в качестве параметра
        # и обнаруживает объекты разных размеров в виде списка прямоугольников
        # print(results)
        for x, y, w, h in faces:
            # print(x, y, w, h)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))
            img_eye = gray[x:x + w, y:y + h]
            eyes = eye_cascade.detectMultiScale(img_eye, scaleFactor=1.3, minNeighbors=5)
            for ex, ey, ew, eh in eyes:
                # print(x, y, w, h)
                cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 200, 200), thickness=2)

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def face_detect_video_camera():
    # загрузите каскад Хаара для обнаружения этих лиц
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    # img = cv2.imread(image)
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
        # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого
        results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # Функция detectMultiScale() принимает изображение в качестве параметра
        # и обнаруживает объекты разных размеров в виде списка прямоугольников
        # print(results)
        for x, y, w, h in results:
            # print(x, y, w, h)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def face_detect(image):
    # загрузите каскад Хаара для обнаружения этих лиц
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Функция imread() загружает изображение из указанного файла и возвращает его как N-мерный массив numpy
    img = cv2.imread(image)
    # cap = cv2.VideoCapture(1)
    # success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Функция cvtColor() преобразует входное изображение из одного цветового пространства в другое,
    # мы указали код cv2.COLOR_BGR2GRAY, что означает преобразование из BGR (Blue Green Red) в оттенки серого
    results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Функция detectMultiScale() принимает изображение в качестве параметра
    # и обнаруживает объекты разных размеров в виде списка прямоугольников
    print(results)
    for x, y, w, h in results:
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
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
    # face_eye_detect_video_camera()
    # face_detect_video_camera()
    images = ['images/1614543532_9-p-lyudi-na-belom-fone-10.jpg',
              'images/foto-i-kartinki-aplodismentov-6.jpg',
              # 'images/img_63.jpg',
              'images/rukovoditeli-novogo-.jpg']
    images02 = ['images/Screenshot_1.jpg',
                'images/Screenshot_2.jpg',
                'images/Screenshot_3.jpg',
                'images/Screenshot_4.jpg',
                'images/Screenshot_5.jpg']
    for i in images02:
        eye_detect_02(i)
        # face_eye_detect(i)
    #     face_detect(i)
    #     face_detect_SSD(i)
