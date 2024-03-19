# можно подобрать параметры (пороги гистерезиса) для поика контура
# w, s, e, d - крутилки
# q == exit

import cv2


def contur(image):
    # img = cv2.imread(image)
    # filterd_image = cv2.medianBlur(img, 7)  # фильтрация, размытие
    # b, g,  r = cv2.split(filterd_image)
    #
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.imread(image, 0)  # загружаем как ЧБ картинку

    t1, t2 = 53, 125  # t1 и t2, так что t1>t2, называемый порогом гистерезиса
    t1, t2 = 21, 51
    img_canny = cv2.Canny(img_gray, t1, t2, L2gradient=False)
    print(t1, t2)
    cv2.imshow("img_gray_L2gradient=False", img_canny)
    while (key := cv2.waitKey(0) & 0xFF) != ord('q'):
        img_canny = cv2.Canny(b, t1, t2, L2gradient=True)
        print(t1, t2)
        cv2.imshow("image b", img_canny)

        if key == ord('w') and t1 < 255:
            t1 += 1
        elif key == ord('s') and t1 > 0:
            t1 -= 1
        elif key == ord('e') and t2 < 255:
            t2 += 1
        elif key == ord('d') and t2 > 0:
            t2 -= 1


if __name__ == '__main__':
    images = ['image/color_text.jpg', ]
    contur(images[0])
