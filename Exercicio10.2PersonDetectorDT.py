import time
import cv2
import os
import numpy as np

use_cam = False
folder ="Files"
file = "vtest.avi"

if use_cam:
    cap = cv2.VideoCapture()
else:
    cap = cv2.VideoCapture(os.path.join(folder, file))

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())

before = 0

while True:
    now = time.time()
    fps = 1/ (now - before)
    before = now

    if not(cap.isOpened()):
        cap.open(0)

    ret, frame = cap.read()
    if ret:
        h, w, c = frame.shape

        if use_cam:
            frame_mirror = frame[:, ::-1, :]
        else:
            frame_mirror = frame

        persons, _ = hog.detectMultiScale(frame_mirror, winStride=(8, 8), scale=1.1)

        image_persons = frame_mirror.copy()

        for person in persons:
            (x, y, w, h) = person
            p1 = (x, y)
            p2 = (x + w, y+ h)
            cv2.rectangle(img=image_persons,
                          pt1=p1,
                          pt2=p2,
                          color=(255, 0, 0),
                          thickness=2)


        text_to_show = "{} fps".format(np.round(fps))
        cv2.putText(img=image_persons,
                    text=text_to_show,
                    org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 255, 0),
                    thickness=2)


        cv2.imshow("persons", image_persons)
        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
