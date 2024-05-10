import cv2
import numpy as np

my_photo = cv2.imread('image/color_text.jpg')

# предобработка. воспользуемся медианным фильтром
filterd_image = cv2.medianBlur(my_photo, 7)

# цветное в ЧБ
img_grey = cv2.cvtColor(filterd_image, cv2.COLOR_BGR2GRAY)

# зададим порог
thresh = 247

# получим картинку, обрезанную порогом
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

# надем контуры
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# создадим пустую картинку
img_contours_gray = np.uint8(np.zeros((my_photo.shape[0], my_photo.shape[1])))
# ЧБ в цветное
img_contours = cv2.cvtColor(img_contours_gray, cv2.COLOR_GRAY2BGR)

sel_countours_b = []
sel_countours_g = []
sel_countours_r = []
for j in range(1, 10):
    sel_countours_b.append(contours[j])
cv2.drawContours(img_contours, sel_countours_b, -1, (0, 0, 255), 1)  # отобразим контуры
for j in range(10, 20):
    sel_countours_g.append(contours[j])
cv2.drawContours(img_contours, sel_countours_g, -1, (255, 150, 80), 1)
for j in range(20, 33):
    sel_countours_r.append(contours[j])
cv2.drawContours(img_contours, sel_countours_r, -1, (255, 255, 255), 1)

cv2.imshow('res', img_contours)  # выводим итоговое изображение в окно
cv2.waitKey()

