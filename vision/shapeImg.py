import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path = "img/puppy.jpg"
img = plt.imread(img_path)

plt.imshow(img)
plt.show()

# picShape = np.asarray(img)
# picShape.shape
# plt.imshow(picShape)
# plt.show()