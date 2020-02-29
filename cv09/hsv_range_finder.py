import cv2

frame_hsv = None

def print_hsv(event, col, row, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(frame_hsv[row][col])


cv2.namedWindow('frame')
cv2.setMouseCallback('frame', print_hsv)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('p'):
        break

frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

cv2.waitKey(0)

cv2.destroyAllWindows()
