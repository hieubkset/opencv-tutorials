import cv2

cap = cv2.VideoCapture('output.avi')

while cap.isOpened():
    ret, frame = cap.read()

    # video is end
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
