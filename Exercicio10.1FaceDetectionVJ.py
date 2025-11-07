import time
import cv2
import os
import numpy as np

classifier_folder = cv2.data.haarcascades
classifier_file = 'haarcascade_frontalface_alt.xml'
face_detector = cv2.CascadeClassifier(os.path.join(classifier_folder, classifier_file))

cap = cv2.VideoCapture()

before = 0

while True:
    now = time.time()
    fps = 1/ (now - before)
    before = now

    if not(cap.isOpened()):
        cap.open(0)

    ret, frame = cap.read()
    h, w, c = frame.shape

    frame_mirror = frame[:, ::-1, :]

    faces = face_detector.detectMultiScale(frame_mirror, scaleFactor=1.1)

    image_faces = frame_mirror.copy()

    for face in faces:
        (x, y, w, h) = face
        p1 = (x, y)
        p2 = (x + w, y+ h)
        cv2.rectangle(img=image_faces,
                      pt1=p1,
                      pt2=p2,
                      color=(255, 0, 0),
                      thickness=2)


    text_to_show = "{} fps".format(np.round(fps))
    cv2.putText(img=image_faces,
                text=text_to_show,
                org=(10, 30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 255, 0),
                thickness=2)

    if ret:
        cv2.imshow("faces", image_faces)
        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()


