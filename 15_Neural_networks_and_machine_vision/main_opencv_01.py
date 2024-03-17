import numpy as np
import cv2

img = np.zeros((400, 400, 3), dtype='uint8')
cv2.circle(img, (200, 200), 150, (255, 255, 255), 3)
for d in (25, 50):
    cv2.ellipse(img, (200, 200), (d, d), 0, 0, 180, (0, 255, 0), 3)
for x in (150, 175, 225, 250):
    cv2.line(img, (x, 150), (x, 200), (255, 0, 0), 3)
for x in (150, 225):
    cv2.line(img, (x, 150), (x + 25, 150), (0, 0, 255), 3)
cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255))

cv2.imshow('Photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# свой вариант логотипа...
imgq = np.zeros((400, 400, 3), dtype='uint8')
cv2.circle(img, (200, 200), 150, (255, 255, 255), 3)
red = (0, 0, 255)
blue = (255, 0, 0)
for d in (25, 50):
    cv2.ellipse(img, (200, 200), (d, d), 0, 0, 90, blue, 3)
    cv2.ellipse(img, (200, 200), (d, d), 0, 90, 180, red, 3)
for x, c in ([150, red], [175, red], [225, blue], [250, blue]):
    cv2.line(img, (x, 150), (x, 200), c, 3)
for x, c in ([150, red], [225, blue]):
    cv2.line(img, (x, 150), (x + 25, 150), c, 3)

cv2.imshow('Photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
