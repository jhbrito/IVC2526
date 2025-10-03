import cv2

h = 90
s = 128


def on_trackbar_change_H(val):
    global h
    h = val


def on_trackbar_change_S(val):
    global s
    s = val


cv2.namedWindow("HSV")
cv2.createTrackbar("H", "HSV", h, 180, on_trackbar_change_H)
cv2.createTrackbar("S", "HSV", s, 255, on_trackbar_change_S)

cap = cv2.VideoCapture()

while True:
    if not(cap.isOpened()):
        cap.open(0)

    ret, frame = cap.read()

    if ret:
        frame_mirror = frame[:, ::-1, :]
        image_HSV = cv2.cvtColor(frame_mirror, cv2.COLOR_BGR2HSV)
        image_HSV[:, :, 0] = h
        image_HSV[:, :, 1] = s
        image_HSV_BGR = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)

        cv2.imshow("HSV", image_HSV_BGR)
        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
