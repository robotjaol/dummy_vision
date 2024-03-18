import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# how to resize images
# image = cv.imread('data/image.png')
# assert image is not None, "File could not be, read check with os.path.exists()"

# res = cv.resize(image,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

# cv.imshow("input", image)
# cv.imshow("resize", res)

# cv.waitKey(0)
# cv.destroyAllWindows()

image = cv.imread('data/img/image.png', cv.IMREAD_GRAYSCALE)
assert image is not None, "File could not be, read check with.os.path.exists()"
rows,cols = image.shape

# M = np.float32([[1,0,100],[0,1,50]])
# flip = cv.warpAffine(image, M, (rows, cols))

# comparison
# cv.imshow('input', image)
# cv.imshow('result',flip)


# affine transfromation using matplotlib

# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(image,M,(cols,rows))
# plt.subplot(121),plt.imshow(image),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')


# Perspective transformation

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(image,M,(image.shape))

# plotting

plt.subplot(121), plt.imshow(image),plt.title("Input")
plt.subplot(122), plt.imshow(dst),plt.title("Output")

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

