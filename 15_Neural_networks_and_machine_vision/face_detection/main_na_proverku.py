# https://waksoft.susu.ru/2021/04/02/raspoznavanie-licz-s-ispolzovaniem-opencv-v-python/

import cv2
import numpy as np


def eye_detect_02():
    # загрузите каскад Хаара для обнаружения этих глаз
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # Теперь создадим объект VideoCapture, чтобы, как следует из названия, «захватывать» видео
    cap = cv2.VideoCapture(1)
    # цикл while, чтобы получать из источника кадр за кадром
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



if __name__ == '__main__':
    eye_detect_02()
