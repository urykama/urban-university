import cv2

def face_detect(image):
    img = cv2.imread(image)
    cap = cv2.VideoCapture(1)
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    print(results)
    for x, y, w, h in results:
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))

    cv2.imshow("Result", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    face_detect('images/1614543532_9-p-lyudi-na-belom-fone-10.jpg')
    face_detect('images/foto-i-kartinki-aplodismentov-6.jpg')
    face_detect('images/img_63.jpg')
    face_detect('images/rukovoditeli-novogo-.jpg')

