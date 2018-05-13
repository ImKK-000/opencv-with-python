import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png')

edges = cv2.Canny(img,100,200)
blur = cv2.GaussianBlur(edges,(51,51),0)

plt.subplot(1,3,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2),plt.imshow(edges),plt.title('Edges')
plt.xticks([]), plt.yticks([])

plt.subplot(1,3,3),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()
