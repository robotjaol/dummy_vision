import cv2
import numpy as np


# img = ('data/img/image.png')

def draw_circle(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),50,(0,255,0),-1)

cv2.namedWindow(winname="My Drawing")
cv2.setMouseCallback('My Drawing',draw_circle)

img = np.zeros((512, 512, 3), np.int8)

while True:
    cv2.imshow('My Drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
