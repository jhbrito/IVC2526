import cv2
import os
import numpy as np

folder = "Files"
file = "baboon.png"

file_path = os.path.join(folder, file)

image = cv2.imread(file_path)
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_HSV[:,:,0] = 120
image_HSV_BGR = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)

cv2.imshow("image", image)
cv2.imshow("HSV", image_HSV)
cv2.imshow("HSV_BGR", image_HSV_BGR)
cv2.waitKey()
