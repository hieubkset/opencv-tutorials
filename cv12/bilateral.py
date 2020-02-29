import cv2
import matplotlib.pyplot as plt

img = cv2.imread('edge.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gauss = cv2.GaussianBlur(img, (5, 5), 0)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.figure()
plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(gauss), plt.title('Guass')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(bilateral), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()
