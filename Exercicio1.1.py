import cv2
import os

folder = "Files"
file = "baboon.png"

file_path = os.path.join(folder, file)

image = cv2.imread(file_path)
image = image / 255.0

image = image + 100/255.0



cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

video_file = "vtest.avi"
cap = cv2.VideoCapture(os.path.join(folder, video_file))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(33)
    else:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()


