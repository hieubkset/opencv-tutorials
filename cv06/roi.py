import cv2

img = cv2.imread('messi5.jpg')
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)
cv2.waitKey(0)