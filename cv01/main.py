import cv2 as cv

image = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('image', image)
k = cv.waitKey(0)
if k == 27:  # wait for Esc key to exit
    cv.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv.imwrite('gray_image.jpg', image)
    cv.destroyAllWindows()
