import cv2
import time

img1 = cv2.imread('messi5.jpg')

t1 = time.time()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
t2 = time.time()
t = t2 - t1

print("Result I got %.2f seconds" % t)