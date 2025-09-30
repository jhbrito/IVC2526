import cv2
import os

folder = "Files"
file = "baboon.png"

file_path = os.path.join(folder, file)

image = cv2.imread(file_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def ivc_remove_red(src):
    dst = src.copy()
    dst[:,:,2] = 0
    return dst


def ivc_remove_green(src):
    dst = src.copy()
    dst[:,:,1] = 0
    return dst


def ivc_remove_blue(src):
    dst = src.copy()
    dst[:,:,0] = 0
    return dst


def ivc_gray_negative(src):
    dst = src.copy()
    dst = 255 - dst
    return dst


image_no_red = ivc_remove_red(image)
image_no_green = ivc_remove_green(image)
image_no_blue = ivc_remove_blue(image)
image_gray_negative = ivc_gray_negative(image_gray)


cv2.imshow("Image", image)
cv2.imshow("Image no red", image_no_red)
cv2.imshow("Image no green", image_no_green)
cv2.imshow("Image no blue", image_no_blue)
cv2.imshow("Image Gray", image_gray)
cv2.imshow("Image Gray Negative", image_gray_negative)

cv2.waitKey(0)

