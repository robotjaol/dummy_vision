import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])        # warna Biru
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([40, 50, 50])        # warna Hijau
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([0, 50, 50])          # warna Merah
    upper_red = np.array([10, 255, 255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_red = cv.inRange(hsv, lower_red, upper_red)

    mask_combined = mask_blue | mask_green | mask_red    #jika ingin ditampilkan dalam satu frame
    res = cv.bitwise_and(frame, frame, mask=mask_combined)

    cv.imshow('frame', frame)
    # cv.imshow('mask_combined', mask_combined)   #jika ingin ditampilkan dalam satu frame
    cv.imshow('mask_blue', mask_blue)
    cv.imshow('mask_green', mask_green)
    cv.imshow('mask_red', mask_red)
    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
cap.release()
