import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('haarcascade_eye.xml')

    results = faces.detectMultiScale(gray_img, scaleFactor=1.7, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in results:
        square = cv2.rectangle(img.copy(), (x - 55, y), (x + w + 30, y + h), (150, 150, 150), thickness=-1)
        cv2.blur(square.copy(), (5, 5))
        img = cv2.bitwise_and(img, square)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# cv2.imwrite('image_eye_1.jpg', img)
