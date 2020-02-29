import numpy as np
import cv2

# Tao mot hinh mau den
img = np.zeros((512, 512, 3), np.uint8)

# Ve duong thang
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Ve hinh chu nhat
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Ve hinh tron
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Them text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

# Hien thi buc anh
cv2.imshow('image', img)
cv2.waitKey(0)