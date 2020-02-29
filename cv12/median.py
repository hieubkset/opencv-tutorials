import cv2
import matplotlib.pyplot as plt

img = cv2.imread('noise.png')
median = cv2.medianBlur(img, 5)

plt.figure()
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
