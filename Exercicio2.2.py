import cv2
import os
import numpy as np

folder = "Files"
file = "baboon.png"

file_path = os.path.join(folder, file)

image = cv2.imread(file_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
R = image[:,:,2]
G = image[:,:,1]
B = image[:,:,0]
image_gray_manual = R * 0.299 + G * 0.587 + B * 0.114
image_gray_manual = np.round(image_gray_manual).astype(np.uint8)


image_float = image / 255.0
R = image_float[:,:,2]
G = image_float[:,:,1]
B = image_float[:,:,0]
image_float_gray_manual = R * 0.299 + G * 0.587 + B * 0.114


cv2.imshow("image_gray", image_gray)
cv2.imshow("image_gray_manual", image_gray_manual)
cv2.imshow("image_float_gray_manual", image_float_gray_manual)

cv2.waitKey()
cv2.destroyAllWindows()