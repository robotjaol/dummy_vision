import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("data/img/image.png", cv.IMREAD_GRAYSCALE)

if image is None:
    assert image is None, "File could not be created, check with os.path.exists"

ret,tresh1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
ret,tresh2 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
ret,tresh3 = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
ret,tresh4 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
ret,tresh5 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['ORIGINAL IMAGE', 'BINARY', 'BINARY INVERSE', 'TRUNC', 'TOZERO', 'TOZERO INVERSE']
images = [image, tresh1, tresh2, tresh3, tresh4, tresh5]

for i in range(6):
    plt.subplot(2, 3,i+1), plt.imshow(images[i], 'gray', vmin = 0, vmax = 255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv.imshow('image', image)
# cv.waitKey(0)
# cv.destroyAllWindows()