import cv2

img = cv2.imread('../images/messi5.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), -90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)