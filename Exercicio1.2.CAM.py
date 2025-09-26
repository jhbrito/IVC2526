import cv2
import os


cap = cv2.VideoCapture()

while True:
    if not(cap.isOpened()):
        cap.open(0)

    ret, frame = cap.read()
    h, w, c = frame.shape

    frame_mirror = frame[:, ::-1, :]

    if ret:
        cv2.imshow("frame", frame_mirror)
        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()


