import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((200, 300, 3), np.uint8)
img[50:150, 50:250, :] = 255
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 127, 255, 0)
_, none_contours, _ = cv2.findContours(binary_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_, sim_contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
none_img = cv2.drawContours(img, none_contours, -1, (0, 0, 255), 5)
sim_img = cv2.drawContours(img, sim_contours, -1, (0, 0, 255), 5)
plt.figure()
plt.subplot(121); plt.imshow(none_img); plt.xticks([]); plt.yticks([]); plt.title("cv2.CHAIN_APPROX_NONE")
plt.subplot(122); plt.imshow(sim_img); plt.xticks([]); plt.yticks([]); plt.title("cv2.CHAIN_APPROX_SIMPLE")
plt.show()
print("cv2.CHAIN_APPROX_NONE - the number of points: ", none_contours[0].shape[0])
print("cv2.CHAIN_APPROX_SIMPLE - the number of points: ", sim_contours[0].shape[0])