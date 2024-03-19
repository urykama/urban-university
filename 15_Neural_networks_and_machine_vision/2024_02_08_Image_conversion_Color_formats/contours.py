import cv2
import numpy as np
import math
import os

my_photo = cv2.imread('image/color_text.jpg')

filterd_image = cv2.medianBlur(my_photo, 7)
img_grey = cv2.cvtColor(filterd_image, cv2.COLOR_BGR2GRAY)

# set a thresh
thresh = 247

# get threshold image
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

# find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
# create an empty image for contours
img_contours = np.uint8(np.zeros((my_photo.shape[0], my_photo.shape[1])))

for contour in contours:
    print(contour[0][0][0])
    # if len(contour) < 5:
    #     continue
    color = (255, 255, 255)
    if contour[0][0][0] > 20:
        color = (0, 0, 255)
    if contour[0][0][0] > 50:
        color = (255, 0, 0)

    cv2.drawContours(img_contours, contour, -1, color, 1)
    cv2.imshow('res', img_contours)  # выводим итоговое изображение в окно
    cv2.waitKey()
cv2.drawContours(img_contours, contours, -1, (255, 255, 255), 1)

cv2.imshow('origin', my_photo)  # выводим итоговое изображение в окно
cv2.imshow('res', img_contours)  # выводим итоговое изображение в окно

cv2.waitKey()
cv2.destroyAllWindows()

