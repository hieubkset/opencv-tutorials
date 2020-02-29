import cv2
import numpy as np

# find contours
img = cv2.imread('star.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, 1, 2)
img = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)

# find moments
cnt = contours[0]
M = cv2.moments(cnt)
print("Moments: ", M)

# find centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)
print("Centroid: (%d, %d)" % (cx, cy))

# find area
area = cv2.contourArea(cnt)
print("contourArea: ", area)
print("M['m00']: ", M['m00'])

# find perimeter
perimeter = cv2.arcLength(cnt, True)
print("perimeter: ", perimeter)

cv2.imshow('img', img)
cv2.waitKey(1)
