import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("Range HSV")
cv2.resizeWindow("Range HSV", 500, 350)
cv2.createTrackbar("HUE Min", "Range HSV", 0, 180, empty)
cv2.createTrackbar("HUE Max", "Range HSV", 180, 180, empty)
cv2.createTrackbar("SAT Min", "Range HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "Range HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "Range HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "Range HSV", 255, 255, empty)


webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    # get value from trackbar
    h_min = cv2.getTrackbarPos("HUE Min", "Range HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "Range HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "Range HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "Range HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "Range HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "Range HSV")

    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.inRange(hsv, lower_range, upper_range)
    bitwise = cv2.bitwise_and(frame, frame, mask=thresh)
    contours, hierarchy = cv2.findContours(thresh,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 600):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(imageFrame, "Bola Ping Ping", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('hsv', hsv)
    cv2.imshow('thresh', thresh)
    cv2.imshow('bitwise', bitwise)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
