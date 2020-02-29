import cv2
import matplotlib.pyplot as plt

image = cv2.imread('messi5.jpg')
level1 = image
level2 = cv2.pyrDown(level1)
level3 = cv2.pyrDown(level2)
level4 = cv2.pyrDown(level3)

plt.figure()
plt.subplot(411), plt.imshow(level4)
plt.subplot(412), plt.imshow(level3)
plt.subplot(413), plt.imshow(level2)
plt.subplot(414), plt.imshow(level1)
plt.show()